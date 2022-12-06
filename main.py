#coding:utf-8
import utils.chronometre as ch
import utils.session_manager as sm
    

def main():
    chrono = ch.Chronometre()
    running = True
    while running:
        chrono.listen()
        chrono.save_time_in_session(chrono.currentSessionName, chrono.currentSessionFile["times"])
        print(chrono.currentSessionFile["times"])
    

if __name__ == "__main__":
    main()