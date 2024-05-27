import hashlib


def hash_password(passw):
    hash_obj = hashlib.sha256()
    hash_obj.update(passw.encode("utf-8"))
    return hash_obj.hexdigest()


def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            print(line)
            print(line.strip())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    hashed_pwd = hash_password(pwd)
    with open("password.txt", "a") as f:
        f.write(name + "|" + hashed_pwd + "\n")

if __name__ == "__main__":
    bienvenue = input("Bienvenue dans le monde de l'aventure des mots de passe**/Enter/**  ")
    name = input("Quel est votre nom ? : ")
    option = input("**{}** tu veux voir le mot de pass, ajouter , ou quitter le programme? View,Add or Q? : ".format(name))

    while option.lower() != "q":
        if option == "view":
            view()
        elif option == "add":
            add()
        else:
            print("Add your name")
            name = input("Quel est votre nom ? : ")

        option = input("View or Add? : ")
