#coding:utf-8
import time
from pynput import keyboard
import utils_P.session_manager as sm
import utils_C.interfaceCPY as inCPY


class Chronometre(sm.sessionManager):

    def __init__(self, filePath, interfacePath):
        super().__init__()
        self.timestart = 0
        self.state = 0
        self.filePath = filePath
        self.interfacePath = interfacePath

    def launch(self):
        """
        enregistre le temps de départ dans une variable
        """
        self.timestart = time.time()
        print("timer start")
    
    def stop(self) -> float|int:
        """
        calcule le temps de résolution en faisant t1-t2 et le sauvegarde dans une liste. 
        """
        print("time stop")
        the_time = round(time.time() - self.timestart, 3)
        print("votre temps : " + str(the_time))  
        print(inCPY.scramble(self.filePath, self.interfacePath))
        self.currentSessionFile["times"].append(the_time)
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
    
    def sessionManagerDeb(self) -> str:
        currentSessionName = super().sessionManagerDeb()
        self.currentSessionName = currentSessionName
        self.currentSessionFile: dict[list|int] = self.get_json_file_content("./sessions/{}.json".format(self.currentSessionName))

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
