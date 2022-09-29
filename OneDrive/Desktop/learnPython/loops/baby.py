from random import choice
questions = ["Why is the sky blue?","why is that dog running?", "Where do you want me to be?"]

answer = input(choice(questions)).lower()
while (answer != "just because"):
    answer = input("Why").strip().lower()

print("Oh... ok")