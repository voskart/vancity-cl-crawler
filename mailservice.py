import yagmail
import config

def send_mail(msg):
	try:
		yag = yagmail.SMTP(user=config.user,password=config.password)
		yag.send(to=config.to,subject='Testing Yagmail', contents=msg)
		print("Email sent successfully")
	except:
		print("Error, email was not sent")

