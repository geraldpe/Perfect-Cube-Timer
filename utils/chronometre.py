#coding:utf-8
import time
from pynput import keyboard
import utils.session_manager as sm


class Chronometre(sm.sessionManager):

    def __init__(self):
        super().__init__()
        self.timestart = 0
        self.state = 0
        currentSession = self.sessionManagerDeb()
        self.currentSession = currentSession

    def launch(self):
        self.timestart = time.time()
        print("timer start")
    
    def stop(self) -> float|int:
        print("time stop")
        the_time = round(time.time() - self.timestart, 3)
        print("votre temps : " + str(the_time))  
        self.save_time_in_session(self.currentSession, the_time)
        return the_time
        
    def space_bar_pressed(self, key):
        if key == keyboard.Key.space:
            if self.state == 2:
                self.stop()
                self.state = 0
            elif self.state == 0:
                self.state = 1
    
    def space_bar_released(self, key) -> None|bool:
        if key == keyboard.Key.space:
            if self.state == 1:
                self.launch()
                self.state = 2
        elif key == keyboard.Key.esc:
            print("fin du chrono")
            return False

    def listen(self):
        with keyboard.Listener(
                on_press=self.space_bar_pressed,
                on_release=self.space_bar_released) as listener:
            listener.join()    


def main():
    chrono = Chronometre()
    chrono.listen() 


if __name__ == "__main__":
    main()
