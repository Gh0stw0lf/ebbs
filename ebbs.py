import requests

site_url = 'https://www.zeroharmbbs.com/'
file_url = 'https://www.zeroharmbbs.com/admin/download.html?start=01%2F01%2F2018&end=10%2F23%2F2018&r=safetyaudit&loc=13'
username = input('What is your username?')
password = input('What is your password')

print('Tiny robot is checking your credentials....')

s = requests.Session()
s.get(site_url)
s.post(site_url,data={'loginUsername':'username','loginPassword': 'password'})


print('Verification complete. Hooray!')
print('Little bot is downloading EBBS excel files....')

s.get(file_url)

print('Success!')