#Author: Juha Pekkala
#Date: 2025-10-07

serie_resistans = 0
parallell_resistans = 0

resistor = input('Ange resistorer> ')

if resistor == '':
    print(f'Serieresistans: {serie_resistans}')
    print(f'Parallellresistans: {parallell_resistans}')

else:
    for r in resistor.split():
        serie_resistans += int(r)
        parallell_resistans += int(r)**-1

    parallell_resistans = pow(parallell_resistans, -1)
    print(f'\nEi24 - genrep praktiskt prov')
    print(f'Serieresistans: {serie_resistans}')
    print(f'Parallellresistans: {parallell_resistans}')