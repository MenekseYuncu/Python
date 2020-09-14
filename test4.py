with open("yazilim.txt", "r+") as dosya:
    data = dosya.readlines()
    data.insert(1, "welcome\n")
    dosya.seek(0)
    dosya.writelines(data)
