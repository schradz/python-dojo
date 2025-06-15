def get_user_difficulty():
    print("What difficulty challenge will you attempt?")
    selected_difficulty = input()
    if selected_difficulty.lower() == "easy":
        return selected_difficulty.lower()
    elif selected_difficulty.lower() == "medium":
        return selected_difficulty.lower()
    elif selected_difficulty.lower() == "hard":
        return selected_difficulty.lower()
    else:
        return "error"
    

def main():
    selected_difficulty = get_user_difficulty()


if __name__ == "__main__":
    main()