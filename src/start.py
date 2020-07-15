# E-Commerce
# What data is needed to have a store front
# defining an object
# constructor == __init__
# blueprint for the store objects - can create 100s later
# self is basically the equivalent of this in JS without the nuances of JS - obj - to reference the obj category
# super === obj of the parent that the child is inherenting == same DNA/atttibutes
# categories are a list []
# OOO == bundling and reuse data

# from [filename] import [class name]
from category import Category

class Store:
    def __init__(self, name, categories):
        # attributes
        self.name = name
        self.categories = categories

    def __str__(self):
        output = f"{self.name}" + "\n"
        for i, c in enumerate(self.categories):
            output += " " + str(i+1) + ". " + c + "\n"
        return output
    
# storing the class definition obj in the computer's memory
my_store = Store("Cat's Bodeguita", [Category("food"), Category("beverage"), Category("clothing")])
print(my_store)
 
selection = 0
while int(selection) != len(my_store.categories)+1:
    selection = input("Select the number of a department: ")
    
    try: 
        # move casting to int into the try block - 
        selection = int(selection)
        if selection == len(my_store.categories)+1:
            print("Thanks for shopping.")
        elif selection > 0 and selection <= len(my_store.categories):
            print(my_store.categories[selection - 1])
        else:
            print("Please select a valid number")
    except ValueError: 
        print("Please enter your choice as a number")
        
