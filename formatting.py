# Prompt user to "press 'Enter' to continue...""
def press_enter():
    input("Press 'Enter' to continue...")

# Adds lines at the top of the current page.
def top_lines():
    print("==================================================================================================")

# Adds lines at the bottom of the current page.
def bot_lines():
    print("==================================================================================================\n")

# Error shown if contact is not found.
def contact_not_found():
    text1 = "\nCONTACT NOT FOUND!"
    title1 = "\x1B[1;4m" + text1 + "\x1B[0m" + "\n"
    print(title1)
    text2 = "Please note:"
    title2 = "\x1B[3;4m" + text2 + "\x1B[0m"
    print(title2)
    print("1. The search is case sensitive.")
    print("2. The search requires the full name to be entered exactly as it was added to the Contact Book!\n") 
    text3 = "Tip: If you're unsure of the full name, press '1' from the Main Menu to view all contacts.\n"
    title3 = "\x1B[3m" + text3 + "\x1B[0m"
    print(title3)