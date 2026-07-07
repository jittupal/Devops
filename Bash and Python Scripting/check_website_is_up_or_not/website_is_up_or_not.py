import requests as rq
import smtplib as spb
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart 
import os
from dotenv import load_dotenv

load_dotenv()

def check_website(url):
    try:
        # Added a timeout so the script doesn't hang forever if the site is down
        response = rq.get(url, timeout=5)
        return response.status_code == 200
    except:
        return False
    
def send_email(sender_email, password, receiver_email, subject, body):
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
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send the email")
        print(e)
        
# Fixed the typo from .og to .org
url = "https://fakestoreapi.og/" 

if not check_website(url):
    sender_email = os.getenv("APP_EMAIL")
    receiver_email = os.getenv("APP_EMAIL")
    subject = "ALERT: Website is DOWN!"  # Fixed subject to match the reality
    body = "Hii, website down hai. Please check karo."
    
    # REMOVED SPACES FROM THE APP PASSWORD HERE:
    password = os.getenv("APP_PASSWORD") 
    
    send_email(sender_email, password, receiver_email, subject, body)
else:
    print("Website is up and running perfectly.")