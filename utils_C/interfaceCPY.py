
import subprocess
import time
import pathlib as pl

def get_file_paths() -> tuple[str]:
    return (str(pl.Path().absolute() / "utils_C/scramble.exe"),
            str(pl.Path().absolute() / "utils_C/interface.txt"))

def scramble(filePath, interfacePath):
    
    result = ""
    subprocess.call(filePath)
    time.sleep(0.2)
    with open(interfacePath, "r", encoding="utf-8") as interface:
        result = interface.read()

    #clearing the interface file
    with open(interfacePath, "w", encoding="utf-8") as interface:
        interface.write("")
    
    return result
