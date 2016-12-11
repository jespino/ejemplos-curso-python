import os

os.mkdir("new-dir")
fd = open(os.path.join("new-dir", "new-file.txt"), "w")
fd.write("Hola")
fd.close()
