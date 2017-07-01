import os

from twilio.rest import Client

account_sid = "AC296b29fe20967a9d0b5c799b9cc55a47"
auth_token = "c315683ba3d453c8907c09a4be1a9bc9"

client = Client(account_sid,auth_token)

client.messages.create(

	to ="+919930087431" ,
	from_ = "+12513330911",
	body="Ground control to Major Tom"
	)