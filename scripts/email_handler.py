import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import configparser

def send_email(to_email, name, book_title):
    """Send a personalized email."""
    config = configparser.ConfigParser()
    config.read('../config/config.ini')

    smtp_server = config['EMAIL']['SMTP_SERVER']
    smtp_port = int(config['EMAIL']['SMTP_PORT'])
    email_user = config['EMAIL']['EMAIL_USER']
    email_password = config['EMAIL']['EMAIL_PASSWORD']
    from_email = config['EMAIL']['FROM_EMAIL']

    subject = "Subscribe to Bookstore Updates"

    # Load email template
    with open('../templates/email_template.html', 'r') as file:
        template = file.read()

    # Personalize template
    html_content = template.replace('{{ name }}', name).replace('{{ book_title }}', book_title)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.attach(MIMEText(html_content, 'html'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_user, email_password)
            server.send_message(msg)
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")
