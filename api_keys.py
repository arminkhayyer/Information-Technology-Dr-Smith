from congress import Congress

api_key = 'Z7cnuQ3cufA08VfbWOoqURVpeSUuyT8QQazVwAGY'
congress = Congress(api_key)

# get member by bioguide ID
pelosi = congress.members.get('P000197')
print(pelosi['twitter_account'])
'NancyPelosi'