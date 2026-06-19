import requests as rq
import smtplib as spb
from email.mime.text import MIMEText  # used for sending plain text emails
from email.mime.multipart import MIMEMultipart #form sending attachments

def check_website(url):
    try:
        response = rq.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False
    

def send_email(sender_email, password,  receiver_email, subject, body):
    message = MIMEMultipart()
    message["from"] = sender_email
    message["to"] = receiver_email
    message["subject"] = subject
    message.attach(MIMEText(body, "plain"))
    
    try:
        server = spb.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("email sent")
    except Exception as e:
        print("Failed to sent the email")
        print(e)
        
url = "https://fakestoreapi.og/"

if not check_website(url):
    sender_email = "xxxxxxx"
    subject = "Website is up"
    body = "hii, website check karo"
    receiver_email = "xxxxx"
    password = "xxxx"
    send_email(sender_email, password, receiver_email, subject, body)
else:
    print("Website is up")
    

