# Lucas Villarroel

import sys

logs_file1 = (sys.argv[1])
logs_file2 = (sys.argv[2])

# Se leen los archivos con los logs
with open(logs_file1, "r") as file:
    logs = file.read().splitlines()

with open(logs_file2, "r") as file:
    logs += file.read().splitlines()

# Se aplica la función split
logs_splitted = (list(map(lambda s: s.split(";"), logs)))

# Se ordenan por el 3er elemento
logs_sorted = sorted(logs_splitted, key=lambda x: int(x[2]))

# Se escriben los logs ordenados
with open("logs_ordenados", "w") as file:
    for log in logs_sorted:
        file.write("%s\n" % ";".join(log))
