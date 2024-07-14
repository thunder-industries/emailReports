import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # e.g., smtp.gmail.com
SMTP_PORT = 587  # For TLS
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'

# Function to send the email
def send_email():
    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'recipient@example.com'
    msg['Subject'] = 'Daily Report'

    # Create the body of the email
    body = 'This is your daily report.'
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # Send the email
        server.sendmail(EMAIL_ADDRESS, 'recipient@example.com', msg.as_string())
        server.quit()

        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Schedule the email to be sent daily
schedule.every().day.at("08:00").do(send_email)  # Set the time as per your requirement

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)