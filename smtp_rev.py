import imaplib
import getpass

M= imaplib.IMAP4_SSL('imap.gmail.com')
email = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")
M.login(email, password)