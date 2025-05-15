
chamada = {'ana': 8.5, 'pedro': 7.0, 'maria': 9.2}
 
print(chamada)

chamada['carlos'] = 6.5
print(chamada)

chamada['ana'] = 9.0
print(chamada)

del chamada['pedro']
print(chamada)

media = sum(chamada.values())/ len(chamada)
print('a media geral é: ', media)

print(chamada.get('maria', 'não se encontra.'))

