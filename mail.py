from fastapi import APIRouter, HTTPException
from email.mime.text import MIMEText
import smtplib

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
        my_email = 'mail@hotmail.com'
        server.login(my_email, 'email pass')
        message = MIMEText(email.body)
        message['From'] = my_email
        message['To'] = email.recipient
        message['Subject'] = "OTP"
        server.sendmail(my_email, email.recipient, message.as_string())
        server.quit()
        return {"message": "Email sent successfully."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)