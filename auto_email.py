
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage 


My_ADDRESS = 'email'
PASSWORD = 'password'



names = []
emails = []
#links = []


with open('names.txt','r',encoding='utf-8') as namefile:
    for name in namefile:
        names.append(name)
print(names[0])

with open('email.txt','r',encoding='utf-8') as emailfile:
    for email in emailfile:
        emails.append(email)
print(emails[0])


'''
with open('link.txt','r',encoding='utf-8') as linkFile:
	for link in linkFile:
		links.append(link)
print(links[0])
'''


def read_Template(textfile):
    with open(textfile,'r',encoding='utf-8') as text:
        content = text.read()

    return Template(content)

def main():
    #names , emails = get_contact('names.txt','email.txt')
    message_content = read_Template('content.html')
 

    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(My_ADDRESS,PASSWORD)

    for name,email in zip(names,emails):
        msg = MIMEMultipart()

        message = message_content.substitute(PERSON_NAME=name.title())
        #link_urls = message_content.substitute(LINK=link)

        print(msg)

        msg['From'] = My_ADDRESS
        msg['TO'] = email
        msg['subject'] = "Invitation for ETSA Farewell"

        msg.attach(MIMEText(message,'html'))
        #msg.attach(MIMEText(link_urls,'plain'))
        
        #msg.attach(MIMEImage(file("etsa.png").read()))

        server.send_message(msg)
        del msg

    server.quit()

if __name__ == '__main__':
    main()



