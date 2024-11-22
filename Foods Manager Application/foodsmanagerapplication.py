# Foods Manager Application
Foods_List = []

def display_menu():
    print("\n--- Welcome Foods Manager Application ---")
    print("1. Add Food")
    print("2. Remove Food")
    print("3. View All Foods")
    print("0. Exit")

while True:
    display_menu()
    try:
        choice = int(input("~ Select an option: "))
    except ValueError:
        print("Error: Invalid input! Please enter a number from the options.")
        continue

    if choice == 1:
        food_name = input("\t- Enter the name of the food: ").strip().capitalize()
        try:
            food_price = float(input("\t- Enter the price of the food: "))
            Foods_List.append((food_name, food_price))
            print(f"\t- Success: '{food_name}' added with a price of ${food_price:.2f}.")
        except ValueError:
            print("Error: Invalid price! Please enter a numerical value.")

    elif choice == 2:
        food_name = input("\t- Enter the name of the food to remove: ").strip().capitalize()
        for food in Foods_List:
            if food[0] == food_name:
                Foods_List.remove(food)
                print(f"\t- Success: '{food_name}' has been removed.")
                break
        else:
            print(f"\t- Error: '{food_name}' not found in the favorite foods list.")

    elif choice == 3:
        if Foods_List:
            print("\t- All Foods List:")
            for i, (name, price) in enumerate(Foods_List, start=1):
                print(f"\t- {i}. {name} - ${price:.2f}")
        else:
            print("\t- No favorite foods have been added yet.")

    elif choice == 0:
        print("\t- Thank you for using the Foods Manager. Goodbye!")
        break

    else:
        print("\t- Error: Invalid choice, please select again.")
