import sys
import time
from files.operations import *
from files.read import *
from files.write import *

def main():    
    while True:
        print("The Notebook Warehouse".center(100))
        print("Basundhara, Kathmandu".center(100))
        print("-" * 100)
        print("1. View Inventory")
        print("2. Sell Laptops")
        print("3. Purchase Laptops")
        print("4. Exit")
        print("_" * 100)
        print()
        option = input("What would you like to do? ")
        
        if option == "1":
            display()
        
        elif option == "2":
            sell()
            
        elif option == '3':
            buy()

        elif option == '4':
            print("\n")
            print("Exitting...")
            time.sleep(1)
            sys.exit()
        else:
            print("Invalid input ... ")
            print()

main()


