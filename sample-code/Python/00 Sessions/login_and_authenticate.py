'''
- login and get token
- process 2FA if 2FA is setup for this account
- login and get token for a user (whether a regular
  user or a parteradmin / superadmin).
- In case 2FA is not enabled it returns a JSON of the format:
{ "status": "ok", "id": 291, "timeouts": { "IDLE_TIMEOUT": 30, "TOTAL_TIMEOUT": 240 }
, "token": "ZSPiYDu5ezX66tGRLy8R", "email": "admin@mesitis.com",
"display_name": "canopy_demo", "base_currency": "USD", "username":
"canopy_demo", "registered_on": "03-06-2015", "role": "Customer", "is_new": false,
"login_flow": "logged_in" }
- in case 2FA is enabled you get a JSON of the format:
{ "status": "ok", "id": 291, "timeouts": { "IDLE_TIMEOUT": 5, "TOTAL_TIMEOUT": 5 }
, "token": "pscxZd4snAeSsFevUmDC", "display_name": "canopy_demo", "username":
"canopy_demo", "login_flow": "2fa_verification" }
'''

import requests
import json

get_token_url = "https://api.canopy.cloud:443/api/v1/sessions/"		
validate_otp_url = "https://api.canopy.cloud:443/api/v1/sessions/otp/validate.json" #calling the production server for OTP authentication
login_and_authenticate_url = "https://api.canopy.cloud:443/api/v1/sessions/"

#please replace below with your username and password over here
username = 'userxxx'
password = 'passxxx'

#please enter the OTP token in case it is enabled
otp_code = '123456'


#first call for a fresh token
payload = "user%5Busername%5D=" + username + "&user%5Bpassword%5D=" + password
headers = {
	'accept': "application/json",
	'content-type':"application/x-www-form-urlencoded"
	}

response = requests.request("POST", get_token_url, data=payload, headers=headers)

print json.dumps(response.json(), indent=4, sort_keys = True)

token = response.json()['token']
login_flow = response.json()['login_flow']

#in case 2FA is enabled use the OTP code to get the second level of authentication
if login_flow == '2fa_verification':
	headers['Authorization'] = token
	payload = 'otp_code=' + otp_code
	response = requests.request("POST", validate_otp_url, data=payload, headers=headers)
	print json.dumps(response.json(), indent=4, sort_keys = True) #print response.text
	token = response.json()['token']

url = "https://api.canopy.cloud:443/api/v1/sessions/"

payload = {"user[username]": username, "user[password]": password}
headers = {
    'accept': "application/json",
    'content-type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print json.dumps(response.json(), indent=4, sort_keys = True)
