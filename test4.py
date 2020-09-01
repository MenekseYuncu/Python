f = open("demofile3.txt", "w")
f.write("içeriği sildim")
f.close()

f = open("demofile.txt", "r")
print(f.readline())
