from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List

conf = ConnectionConfig(
    MAIL_USERNAME = "srpradhan131@gmail.com",
    MAIL_PASSWORD = "gkzc kbxh xudm wohr",
    MAIL_FROM = "srpradhan131@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME="SR Pradhan",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)


async def send_emails(emails: List[str]):
    html = """<p>Hi, Thanks for Registration !!!</p> """

    message = MessageSchema(
        subject="Registration Confirmation",
        recipients=emails,
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return {"msg":"emai; has beed sent"}