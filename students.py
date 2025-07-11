import csv 

name = input("Enter your name :")
home = input("Where do you live : ")

with open("student.csv" , "a", newline="") as file :
    writer = csv.DictWriter(file , fieldnames=["name", "home"])
    writer.writerow({"name": name , "home": home})