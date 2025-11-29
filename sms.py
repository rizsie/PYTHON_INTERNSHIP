from twilio.rest import Client
ACCOUNT_SID = "ACae8acb4c8cf1576ceec2c7ce1e5be4fc"
AUTH_TOKEN = "b89a3bff61fdd302c6436310258cab68"
TWILIO_NUMBER = "+1307xxxxx"
RECIEVER_NUMBER = "+91 745xxxxx"
Client = Client(ACCOUNT_SID, AUTH_TOKEN)
message =Client.messages.create(body = "hello", from_ = TWILIO_NUMBER, to = RECIEVER_NUMBER )