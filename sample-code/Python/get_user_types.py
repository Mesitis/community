'''
- login and get token
- process 2FA if 2FA is setup for this account
- returns all user types if user is a partner admin (or above) - else error
'''
import requests
import json

get_token_url = "https://api.canopy.cloud:443/api/v1/sessions/"		
validate_otp_url = "https://api.canopy.cloud:443/api/v1/sessions/otp/validate.json" #calling the production server for OTP authentication
get_partner_users_url = "https://api.canopy.cloud:443/api/v1/admin/users.json"
get_user_types_url = "https://api.canopy.cloud:443/api/v1/admin/users/types.json"

#please replace below with your username and password over here
username = 'login_name'
password = 'xxxxxxxxx'

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

headers = {
    'authorization': token,
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8"
    }

response = requests.request("GET", get_user_types_url, headers=headers)

print json.dumps(response.json(), indent=4, sort_keys = True)
