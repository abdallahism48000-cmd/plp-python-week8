# ==============================================
# Personal Mini-Toolkit
# Author: Abdallah Ahmed Mohamed
# Description: A menu-driven program combining lists, 
# loops, conditionals, and interactive tools.
# ==============================================

import random

def show_banner():
    """Displays a welcoming startup banner."""
    print("\n" + "=" * 42)
    print("      WELCOME TO YOUR PERSONAL MINI-TOOLKIT     ")
    print("=" * 42)

# Tool 1: Quick Notes Manager (Uses lists, loops, and conditionals)
def quick_notes_manager():
    """Allows the user to add, view, and clear quick notes dynamically using a list."""
    notes = []
    print("\n--- Tool 1: Quick Notes Manager ---")
    
    while True:
        print("\n[1] Add a Note")
        print("[2] View All Notes")
        print("[3] Clear All Notes")
        print("[4] Back to Main Menu")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            note = input("Enter your note: ").strip()
            if note:
                notes.append(note)
                print(f"Success: '{note}' has been added.")
            else:
                print("Note cannot be empty.")
        elif choice == "2":
            if not notes:
                print("Your notes list is currently empty.")
            else:
                print("\nYour Notes:")
                for index, n in enumerate(notes, start=1):
                    print(f"{index}. {n}")
        elif choice == "3":
            notes.clear()
            print("All notes have been cleared.")
        elif choice == "4":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 4.")

# Tool 2: Number Guessing Game (Uses loops and conditionals)
def number_guessing_game():
    """A game where the user guesses a randomly generated number between 1 and 10."""
    print("\n--- Tool 2: Number Guessing Game ---")
    secret_number = random.randint(1, 10)
    attempts = 0
    
    print("I have picked a secret number between 1 and 10. Try to guess it!")
    
    while True:
        guess_input = input("Enter your guess (or type 'quit' to exit): ").strip().lower()
        
        if guess_input == "quit":
            print(f"Exiting game. The secret number was {secret_number}.")
            break
            
        if not guess_input.isdigit():
            print("Please enter a valid number.")
            continue
            
        guess = int(guess_input)
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break

# Tool 3: Tip Calculator (Uses conditionals and arithmetic)
def tip_calculator():
    """Calculates meal tips and total bill shares based on service quality."""
    print("\n--- Tool 3: Tip Calculator ---")
    
    try:
        bill = float(input("Enter the total bill amount ($): "))
        if bill < 0:
            print("Bill amount cannot be negative.")
            return
            
        print("Service Rating: [1] Good (20%) [2] Fair (15%) [3] Poor (10%)")
        rating = input("Choose service rating (1-3): ").strip()
        
        if rating == "1":
            tip_percent = 0.20
        elif rating == "2":
            tip_percent = 0.15
        elif rating == "3":
            tip_percent = 0.10
        else:
            print("Invalid rating choice. Defaulting to 15%.")
            tip_percent = 0.15
            
        people = int(input("Enter number of people splitting the bill: "))
        if people <= 0:
            print("Number of people must be at least 1.")
            return
            
        tip_amount = bill * tip_percent
        total_bill = bill + tip_amount
        per_person = total_bill / people
        
        print("\n--- Bill Summary ---")
        print(f"Tip Amount: ${tip_amount:.2f}")
        print(f"Total Bill (incl. tip): ${total_bill:.2f}")
        print(f"Each person pays: ${per_person:.2f}")
        print("-" * 22)
        
    except ValueError:
        print("Invalid input detected. Please enter valid numbers.")

# Main Program Loop
def main():
    show_banner()
    
    while True:
        print("\n==============================")
        print("       MAIN MENU PROGRAM      ")
        print("==============================")
        print("1. Quick Notes Manager")
        print("2. Number Guessing Game")
        print("3. Tip Calculator")
        print("4. Quit")
        print("==============================")
        
        choice = input("Select a tool (1-4): ").strip()
        
        if choice == "1":
            quick_notes_manager()
        elif choice == "2":
            number_guessing_game()
        elif choice == "3":
            tip_calculator()
        elif choice == "4":
            print("\nThank you for using Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print("\n[!] Invalid choice. Please select an option between 1 and 4.")

if __name__ == "__main__":
    main()
