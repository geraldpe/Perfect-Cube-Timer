
import json

def get_json_file_content(path):
    with open("{}".format(path), "r", encoding="utf-8") as jsfile:
        result = json.load(jsfile)
    return result

def save_time_in_session(sessionName, time):
    session_file = {}
    if time is not None:
        session_file = get_json_file_content("sessions/{}.json".format(sessionName))
        session_file["times"].append(time)
        session_file["times_in_session"] += 1
    with open("sessions/{}.json".format(sessionName), "w", encoding="utf-8") as jsfile:
        json.dump(session_file, jsfile, indent=2)

def delete_last_time_in_session(sessionName):
    session_file = {}
    session_file = get_json_file_content("sessions/{}.json".format(sessionName))
    session_file["times"]: list .pop(len(session_file["times"])-1)
    session_file["times_in_session"] -= 1
    with open("sessions/{}.json".format(sessionName), "w", encoding="utf-8") as jsfile:
        json.dump(session_file, jsfile, indent=2)

def create_session(sessionName):
    with open("sessions/{}.json".format(sessionName), "w") as file:
        json.dump({"times_in_session": 0, "times": []}, file)
    session_list = []
    with open("memory.txt", "r", encoding="utf-8") as file:
        session_list = file.read().splitlines()
    session_list.append(sessionName)
    with open("memory.txt", 'w', encoding='utf-8') as file:
        for elem in session_list:
            file.write(elem + "\n")
