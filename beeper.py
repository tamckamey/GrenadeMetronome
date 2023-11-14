import winsound
import time
from threading import Thread

class Beeper(Thread):
    def __init__(self, interval):
        Thread.__init__(self)
        self.running = False
        self.interval = interval
        self.loudBeep = False
        self.iteration = 0

    def run(self):
        self.running = True
        while self.running:
            self.iteration += 1
            print(self.interval, self.iteration)
            if (self.iteration >= self.interval):
                self.loudBeep = True
                self.iteration = 0
                winsound.Beep(600, 400)
                time.sleep(0.6)
            else:
                winsound.Beep(500, 400)
                time.sleep(0.6)

    def stop(self):
        self.running = False



        

    

