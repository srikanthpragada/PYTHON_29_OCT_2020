# Positional only args
def wish(name, message, /):
    print(message, name)


wish('Ben', 'Hello')
wish(name='Ben', message='Hello')
