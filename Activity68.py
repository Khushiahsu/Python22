#First, create a dictionary that consists of - id, name, class and subject integration of students. Then, write a program to retrieve unique entries and eliminate the rest.

nam = {'id1':{'name':['Aarav'], 'class':['V'],'sub_int':['english','math']},
        'id2':{'name':['John'], 'class':['V'],'sub_int2':['science','art']},
        'id3':{'name':['Aarav'], 'class':['V'],'sub_int3':['english','math']},
        'id4':{'name':['Dora'], 'class':['V'],'sub_int4':['physics','coding']}}

res = {}

for key,value in nam.items():
    if value not in res.values():
        res[key]=value
print(res)