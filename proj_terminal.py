import smtplib 
from email.MIMEBase import MIMEBase
from email import encoders
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from twilio import TwilioRestException
from twilio.rest import TwilioRestClient
import getpass
import fbchat
import sys
import tweepy
print """...........
          Welcome 
         ..........."""
print " Enter ur Email id details"
your_adr= raw_input("ur email id")
pass_adr= getpass.getpass()

print 'enter ur fb details'
your_id =str(raw_input("enter username"))
pass_fb=getpass.getpass()

print "Enter SMS details"

ACCOUNT_SID =raw_input("acc SID")
AUTH_TOKEN= raw_input("acc Token")
fromNumber=str(raw_input("enter ur no"))


print "Enter Twitter details"
Access_token=raw_input("enter access token")
Access_token_secret=getpass.getpass('Access_token_secret :')
Consumer_key=raw_input("enter consumer_key")
Consumer_secret=getpass.getpass('Consumer_secret :')

exit_input= raw_input("""to exit type EXIT,else press any key""")

while(exit_input != "EXIT"):
	print " email-1 fb-2 sms-3 twitter-4"
	number=int(raw_input("selection"))
	if(number==1):
		rec_adr=raw_input("receiver's email")
		msg=MIMEMultipart()
		subj=raw_input("subject:")
		msg['From']=your_adr
		msg['To']=rec_adr
		msg['Subject']=subj

	        print "text msg"
		body=sys.stdin.read()
		
		msg.attach(MIMEText(body,'plain'))

		inp=raw_input("Do u want to attach file?Y/N")
		if(inp=='Y'):
		 strings= raw_input("enter file address")  
   
		 if(strings !=''):
		   attachment=open(strings,"rb")
		   part= MIMEBase('application','octet-stream')
		   part.set_payload((attachment).read())
		   encoders.encode_base64(part)
		   part.add_header('Content-Disposition',"attachment;filename=%s"%strings)

		 msg.attach(part)

		server=smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()
		server.login(your_adr,pass_adr)
		text=msg.as_string()
		server.sendmail(your_adr,rec_adr,text)
		server.quit()

    #FB chat
	elif(number==2):
		client= fbchat.Client(your_id,pass_fb)
		fname=str(raw_input("enter friend's name"))
		friends=client.getUsers(fname)
		friend=friends[0]
		messagetosend=str(raw_input("Message to send"))
		sent=client.send(friend.uid,messagetosend)
		if sent:
			print("msg sent successfully")
		else:
			print("msg sending failed")
      #SMS
	elif(number==3):
		client= TwilioRestClient(ACCOUNT_SID,AUTH_TOKEN)

		ToNumber=str(raw_input("Enter receiver's no"))
		bodyText=str(raw_input("enter text"))
		try:
		 client.messages.create(
			to = '+91'+ToNumber,
			from_ ='+'+fromNumber,
			body = bodyText,
			)
		except TwilioRestException as e:
			#print e
                        if(e.code==21212):
			  fromNumber=raw_input("enter ur correct no")
			  
			elif(e.code==21608):
			  print "verify the no with twilio"
			elif(e.code==20003):
			  ACCOUNT_SID =raw_input("enter correct acc SID")
			  AUTH_TOKEN= raw_input("enter correct acc Token")
			else:
			  print "error please try again"
			  
			#print TwilioRestException.__dict__
	elif(number==4):
		auth = tweepy.OAuthHandler(Consumer_key,Consumer_secret)
  		auth.set_access_token(Access_token,Access_token_secret)
		print "Enter your tweet"
		tweet=sys.stdin.read()
		status=tweepy.API(auth).update_status(status=tweet)
	exit_input= raw_input("""to exit type EXIT,else press any key""")
		
			

		
		




