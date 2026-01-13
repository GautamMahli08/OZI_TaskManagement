from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from typing import List
from app.core.config import settings
from jinja2 import Template

# Email configuration
conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
    MAIL_STARTTLS=settings.MAIL_STARTTLS,
    MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

# HTML email template
VERIFICATION_EMAIL_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        .container {
            background-color: #f9f9f9;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .header {
            text-align: center;
            color: #4F46E5;
            margin-bottom: 30px;
        }
        .button {
            display: inline-block;
            padding: 12px 30px;
            background-color: #4F46E5;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            margin: 20px 0;
            font-weight: bold;
        }
        .button:hover {
            background-color: #4338CA;
        }
        .footer {
            text-align: center;
            font-size: 12px;
            color: #666;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
        }
        .warning {
            background-color: #FEF3C7;
            border-left: 4px solid #F59E0B;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="header">🎯 Task Management System</h1>
        <h2>Welcome, {{ username }}!</h2>
        <p>Thank you for registering with Task Management System. To complete your registration, please verify your email address.</p>

        <div style="text-align: center;">
            <a href="{{ verification_url }}" class="button">Verify Email Address</a>
        </div>

        <p>Or copy and paste this link into your browser:</p>
        <p style="word-break: break-all; background-color: #E5E7EB; padding: 10px; border-radius: 5px;">
            {{ verification_url }}
        </p>

        <div class="warning">
            <strong>⚠️ Important:</strong> This verification link will expire in 15 minutes.
        </div>

        <p>If you didn't create an account, please ignore this email.</p>

        <div class="footer">
            <p>&copy; 2026 Task Management System. All rights reserved.</p>
            <p>This is an automated message, please do not reply.</p>
        </div>
    </div>
</body>
</html>
"""

async def send_verification_email(email: List[str], username: str, token: str):
    """Send email verification link to user."""
    verification_url = f"{settings.FRONTEND_URL}/verify-email?token={token}"

    # Render template
    template = Template(VERIFICATION_EMAIL_TEMPLATE)
    html_content = template.render(
        username=username,
        verification_url=verification_url
    )

    message = MessageSchema(
        subject="Verify Your Email - Task Management System",
        recipients=email,
        body=html_content,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    await fm.send_message(message)