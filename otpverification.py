import os
import math
import random
import smtplib

digits = "0123456789"
OTP = ""
for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]

otp = OTP + " is your OTP"
msg = otp

# Email details - Replace with your actual Gmail address and App Password
sender_email = "afifkhosyidzaki@gmail.com"  # Use your Gmail address
app_password = "ehe"  # Use the App Password you generated
receiver_email = input("Enter your email: ")  # Email address to send the OTP to

try:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()  # Start TLS encryption
    s.login(sender_email, app_password)  # Login to your Gmail account
    s.sendmail(sender_email, receiver_email, msg)  # Send the email
    print("OTP sent successfully!")

    a = input("Enter Your OTP >>: ")  # Prompt user to enter the OTP

    if a == OTP:
        print("Verified")
    else:
        print("Please Check your OTP again")

except smtplib.SMTPAuthenticationError as e:
    print(f"Authentication error: {e}")
    print("Please check your Gmail address and App Password.")
    print("Make sure 'Less secure app access' is enabled or use an App Password.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 's' in locals():
        s.quit()  # Close the connection
