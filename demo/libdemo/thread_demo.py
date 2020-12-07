import threading


class PrintThread(threading.Thread):
    def run(self):  # invoked by start()
        for i in range(1, 10):
            print(i * i)


t = PrintThread()
t.start()
print(threading.main_thread(), threading.active_count())
print('Main Ends Here!')