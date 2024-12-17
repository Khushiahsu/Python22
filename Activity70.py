#Write a program to return the country code for various countries. Here’s a dictionary of different country codes - {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}.
cou = {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}
print('Country code of India is:')
print(cou.get('India','Not Found'))
print('Country code of Australia is:')
print(cou.get('Australia','Error'))
print('Country code of Nepal is:')
print(cou.get('Nepal','Not Found'))
