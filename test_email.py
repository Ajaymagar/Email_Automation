names = []
emails = []
links = []


import smtplib

fromaddres = 'magarajay538@gmail.com'
password = 'magarajay5381848'


with open('names.txt','r',encoding='utf-8') as nameFile:
	for name in nameFile:
		names.append(name)

with open('email.txt','r',encoding='utf-8') as emailfile:
    for email in emailfile:
        emails.append(email)

with open('link.txt' , 'r',encoding='utf-8') as LinkFile:
	for link in LinkFile:
		links.append(link)


for name , email , link in zip(names,emails,links):
	print(name , email , link)	







'''
for dest in emails:
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()   
    server.starttls()
    server.login(fromaddres,password)
    server.sendmail(fromaddres,dest,msg)
    server.quit()
'''

Aishwarya Bharati
Ankita Rajbhar
Anusha Deshpande
Dikshita Oswal
Jinisha Jain
Nitin Patil
Ruchi Rai
Sakshi Saini
Sathyan Thever
Sweta Bhattacharjee
Tanavi Joshi
Chetan Tawade
Krishnan
Divyesh Patil
Aniket Shirsekar
Arpit Pandey
Kunal Sonawane
Jowin J
Shreeraj Nikam
Vincent Dsouza

aishwaryabharati8976@gmail.com
ankitarajbhar2000@gmail.com
anusha.deshpande17@siesgst.ac.in
oswalddel16e@student.mes.ac.in
jinisha1611@gmail.com
nitin11121@gmail.com
rairucra18extc@student.mes.ac.in
sakshisaini3694@gmail.com
sathyanthever101@gmail.com
bhattacharjeeswech18ce@student.mes.ac.in
tanavijoshi@gmail.com
chetantawade1002@gmail.com
knkrishnano97@gmail.com
divyeshpatil1998@gmail.com
aniketshirsekar08@gmail.com
7884.stkabirdin@gmail.com
kunalsonawanezucc@gmail.com
jowinprabhu007@gmail.com
nikamshreeraj178@gmail.com
vinvan007vd@gmail.com 

