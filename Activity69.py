#Write a program to check the frequency of a value in a dictionary - {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}.

cod = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
print('The original dictionary is',str(cod))
ini = 2 
res = 0
for key in cod:
    if cod[key]==ini:
        res = res+1
print('The frequency of',ini,'is:',str(res))