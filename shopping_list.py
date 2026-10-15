shopping_list = []

while True:
    action = input("Choose an action (add / remove / show / done): ").strip().lower()

    if action == "add":
        item = input("What item would you like to add? ").strip()
        if item:
            shopping_list.append(item)
            print(f"Added {item}.")
        else:
            print("Please enter an item.")
    elif action == "remove":
        item = input("What item would you like to remove? ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Removed {item}.")
        else:
            print("That item is not on your list.")
    elif action == "show":
        if shopping_list:
            for item in shopping_list:
                print(item)
        else:
            print("Your shopping list is empty.")
    elif action == "done":
        print("Goodbye!")
        break
    else:
        print("Please choose add, remove, show, or done.")
