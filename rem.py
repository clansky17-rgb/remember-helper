import os

if not os.path.exists("rem.txt"):
    with open("rem.txt", "w", encoding="utf-8") as file:
        pass

while True:
    rem = input("What do you need help rembering, type 'rem' to rember it, or type take down to remove an item ")
    if rem == "rem":
        with open("rem.txt", "r", encoding="utf-8") as file:
            contents = file.readlines()
        if not contents:
            print("Your list is empty.")
        else:
            for i, line in enumerate(contents, start=1):
                print(f"{i}. {line.strip()}")
    elif rem == "take down":
        with open("rem.txt", "r", encoding="utf-8") as file:
            contents = file.readlines()
        num = int(input("Which number do you want to take down? "))
        if 1 <= num <= len(contents):
            removed = contents.pop(num - 1)
            with open("rem.txt", "w", encoding="utf-8") as file:
                file.writelines(contents)
            print(f"Took down: {removed.strip()}")
        else:
            print("That number is not on the list.")
    else:
        with open("rem.txt", "a", encoding="utf-8") as file:
            file.write(rem + "\n")


        
