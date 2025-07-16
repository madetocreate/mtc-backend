def main():
    print("Creator Engine CLI Menü")
    print("1. Video Creator")
    print("2. Audio Creator")
    print("3. GPT Wizard")
    print("0. Exit")

    while True:
        choice = input("Bitte Auswahl: ")
        if choice == '1':
            print("Starte Video Creator...")
        elif choice == '2':
            print("Starte Audio Creator...")
        elif choice == '3':
            print("Starte GPT Wizard...")
        elif choice == '0':
            print("Exit")
            break
        else:
            print("Ungültig!")

if __name__ == "__main__":
    main()
