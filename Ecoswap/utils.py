import requests
from requests.auth import HTTPBasicAuth

def send_sms(to_number, message):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    from_number = '+YourTwilioNumber'

    url = f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json'
    data = {
        'To': to_number,
        'From': from_number,
        'Body': message
    }

    response = requests.post(url, data=data, auth=HTTPBasicAuth(account_sid, auth_token))
    
    # Optional: log or raise error if it fails
    if response.status_code != 201:
        print("Failed to send SMS:", response.text)
    
    return response.status_code