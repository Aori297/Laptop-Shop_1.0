import os
from datetime import date


def clear():
    if os.name == 'posix':
        clear = "clear"
    else:
        clear = "cls"
    os.system(clear)


# storing data from laptop.txt to a list
laptop_list = []

# indexing in the list
sn = 1
with open("laptop.txt", "r") as file:
    for line in file:
        laptops = line.split(",")

        for x in range(0, len(laptops)):
            # strips each word in the array of trailing whitespaces
            laptops[x] = laptops[x].strip()

        # append a dict of laptop in the list
        laptop_list.append(
            dict(
                id=sn,
                name=laptops[0],
                manufacturer=laptops[1],
                price=laptops[2],
                quantity=int(laptops[3]),
                cpu=laptops[4],
                gpu=laptops[5]
            )
        )
        sn += 1


def sell():
    customer_details = {
        "name": "",
        "phone": "",
        "cart": [],
        "quantity": [],
        "price": [],
        "total": []
    }
    display()
    print("Enter customer details... ")
    print("-" * 100)
    customer_details["name"] = input("Enter the name of the customer: ")
    customer_details["phone"] = input(
        "Enter the phone number of the customer: ")
    print("-" * 100)
    while True:
        choice = input(
            f"Enter the id of the laptop to sell (1 - {len(laptop_list)}): ")
        try:
            choice = int(choice)
            if choice > len(laptop_list) or choice <= 0:
                raise IndexError
            laptop = laptop_list[choice - 1]  # can raise IndexError
            print("-" * 100)
            print(f"Selling {laptop['name']}")
            print("-" * 100)
            qty = input("Enter quantity to sell: ")
            qty = int(qty)
            if qty < 0 or qty > laptop["quantity"]:
                raise ValueError
            laptop["quantity"] -= qty
            price = int(laptop['price'][1:])
            total = price * qty
            print("Cost: $", total)
            customer_details["cart"].append(laptop["name"])
            customer_details["quantity"].append(qty)
            customer_details["price"].append(price)
            customer_details["total"].append(total)
            print()
            update_data()
            loop = input("Do you want to add more items (Y/N)? ").lower()
            if loop != 'y':
                break

        except ValueError:
            print("Invalid value.")
            return
        except IndexError:
            print("That ID does not exist...")
            print("-" * 100, "\n")
            return

    generate_bill(customer_details)
    write_bill(customer_details)
    print("Thanks for shopping...\n\n")
    return


def display():
    clear()
    # .center(n) --> centers the string literal with equal spaces around
    print("Inventory".center(116))
    print()
    print("-" * 116)

    # string formatting
    # aligning text to the left while reserving `n` characters
    print_format = "{:<3} | {:<20} | {:<15} | {:<8} | {:<10} | {:<20} | {:<20} |"
    print(print_format.format("ID", "Name", "Manufacturer",
          "Price", "Quantity", "CPU", "GPU"))
    print("-" * 116)

    for laptop in laptop_list:
        print(print_format
              .format(laptop["id"], laptop["name"], laptop["manufacturer"], laptop["price"], laptop["quantity"], laptop["cpu"], laptop["gpu"]))
        print("-" * 116)
    print("\n" * 2)
    return


def generate_bill(details):
    length = range(len(details["cart"]))
    cart = details["cart"]
    prices = details["price"]
    qtys = details["quantity"]
    totals = details["total"]
    amount = 0
    for x in totals:
        amount += x
    clear()
    print("Generating bill...")
    print()
    print("The Notebook Warehouse".center(62))
    print("_" * 64)
    ok_format = "| {:<8} {:<52}|"
    print(ok_format.format("Name: ", details["name"]))
    print(ok_format.format("Phone: ", details["phone"]))
    print(ok_format.format("Date: ", str(date.today())))
    print("-" * 64)
    bill_format = "| {:<3} | {:<20} | {:<8} | {:<10} | {:<7} |"
    print(bill_format.format("SN", "Item", "Price", "Quantity", "Amount"))
    print("-" * 64)
    for i in length:
        print(bill_format.format(length[i] + 1,
              cart[i], "$" + str(prices[i]), qtys[i], "$" + str(totals[i])))
        print("-" * 64)
    print()
    print("{:>63}".format("Total amount: $" + str(amount)))
    print()


