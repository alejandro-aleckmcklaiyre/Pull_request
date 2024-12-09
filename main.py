#mainmenu

from package import alejandro

def main_menu():
    while True:
        print("\n---Main Menu ---")
        print("1. Alejandro")
        print("2. De Leon")
        print("3. Esparagoza")
        print("4. Gomez")
        print("5. Mosenos")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            print("-----------------------------------")
            alejandro.greetings()

        elif choice == '2':
            print("-----------------------------------")

        elif choice == '3':
            print("-----------------------------------")

    
        elif choice == '4':
            print("-----------------------------------")

        elif choice == '5':
            print("-----------------------------------")

   
        elif choice == '6':
            print("\nExiting program.\n")
            break
        else:
            print("\nInvalid option. Please try again.\n")

# Run the main menu
if __name__ == "__main__":
    main_menu()