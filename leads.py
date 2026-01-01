import smtplib
from email.mime.text import MIMEText

def send_instant_welcome(user_email, user_name):
    """Sends a professional BNI welcome email automatically"""
    msg = MIMEText(f"Hello {user_name},\n\nThank you for reaching out! Your interest in BNI is the first step toward growing your business through referrals. A Chapter Director will contact you shortly.\n\nGivers Gain,\nThe BNI Agent")
    msg['Subject'] = 'Welcome to BNI - Your Inquiry Received'
    msg['From'] = 'tech.maxener@gmail.com'
    msg['To'] = user_email

    # Note: To use Gmail, you'll need an 'App Password' from Google Security settings
    print(f"📧 [SIMULATED] Welcome email sent to {user_email}")