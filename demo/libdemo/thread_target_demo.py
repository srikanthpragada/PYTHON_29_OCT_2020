from threading import Thread


def squares(s, e):
    for i in range(s, e):
        print(i * i)


t = Thread(target=squares, args=(10, 15))
t.start()
print('Main Ends Here!')
