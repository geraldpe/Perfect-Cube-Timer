
import subprocess
import time

def scramble():
    result = ""
    subprocess.call("scramble.exe")
    time.sleep(0.2)
    with open("interface.txt", "r", encoding="utf-8") as interface:
        result = interface.read()

    #clearing the interface file
    with open("interface.txt", "w", encoding="utf-8") as interface:
        interface.write("")
    
    return result

for i in range(5):
    print(scramble())