'''
- login and get token
- process 2FA if 2FA is setup for this account
- if the user is a regular customer then get a list of transactions for this user
- if the user is a partner_admin then get a list of transactions for the first user from the list of users this partner admin has access to
'''

import requests
import json

get_token_url = "https://api.canopy.cloud:443/api/v1/sessions/"		
validate_otp_url = "https://api.canopy.cloud:443/api/v1/sessions/otp/validate.json" #calling the production server for OTP authentication
get_transactions_url = "https://api.canopy.cloud:443/api/v1/transactions.json"
get_partner_users_url = "https://api.canopy.cloud:443/api/v1/admin/users.json"



#please replace below with your username and password over here
username = 'username'
password = 'passwordxxx'

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

login_role = response.json()['role']
switch_user_id = response.json()['id']

if login_role == 'Partneradmin':

    #print "============== partner's users ==========="
    headers = {
        'authorization': token,
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8"
        }

    partner_users = []

    response = requests.request("GET", get_partner_users_url, headers=headers)
    for parent_user in response.json()['users']:
        partner_users.append(parent_user['id'])

    #print partner_users
    #take the first users in the list as the switch_user_id
    switch_user_id = partner_users[0]

#	print json.dumps(response.json(), indent=4, sort_keys = True)



#in case the user is a partner_admin then switch_user_id is any one of the users it has access to (here we take the first one from the list)
#in case the user is a regular customer then the switch_user_id = user_id for this customer


#now get the transactions data
transaction_page = 1
transactions_per_page = 10000

transaction_header = {
        'Authorization': 'Token token="' + token + '", username="' + username + '"',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-App-Switch-User': str(switch_user_id),
    }


transaction_endpoint = get_transactions_url + '?page=' + str(transaction_page) + '&per_page=' + str(transactions_per_page) + '&for_current_user=true&output_format=json&all_pages=true'

transactions = requests.get(transaction_endpoint, headers=transaction_header)

print json.dumps(transactions.json(), indent=4, sort_keys = False)
