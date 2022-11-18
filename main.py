#coding:utf-8
import chronometre as ch
import session_manager as sm


def session_creator():
    name = str(input("nom de la nouvelle session >> "))
    sm.create_session(name)
    return name

def create_existing_sessions_list():
    session_list = []
    with open("memory.txt", 'r', encoding='utf-8') as file:
        session_list = file.read().splitlines
    return session_list

def sessionManagerDeb():
    currentSession = None
    while currentSession is None:
        print("voulez vous créer une nouvelle session ou entrer dans une déjà existente ? ")
        print("")
        print("   déjà existante : 1")
        print("   créer une session : 2")
        answer = str(input(' >> '))
        if answer == "2":
            sessionName = session_creator()
            answer = str(input("voulez vous utiliser cette session ? (y/n) >> "))
            if answer == "y":
                currentSession = sessionName
        elif answer == "1":
            session_list = create_existing_sessions_list()
            print("")
            for elem in session_list:
                print(elem)
            print("")
            answer = None
            while answer not in session_list:
                answer = str(input("entrez le nom de la session dans laquelle vous voulez entrer >> "))
            currentSession = answer
    return currentSession
    

def main():
    currentSession = sessionManagerDeb()
    chrono = ch.Chronometre(currentSession=currentSession)
    chrono.listen()
    
    
        
    
            


if __name__ == "__main__":
    main()