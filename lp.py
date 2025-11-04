file = open("numbers.txt", "r")
lines = file.readlines()
n = [int(i.rstrip()) for i in lines]

