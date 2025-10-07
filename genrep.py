#Author: Juha Pekkala
#Date: 2025-10-07

serie_resistans = 0
parallell_resistans = 0

resistor = input('Ange resistorer> ')

if resistor == '':
    print(f'Serieresistans: {serie_resistans}')
    print(f'Parallellresistans: {parallell_resistans}')

else:
    for resistor in resistor.split():
        serie_resistans += int(resistor)
        parallell_resistans += pow(int(resistor),-1)

    parallell_resistans = pow(parallell_resistans, -1)
    print(f'Serieresistans: {serie_resistans}')
    print(f'Parallellresistans: {parallell_resistans}')