


def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Try again.")
        return get_user_choice()
    return user_choice
