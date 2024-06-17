want_to_exit = False
while not want_to_exit:
    choice = int(input("Do you want to: \n1. Calculate overtime bonus \n2. Calculate how much to sell for buying equipment & moons \n3. Calculate scrap value to get per day to meet quota \nType 1,2 or 3: "))
    if choice == 1:
        quota = int(input("What's the quota?: "))
        how_much_sold = int(input("How much sold?: "))
        overtime_bonus = int((how_much_sold - quota)/5 - 15)
        if overtime_bonus <= 0:
            print("Overtime bonus is: $0")
        else:
            print(f"Overtime bonus is: ${overtime_bonus}")
        continue_choice = input("Do you want to continue? (Y/N): ")
        if continue_choice == "N" or continue_choice == "n":
            want_to_exit = True    
    
    elif choice == 2:
        quota = int(input("What's the quota?: "))
        total_money_earned = int(input("How much money do you want to have including overtime bonus?: $"))
        
        has_existing_money = input("Do you have existing credits?(Y/N): ")
        if has_existing_money == "Y" or has_existing_money == "y":
            original_credits_on_ship = input(int("How much do you have?: "))
            total_money_earned -= original_credits_on_ship

        check_decimal_points = (5*total_money_earned + quota + 75) % 6
        if check_decimal_points == 0:
            how_much_sold = int(5*total_money_earned + quota + 75)/6
            print(f"You need to sell: ${how_much_sold}")
        else:
            how_much_sold = int((5*total_money_earned + quota + 75)/6) + 1
            print(f"You need to sell: ${how_much_sold}")

        continue_choice = input("Do you want to continue? (Y/N): ")
        if continue_choice == "N" or continue_choice == "n":
            want_to_exit = True
    
    elif choice == 3:
        quota = int(input("What's the quota?: "))
        value_on_ship = int(input("How much value do you have on ship?: "))
        days_left = int(input("How many days left until deadline?: "))
        if value_on_ship > quota:
            print("You have already met the quota.")
        else:
            check_decimal_points = (quota - value_on_ship) % days_left
            if check_decimal_points == 0:
                average_value_per_day = int((quota - value_on_ship)/days_left)
            else:
                average_value_per_day = int((quota - value_on_ship)/days_left) + 1
            print(f"You need to get ${average_value_per_day} per day to meet the quota.") 
        continue_choice = input("Do you want to continue? (Y/N): ")
        if continue_choice == "N" or continue_choice == "n":
            want_to_exit = True   

    else:
        print("No such choice.")
 