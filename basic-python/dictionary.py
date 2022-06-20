# value : key seklinde calisir

plakalar = {'Sakarya' : 54,
            'Istambul' : 34}

print(plakalar)     
print(plakalar['Sakarya'])

plakalar['Ankara'] = 6  ## deger ekleme

plakalar['Istambul'] = 'new Value'  ## deger guncellemesi

print(plakalar)  


users = {
    'Taha' : {
        'Age' : 18
        ,'Country' : 'Turkey'
    }
     
    ,'Jhony' : {
        'Age' : 22
        ,'Country' : 'England'

    }
}

print(users)

print(users['Taha'])
print(users['Taha']['Age'])