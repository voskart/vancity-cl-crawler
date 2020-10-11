import yagmail
import config

def send_mail(msg):
	try:
		yag = yagmail.SMTP(user=config.mailuser,password=config.mailpass)
		content = "Neighborhood: %s\n Price: %s\n Link: %s\n Posted on: %s\n" % (msg['neighborhood'], msg['price'], msg['link'], msg['date']) 
		yag.send(to=config.to,subject='I found an apartment!', contents=content)
		print("Email sent successfully")
	except:
		print("Error, email was not sent")

