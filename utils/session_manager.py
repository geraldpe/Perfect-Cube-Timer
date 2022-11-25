
import json


class sessionManager:

    def __init__(self):
        pass

    def get_json_file_content(self, path: str) -> dict[list[float|int]&int]:
        """
        renvoie le contenu d'un fichier json sous la forme d'un dictionnaire (prend le chemin de fichier en entrée)
        """
        with open("{}".format(path), "r", encoding="utf-8") as jsfile:
            result = json.load(jsfile)
        return result

    def save_time_in_session(self, sessionName: str, time: float|int) -> None:
        """
        sauvegarde un temps dans une session à la fin de la liste
        """
        session_file = {}
        if time is not None:
            session_file = self.get_json_file_content("sessions/{}.json".format(sessionName))
            session_file["times"].append(time)
            session_file["times_in_session"] += 1
        with open("./sessions/{}.json".format(sessionName), "w", encoding="utf-8") as jsfile:
            json.dump(session_file, jsfile, indent=2)
    
    def change_Number_of_times(self, sessionName: str, nmbtimes: int, session: dict[list[float|int]&int]):
        """
        change le nombre de temps effectués lors de la session
        """
        session["times_in_session"] = nmbtimes
        with open("./sessions/{}.json".format(sessionName), "w", encoding="utf-8") as jsfile:
            json.dump(session, jsfile, indent=2)

    def delete_last_time_in_session(self, sessionName: str) -> None:
        """
        supprime le dernier temps de la session
        """
        session_file = {}
        session_file = self.get_json_file_content("sessions/{}.json".format(sessionName))
        session_file["times"]: list .pop(len(session_file["times"])-1)
        session_file["times_in_session"] -= 1
        with open("./sessions/{}.json".format(sessionName), "w", encoding="utf-8") as jsfile:
            json.dump(session_file, jsfile, indent=2)

    def create_session(self, sessionName: str) -> None:
        """
        crée une nouvelle session (nouveau fichier json)
        """
        with open("./sessions/{}.json".format(sessionName), "w") as file:
            json.dump({"times_in_session": 0, "times": []}, file)
        session_list = []
        with open("./sessions/memory.txt", "r", encoding="utf-8") as file:
            session_list = file.read().splitlines()
        session_list.append(sessionName)
        with open("./sessions/memory.txt", 'w', encoding='utf-8') as file:
            for elem in session_list:
                file.write(elem + "\n")
    
    def checkAndCorrectNumberOfTimes(self, session: str) -> str:
        """
        vérifie la justesse du nombre de temps enregistré et si il est faux le modifie
        """
        file = self.get_json_file_content("./sessions/{}".format(session))
        nmbTimes = len(file["times"])
        if nmbTimes != file["times_in_session"]:
            self.change_Number_of_times(session, nmbTimes, file)
            return "changed"
        else: 
            return "perfect"

    def session_creator(self) -> str:
        name = str(input("nom de la nouvelle session >> "))
        self.create_session(name)
        return name

    def create_existing_sessions_list(self) -> list[str]:
        """
        genere la liste des fonctions créées à partir du fichier memory
        """
        session_list = []
        with open("./sessions/memory.txt", 'r', encoding='utf-8') as file:
            session_list = file.read().splitlines()
        return session_list

    def sessionManagerDeb(self) -> str:
        currentSession = None
        while currentSession is None:
            print("voulez vous créer une nouvelle session ou entrer dans une déjà existente ? ")
            print("")
            print("   déjà existante : 1")
            print("   créer une session : 2")
            answer = str(input(' >> '))
            if answer == "2":
                sessionName = self.session_creator()
                answer = str(input("voulez vous utiliser cette session ? (y/n) >> "))
                if answer == "y":
                    currentSession = sessionName
            elif answer == "1":
                session_list = self.create_existing_sessions_list()
                print("")
                for elem in session_list:
                    print(elem)
                print("")
                answer = None
                while answer not in session_list:
                    answer = str(input("entrez le nom de la session dans laquelle vous voulez entrer >> "))
                currentSession = answer
        return currentSession

