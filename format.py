print('{0},{1},{2}'.format('apple','banana','carrot','pen'))
print('{},{},{}'.format('apple','banana','carrot'))
print('{2},{1},{0}'.format('apple','banana','carrot'))
print('{2},{1},{1},{0}'.format('apple','banana','carrot'))
print('{2},{1},{0}'.format(*'abcd'))
print('{0},{1},{0}'.format('apple','banana','carrot'))
print('coordinates:{latitude},{longitude}'.format(
    latitude='37.24N',longitude='-115.81W'))
print('Welcome:{name},your college is:{college}'.format( name='Harsh',college='VIPS'))
