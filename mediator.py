def getLogin():
    fetchUsername = os.environ.get('USER')
    fetchPassword = os.environ.get('PASS')
    credits = [fetchUsername,fetchPassword]
    return credits

'''
This is a method containing file that fetches username and password from
any windows based operating system using the os library.
A list containing username and password is returned.
Warning : do not use this to print in plaintext format as it may pose privacy concerns.
To set it up correctly, follow instructions given below --
1. Go to Environment variables in your Windows Control panel.
2. In Environment variables create a new variable called 'USER' with value that you would want to return.
3. Follow step 2 to add variable 'PASS' with corresponding password.
4. Save and apply changes.
5. Inside your driver file import os and import mediator (this python file) as library imports.
6. Call the function getLogin() and fetch its zero index element to get fetch username
and first index element to get password.
'''
