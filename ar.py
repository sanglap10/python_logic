fruits = ["Apple","Mango"]

def main():
    while True:
        print("\nWelcome to the array program! Please select an option: ")
        print("1. View array")
        print("2. Add single element")
        print("3. Add multiple element")
        print("4. Delete an element")
        print("5. Replace an element")
        print("6. Exit")

        choice = int(input("select your choice 1-6: "))

        if choice == 1:
            view_element()
        elif choice == 2:
            add_element()
        elif choice == 3:
            add_multiple_element()
        elif choice == 4:
            delete_element()
        elif choice == 5:
            replace_element()
        elif choice == 6:
            break
        else:
            print("Invalid choice! Please select mentioned choice only")
         
def view_element():
    print(fruits)


def add_element():
    fruit_name = input("Enter a name of fruit: ")
    fruits.append(fruit_name)
    print(fruits)

def add_multiple_element():
    totalFruits = int(input("Enter total fruits: "))
    for i in range(1,totalFruits+1):
        name = input(f"Enter fruit{i}: ")
        fruits.append(name)
    print(fruits)

def replace_element():
    print(fruits)
    found = False
    oldFruit = input("Enter name of fruit to be replace: ")
    newFruit = input("Enter new fruit: ")
    for i in fruits:
        if i.lower() == oldFruit.lower():
            index = fruits.index(i)
            fruits[index] = newFruit
            found = True
            break

    if found == True:
        print(fruits)
    else:
        print(f"{oldFruit} does not exist")
    
def delete_element():
    found = False
    fruitname = input("Enter the fruit to be deleted: ")
    for i in fruits:
        if i.lower() == fruitname.lower():
            fruits.remove(fruitname)
            found = True
            break
    
    if found == True:
        print(fruits)
    else:
        print(f"{fruitname} does not exist")
    
main()