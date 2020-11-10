ms = "How do you do"
ss = "o"

pos = -1
while True:
    pos = ms.find(ss, pos + 1)
    if pos == -1:
        break
    print(pos)
