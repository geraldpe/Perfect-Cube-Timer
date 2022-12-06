#coding:utf-8
import utils_P.chronometre as ch
import utils_P.session_manager as sm
    

def main():
    chrono = ch.Chronometre()
    chrono.sessionManagerDeb()
    running = True
    while running:
        chrono.listen()
        chrono.save_time_in_session(chrono.currentSessionName, chrono.currentSessionFile["times"])
        chrono.sessionManagerDeb()
    

if __name__ == "__main__":
    main()