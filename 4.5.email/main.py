# Imports functions from emails module
from emails import email_sender, email_recipient, email_subject, email_body

# Email file name
file_name = '4.5.email/email.txt'

# Prints email information
print('Sender:', email_sender(file_name))
print('Recipient:', email_recipient(file_name))
print('Subject:', email_subject(file_name))
print('Body:')
print(email_body(file_name))