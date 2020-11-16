# Keyword only args
def wish(*, message, name):
    print(message, name)


# wish('Ben','Hello')
wish(name='Ben', message='Hello')
wish(message='Hello', name='Ben')
