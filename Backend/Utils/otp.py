import ssl
import smtplib
from email.message import EmailMessage
import random
import string

email_sender = "otptest1991@gmail.com"
email_password = "vufx crkj tehf shpb"

def generate_otp():
    return "".join(random.choices(string.digits, k=6))

def send_otp_email(email_receiver, otp):
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = "Your OTP Code"
    em.set_content("Your OTP is " + otp)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls(context=context)
            smtp.login(email_sender, email_password)
            smtp.send_message(em)
            
        print("Email sent successfully")
        return True
    except Exception as e:
        print("Error:", e)
        return False