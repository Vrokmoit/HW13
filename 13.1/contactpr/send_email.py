from fastapi_mail import FastMail, MessageSchema, MessageType
from pydantic import EmailStr
from background_tasks import background_tasks
from config import conf
from auth import create_email_token



async def send_email(email: EmailStr, username: str, host: str):
    try:
        token_verification = create_email_token({"sub": email})
        message = MessageSchema(
            subject="Confirm your email",
            recipients=[email],
            template_body={"host": host, "username": username, "token": token_verification},
            subtype=MessageType.html
        )

        fm = FastMail(conf)
        await fm.send_message(message, template_name="email_template.html")
        print("Email sent successfully.")
    except Exception as err:
        print(f"Error sending email: {err}")