'''
- login and get token
- process 2FA if 2FA is setup for this account
- in case the login is authorized as a partner_admin then also list the users that partner_admin has access to
'''

import requests
import json

get_token_url = "https://api.canopy.cloud:443/api/v1/sessions/"		
validate_otp_url = "https://api.canopy.cloud:443/api/v1/sessions/otp/validate.json" #calling the production server for OTP authentication
get_partner_users_url = "https://api.canopy.cloud:443/api/v1/admin/users.json"
get_token_url = 'https://api.canopy.cloud:443/api/v1/sessions.json'
validate_otp_url = "https://api.canopy.cloud:443/api/v1/sessions/otp/validate.json" #calling the production server for OTP authentication



#please replace below with your username and password over here
username = 'userxxx'
password = 'passxxx'

#please enter the OTP token in case it is enabled
otp_code = '259060'


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
#	token = response.json()['token']

login_role = response.json()['role']

'''
you should get an ouput in the following format (in case a regular customer)
{
    "base_currency": "USD", 
    "days_to_password_expiry": 53, 
    "display_name": "canopy_demo", 
    "email": "admin@mesitis.com", 
    "id": 291, 
    "is_new": false, 
    "login_flow": "logged_in", 
    "registered_on": "03-06-2015", 
    "role": "Customer", 
    "status": "ok", 
    "timeouts": {
        "IDLE_TIMEOUT": 30, 
        "TOTAL_TIMEOUT": 240
    }, 
    "token": "816VvjP_3vdj85AHyasL", 
    "username": "canopy_demo"
}

and in case of a partner_admin
{
    "base_currency": "USD", 
    "days_to_password_expiry": 53, 
    "display_name": "demo_rm", 
    "email": "abcd@1234.com", 
    "id": 1674, 
    "is_new": false, 
    "login_flow": "logged_in", 
    "registered_on": "24-08-2016", 
    "role": "Partneradmin", 
    "status": "ok", 
    "timeouts": {
        "IDLE_TIMEOUT": 30, 
        "TOTAL_TIMEOUT": 240
    }, 
    "token": "D9qoCakjxm1bNw8zFUyu", 
    "username": "demo_rm"
}

'''


if login_role == 'Partneradmin':

	print "============== partner's users ==========="
	headers = {
	    'authorization': token,
	    'content-type': "application/x-www-form-urlencoded; charset=UTF-8"
	    }

	partner_users = []

	response = requests.request("GET", get_partner_users_url, headers=headers)

	print json.dumps(response.json(), indent=4, sort_keys = True)


