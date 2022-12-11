#coding:utf-8
import utils_P.chronometre as ch
import utils_P.session_manager as sm
import utils_C.interfaceCPY as inCPY
    

def main():
    filePath, interfacePath = inCPY.get_file_paths()
    chrono = ch.Chronometre(filePath, interfacePath)
    chrono.sessionManagerDeb()
    running = True

    while running:
        print(inCPY.scramble(filePath, interfacePath))
        chrono.listen()
        chrono.save_time_in_session(chrono.currentSessionName, chrono.currentSessionFile["times"])
        chrono.sessionManagerDeb()
    

if __name__ == "__main__":
    main()