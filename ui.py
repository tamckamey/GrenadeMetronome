import beeper
import PySimpleGUI as gui
from threading import Thread

layout = [
    [gui.Text("Grenade Fuse Duration")],
    [gui.Input("5", enable_events =True, key="Timer", justification="left")],
    [
        gui.Button("Stop", button_color="#FF0000"),
        gui.Button("Play", button_color="#009900"),
        gui.Push(),
        gui.Button("Update Timer"),
        gui.Button("Exit")
    ]
]

window = gui.Window("Grenade Sound", layout, icon="assets/grenade.ico")


class MainUI(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
        self.window = window
        self.interval = 5
        self.beeper = beeper.Beeper(self.interval)

    def run(self):
        self.running = True
        while self.running:
            self.handleWindow()

    def stop(self):
        self.running = False
                
    def handleWindow(self):
        event, values = window.read()
        print(event)
        if event == "Timer":
            try:
                self.interval = int(values["Timer"])
            except ValueError:
                self.interval = 5 # Default to 5 if int cast fails
        elif event == "Update Timer":
            self.beeper.interval = self.interval

        elif event == "Play":
            self.beeper.stop()
            self.beeper = beeper.Beeper(self.interval)
            self.beeper.start()
        elif event == "Stop":
            if hasattr(self, 'beeper'):
                self.beeper.stop()
        elif event == "Exit" or event == gui.WIN_CLOSED:
            self.beeper.stop()
            self.stop()
            window.close()