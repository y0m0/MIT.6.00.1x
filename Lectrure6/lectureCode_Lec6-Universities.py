## universities

Techs = ['MIT', 'Cal Tech']
Ivys = ['Harvard', 'Yale', 'Brown']

Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Cal Tech'], ['Harvard', 'Yale', 'Brown']]

Techs.append('RPI')

print('Univs = ')
print(Univs)
print('')
print('Univs1 =')
print(Univs1)


for e in Univs:
    print('Univs contains ')
    print(e)
    print('   which contains')
    for u in e:
        print('      ' + u)