def write_bill(details):
    # destructuring?
    _date = str(date.today())
    name = details['name'].replace(" ", "_")
    phone = details['phone']
    cart = details['cart']
    length = range(len(cart))
    prices = details['price']
    qtys = details['quantity']
    totals = details['total']
    amount = 0
    for x in totals:
        amount += x

    # writing to file
    bill_format = "| {:<3} | {:<20} | {:<8} | {:<10} | {:<7} |"
    ok_format = "| {:<8} {:<52}|"
    with open(f"./bills/{name}_c.txt", "a") as file:
        file.write("-" * 64 + "\n")
        file.write(ok_format.format("Name: ", details["name"]) + "\n")
        file.write(ok_format.format("Phone: ", phone) + "\n")
        file.write(ok_format.format("Date: ", _date) + "\n")
        file.write("-" * 64 + "\n")
        file.write(bill_format.format(
            "SN", "Item", "Price", "Quantity", "Amount") + "\n")
        for i in length:
            file.write(bill_format.format(length[i] + 1,
                                          cart[i], "$" + str(prices[i]), qtys[i], "$" + str(totals[i])) + "\n")
        file.write("-" * 64 + "\n")
        file.write("\n")
        file.write("{:>63}".format("Total amount: $" + str(amount)) + "\n")
        file.write("\n")


def update_data():
    with open("laptop.txt", "w") as file:
        for laptop in laptop_list:
            file.write(
                f"{laptop['name']}, {laptop['manufacturer']}, {laptop['price']}, {laptop['quantity']}, {laptop['cpu']}, {laptop['gpu']}\n"
            )


def buy():
    buy_details = {
        "name": "Owner",
        "phone": "9800000000",
        "cart": [],
        "quantity": [],
        "price": [],
        "total": []
    }
    clear()
    while True:
        print("-" * 100)
        print("\n\n\n")
        print("1. Restock current laptops")
        print("2. Buy new laptops")
        print("3. Exit")
        print("-" * 100)
        print("\n\n")
        choice = input("What would you like to do? ")

        if choice == "1":
            display()
            restock = input(
                f"Enter id of the laptop to restock (1 - {len(laptop_list)}): ")
            try:
                restock = int(restock)
                if restock > len(laptop_list):
                    raise IndexError
                laptop = laptop_list[restock - 1]
                qty = int(input("Enter quantity to restock: "))
                if qty < 0:
                    raise ValueError
                price = int(laptop["price"][1:])
                total = qty * price
                laptop["quantity"] += qty
                print(f"Restocked {qty} {laptop['name']}")
                print(f'Cost: ${total}')
                print()
                update_data()
                buy_details["cart"].append(laptop["name"])
                buy_details["quantity"].append(qty)
                buy_details["price"].append(price)
                buy_details["total"].append(total)
            except ValueError:
                clear()
                print("Invalid input")
            except IndexError:
                clear()
                print("That ID does not exist.")
        elif choice == "2":
            clear()
            sn = len(laptop_list) + 1
            name = input("Enter laptop name: ")
            manufacturer = input("Enter laptop manufacturer: ")
            laptop_price = input("Enter price: ")
            quantity = input("Enter quantity: ")
            cpu = input("Enter CPU: ")
            gpu = input("Enter gpu: ")
            try:
                quantity = int(quantity)
                laptop_list.append(
                    dict(
                        id=sn,
                        name=name,
                        manufacturer=manufacturer,
                        price="$" + laptop_price,
                        quantity=quantity,
                        cpu=cpu,
                        gpu=gpu
                    )
                )
                sn += 1
                laptop_price = int(laptop_price)
                ttl = laptop_price * quantity
                print(f"Cost: ${ttl}")
                buy_details["cart"].append(name)
                buy_details["quantity"].append(quantity)
                buy_details["price"].append(laptop_price)
                buy_details["total"].append(ttl)
                update_data()
                print(f"Bought {quantity} {name} from {manufacturer}...")
                print()

            except ValueError:
                print("Invalid value.. ")

        elif choice == "3":
            clear()
            generate_bill(buy_details)
            write_bill(buy_details)
            return
        else:
            clear()
            print("Invalid input..")
