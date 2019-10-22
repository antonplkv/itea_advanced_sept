from threading import Thread
import time


# def random_time_sleep(time_to_sleep):
#     print("thread started")
#     time.sleep(time_to_sleep)
#     print("thread ended")
#
#
# t = Thread(target=random_time_sleep, args=(1, ), name="our thread")
# t.start()
#
#
# print("Main thread process ......")
#
# for _ in range(10):
#     print("works")
#     print(t.is_alive())
#     print(t.isAlive())
#     print(t.isDaemon())
#     print(t.getName())
#     time.sleep(0.5)
#     print("Iteration ended")


class MyThread(Thread):

    def __init__(self, name, is_daemon):
        super().__init__(name=name, daemon=is_daemon)

    def run(self):
        for i in range(5):
            print("i am class thread")
            time.sleep(0.2)


t = MyThread("name", False)
t.start()


