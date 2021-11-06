favorite_car= {
    'JJ' : {'Golf','Camry','LFA'},
    'Nicholas' : {'Innova', 'Panther', 'Fortuner'},
    'Filbert' : {'CX5','Terra','ioniq'},
    'Michael' : {'Pajero','Alpard','CR-V'},
    'Garry' : {'Highlander','Pathfinder','Rogue'}
}

for k,v in favorite_car.items():
    print(k,"likes these cars :")
    for i in favorite_car.get(k):
        print("-",i)

#(ﾟДﾟ)AAAAAAAAAAAAAAAAAAAA