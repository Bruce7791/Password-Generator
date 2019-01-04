# Program that makes passwords
# Cryptography code from https://www.blog.pythonlibrary.org/2017/02/16/pythons-new-secrets-module/
# https://docs.python.org/3.6/library/secrets.html
# https://docs.python.org/3.4/library/string.html
# http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python/
# https://stackoverflow.com/questions/31715119/how-can-i-open-a-website-in-my-web-browser-using-python

import secrets
import string
import pyperclip
import webbrowser

while True:
    print("\nWelcome to Bruce's Python Password Generator")
    print("\nThis program generates a password for you, lets you pick the length of it, helps you test the strength of it, and store it")

    password_Length = int(input("\nPlease enter the length in numbers of what you want your password to be: ", )) 
    print()


    characters = string.ascii_letters + string.digits + "#$%&@"


    finished_password = ''.join(secrets.choice(characters) for i in range(password_Length))


    print("\nHere is your password", finished_password) 
    print("\nYour password has been written to the windows clipboard so you can paste it into that website and a text file for saving it.")
    print("\nTest your password's strength at https://howsecureismypassword.net which has opened in a browser right now.")

    pyperclip.copy(finished_password)
    spam = pyperclip.paste()

    webbrowser.open('https://howsecureismypassword.net', new = 2)

    while True:
        answer = input('\nRun again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':
        continue
    else:
        print('Goodbye')
        break