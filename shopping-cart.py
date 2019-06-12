# shopping_cart.py
shopping = True

import datetime

from datetime import date
from datetime import time

from pprint import pprint

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#print(products)
# pprint(products)

user_date = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) #consulted: https://stackoverflow.com/questions/7999935/python-datetime-to-string-without-microsecond-component for datetime help

    #user_input = int(input())
    #print(user_input)

total_price = 0
selected_ids = []

while True: 
    try: 
        user_input = input("Please input a product identifier: ")

        if user_input == "DONE" or "done" or "Done":
            break
        elif int(user_input) > 20:
            print("Error, please enter valid number")
        elif int(user_input) <= 0:
            print("Error, please enter a valid number")
        else: 
            selected_id = str(user_input)
            selected_ids.append(selected_id)
    except ValueError:
        print("Error, please enter valid number")

for selected_id in selected_ids:
    matching_products = [p for p in products if int(p["id"]) == int(selected_id)]
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    print("SELECTED PRODUCT:" + matching_product["name"] + " " + str(matching_product["price"]))

tax = total_price * 0.0875
final_price = total_price + tax

print("-----------")
print("Amy's Market")
print("www.amys-market.com")
print("-----------")
print("CHECKOUT AT:" + user_date)
print("-----------")

print("SUBTOTAL: " + str(round(total_price, 2))) #stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python
print("TAX: " + str(round(tax,2)))
print("TOTAL: " + str(round(final_price,2)))

#print(final product list)

#print(subtotal)

#print(tax)

print("-----------")
print("THANK YOU, COME BACK SOON!")
print("-----------")



