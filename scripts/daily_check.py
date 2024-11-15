import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import configparser

# Configuration
config = configparser.ConfigParser()
config.read('../config/config.ini')

SMTP_SERVER = config['EMAIL']['SMTP_SERVER']
SMTP_PORT = int(config['EMAIL']['SMTP_PORT'])
EMAIL_USER = config['EMAIL']['EMAIL_USER']
EMAIL_PASSWORD = config['EMAIL']['EMAIL_PASSWORD']
FROM_EMAIL = config['EMAIL']['FROM_EMAIL']


def send_consent_email(to_email, name, book_title):
    subject = "We Value Your Privacy and Preferences"
    
    # loading template
    with open('../templates/email_template.html', 'r') as file:
        html_template = file.read()
    
    # personalization
    html_content = html_template.replace('{{ name }}', name)
    html_content = html_template.replace('{{ book_title }}', book_title)
    html_content = html_template.replace('{{ email }}', to_email)
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email
    msg.attach(MIMEText(html_content, 'html'))
    
    # Send the email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # secure connection
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")
