import os

os.mkdir("new-dir")
with open(os.path.join("new-dir", "new-file.txt"), "w") as fd:
    fd.write("Hola")
