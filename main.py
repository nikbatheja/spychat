#import spy details and friend details from a diff. program
from spydetails import spy, friends
#import steganoraphy
from steganography.steganography import Steganography
from datetime import datetime

#enter the status messages the user would want to set
STATUS_MESSAGES = ['My name is Tony Stark', 'I am IRON MAN.']


#basic hello
print 'Hello! Let\'s get started'

#ask the user if he/she wants to continue with the details imported from spydetails
question = 'Do you want to continue as ' + spy['salutation'] + " " + spy['spy_name'] + ' (Y/N)? '
#take the users input
existing = raw_input(question)

#define add status and show the current status message of the user
def add_status(current_status_message):

    updated_status_message = None

#if the users current message is something , print it
    if current_status_message != None:
        print 'Your current status  is %s \n' % (current_status_message)
# else the text given below will be printed
    else:
        print 'You don\'t have any status currently \n'

#ask the user if he/she would like to select a status from the options given above
    default = raw_input('Do you want to select from the older status (y/n)? ')

#if the user selects no , he will be asked to enter the status he wants to set
    if default.upper() == 'N':
        new_status_message = raw_input('What status do you want to set? ')


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

# else if he selected yes he will be able to select a status from the above messages
    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input('\nChoose from the given messages '))


        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

#if the user selected an option other than y or n , he will be prompted to select either y or n once again
    else:
        print 'Not a valid option! Press either y or n.'

    if updated_status_message:
        print 'Your updated status is: %s' % (updated_status_message)

#now that the user has selected a status , it will be displayed as the new update status of the user
    else:
        print 'You currently don\'t have a status update'

    return updated_status_message


#second option in the menu
#to add a friend
def add_friend():

    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'chats': []
    }

#the user will be asked to give the details of their desired friend
    new_friend['name'] = raw_input('Please add your friend\'s name: ')
    new_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")

    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = raw_input('Age?')
    new_friend['age'] = int(new_friend['age'])

    new_friend['rating'] = raw_input('Spy rating?')
    new_friend['rating'] = float(new_friend['rating'])


#if the user does enter a valid string as the name and the age is valid as set greater than 12 , the syatem will accept the entry
#else the user will be promted to enter a valid name or valid age

    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['rating']:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add a spy with the given details '

    return len(friends)


#if the user selects the third option to send a message
#he will be asked to select a friend that has been imported from the dictionary in spydetails

def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number +1, friend['name'],
                                                   friend['age'],
                                                   friend['rating'])
        item_number = item_number + 1

    friend_choice = raw_input('Choose from your friends')

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


#here the user has decided to send a message to a user
def send_message():

#the user has to select a friend to whom he wants to send to message
# it may be from the list that has been imported or from a new friend added by the user

    friend_choice = select_a_friend()


#here we will ask the user for the image name
    original_image = raw_input('What is the name of the image?')
    output_path = 'output.jpg'

#the user will be asked to enter the text he wants to hide in the image
    text = raw_input('What do you want to say? ')
    Steganography.encode(original_image, output_path, text)

    new_chat = {
        'message': text,
        'time': datetime.now(),
        'sent_by_me': True
    }

    friends[friend_choice]['chats'].append(new_chat)

    print 'Your secret message image is ready!'

#the user can read the message t
def read_message():

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = {
        'message': secret_text,
        'time': datetime.now(),
        'sent_by_me': False
    }

    friends[sender]['chats'].append(new_chat)

    print 'Your message has been saved!'

#the user can read the chat history from here
def read_chat_history():

    read_for = select_a_friend()

    print '\n6'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)



def start_chat(spy_name, spy_age, spy_rating):


    current_status_message = None


    spy_name = spy['salutation'] + " " + spy['spy_name']


    if spy_age > 12 and spy_age < 50:


        print 'Authentication complete. Welcome ' + spy['spy_name'] + ' age: ' + str(spy['spy_age']) + ' and rating of: ' + str(spy['spy_rating']) + ' Good to have you back !'

        show_menu = True

        while show_menu:
            menu_choices = 'What would you like to do ? \n 1. Add a status update \n 2. Add a new friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n'
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    current_status_message = add_status(current_status_message)
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'

if existing == 'Y':
    start_chat(spy['spy_name'], spy['spy_age'], spy['spy_rating'])

#here the user has selected to add a new spy
else:

    spy = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': False
    }

    spy['name'] = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
    spy['salutation'] = raw_input("Should I call you Mr. or Ms.?: ")

    spy['age'] = raw_input("What is your age?")
    spy['age'] = int(spy['age'])

    spy['rating'] = raw_input("What is your spy rating?")
    spy['rating'] = float(spy['rating'])

    spy_is_online = True

    start_chat(spy['name'], spy['age'], spy['rating'])

else:
        print'please add a valid spy name'