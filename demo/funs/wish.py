def wish(*names, message='Hi'):
    for n in names:
       print(message, n)


wish('Scott', 'Joe', 'Larry', message='Greetings')
wish('Tim', 'Steve')
