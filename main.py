with open("./Input/Names/invited_names.txt") as file:
    names = file.read().split("\n")

for name in names:
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
        new_letter = letter.read().replace("[name]", name)

    with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as f:
        f.write(new_letter)
