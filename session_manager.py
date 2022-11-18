
import json

def get_json_file_content(path):
    with open("{}".format(path), "r", encoding="utf-8") as jsfile:
        result = json.load(jsfile)
    return result

def save_time_in_session(sessionName, time):
    session_file: list = []
    if time is not None:
        session_file = get_json_file_content("sessions/{}.json".format(sessionName))
        session_file.append(time)
    with open("sessions/{}.json".format(sessionName), "w", encoding="utf-8") as jsfile:
        json.dump(session_file, jsfile, indent=2)

def create_session(sessionName):
    with open("sessions/{}.json".format(sessionName), "w") as file:
        json.dump([], file)
    session_list = []
    with open("memory.txt", "r", encoding="utf-8") as file:
        session_list = file.read().splitlines()
    with open("memory.txt", 'w', encoding='utf-8') as file:
        for elem in session_list:
            file.write(elem + "\n")
