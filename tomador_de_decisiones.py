from random import choice

# cosas que hay que hacer

estudiar = [['mates', 'logic', 'algoritsm'],
      ['lua', 'logic', 'gay'], 
      ['python', 'simple', 'chill']]

# input mood
print('waht mood are you in?')
mood = input()

for item in estudiar:
    if item[1] == mood:
        print(mood + 'estudiar: ' + item[0])
