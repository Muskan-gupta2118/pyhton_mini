def add_price(price_list):
    price = int(input("Enter the price: "))
    price_list.append(price)

def get_average_price(price_list):
    if len(price_list) == 0:
        return 0
    return sum(price_list) / len(price_list)

def get_max_price(price_list):
    if len(price_list) == 0:
        return 0
    return max(price_list)

price_list = []

while True:
    print("\nMenu:")
    print("1. Add price")
    print("2. Show average price")
    print("3. Show highest price")
    print("q. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_price(price_list)

    elif choice == '2':
        avg = get_average_price(price_list)
        print("Average price:", avg)

    elif choice == '3':
        highest = get_max_price(price_list)
        print("Highest price:", highest)

    elif choice == 'q':
        print("You quit!!!")
        break

    else:
        print("You entered a wrong number")
