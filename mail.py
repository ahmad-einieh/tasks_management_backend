from fastapi import APIRouter, HTTPException
from email.mime.text import MIMEText
import smtplib
import os

from pydantic import BaseModel

mailRouter = APIRouter()

class EmailSchema(BaseModel):
    recipient: str
    body: str

@mailRouter.post("/send_email",tags=["mails"])
def send_email(email: EmailSchema):
    try:
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        my_email = os.environ['SMTP_USERNAME']
        server.login(my_email, os.environ['SMTP_PASSWORD'])
        message = MIMEText(email.body)
        message['From'] = my_email
        message['To'] = email.recipient
        message['Subject'] = "OTP"
        server.sendmail(my_email, email.recipient, message.as_string())
        server.quit()
        return {"message": "Email sent successfully."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
