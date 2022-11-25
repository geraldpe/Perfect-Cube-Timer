#coding:utf-8
import utils.chronometre as ch
import utils.session_manager as sm
    

def main():
    chrono = ch.Chronometre()
    chrono.listen()
    

if __name__ == "__main__":
    main()