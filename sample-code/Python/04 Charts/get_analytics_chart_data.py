'''
- login and get token
- process 2FA if 2FA is setup for this account
- Gets data needed to plot a chart for a ticker (these are Canopy tickers e.g. IBM_US or HPQ_US)
'''

import requests
import json

get_token_url = "https://api.canopy.cloud:443/api/v1/sessions/"		
validate_otp_url = "https://api.canopy.cloud:443/api/v1/sessions/otp/validate.json" #calling the production server for OTP authentication
get_partner_users_url = "https://api.canopy.cloud:443/api/v1/admin/users.json"
get_analytics_chart_data_url = "https://api.canopy.cloud:443/api/v1/charts/analytics.json"

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

#Include user ids here to filter results
user_ids = ""

querystring = {"asset_class":"Equity","field":"market_cap","user_ids":user_ids}

headers = {
    'authorization': token,
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8"
    }

response = requests.request("GET", get_analytics_chart_data_url, headers=headers, params=querystring)

print json.dumps(response.json(), indent=4, sort_keys = True)
