import os

from twilio.rest import Client

account_sid = ""
auth_token = ""

client = Client(account_sid,auth_token)

client.messages.create(

	to ="" ,
	from_ = "",
	body="Ground control to Major Tom"
	)
