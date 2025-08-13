fruits = ["apple","mango"]

def main():
    fruit_name = input("Enter a name of fruit: ")
    fruits.append(fruit_name)
    print(fruits)

def total_fruits():
    totalFruits = int(input("Enter total fruits: "))
    for i in range(1,totalFruits+1):
        name = input(f"Enter fruit{i}: ")
        fruits.append(name)
    print(fruits)

def replace_element():
    fName = input("Enter name of fruit: ")
    fruits[1] = fName
    print(fruits)

def delete_element():
    found = False
    fruitname = input("Enter the fruit to be deleted: ")
    for i in fruits:
        if i.lower() == fruitname.lower():
            fruits.remove(fruitname)
            found = True
            break
    
    if found:
        print(fruits)
    else:
        print(f"{fruitname} does not exist")
    

delete_element()
#replace_element()
#main()
#total_fruits()
