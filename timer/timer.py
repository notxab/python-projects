import time
import os

class timer:

    def __init__(self, seconds = 0, minutes = 0, hours = 0):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def __repr__(self):
        return f'{self.hours:02d}h {self.minutes:02d}m {self.seconds:02d}s'

    def increment(self):
        self.seconds += 1
        if self.seconds >= 60:
            self.minutes += 1
            self.seconds = 0
        if self.minutes >= 60:
            self.hours += 1
            self.minutes = 0

    def start(self):
        while True:
            os.system('cls')
            print(self)
            self.increment()
            time.sleep(1)

timer1 = timer()
timer1.start()