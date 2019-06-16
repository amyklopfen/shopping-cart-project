# shopping-cart-project

#clone repo in Github to place under control; download to Github desktop

# shopping_cart.py

shopping = True

import os
from dotenv import load_dotenv
import sendgrid

# info drawn from send notification exercise.

from sendgrid.helpers.mail import * 

# copied env file from notification exercies, used same API key.

load_dotenv()

import datetime

from datetime import date
from datetime import time

import pprint

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per": "F"},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price_per": "F"},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price_per": "F"},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per": "F"},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price_per": "F"},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99, "price_per": "F"},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50, "price_per": "F"},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25, "price_per": "F"},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50, "price_per": "F"},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99, "price_per": "F"},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99, "price_per": "F"},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50, "price_per": "F"},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00, "price_per": "F"},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99, "price_per": "F"},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50, "price_per": "F"},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50, "price_per": "F"},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99, "price_per": "F"},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50, "price_per": "F"},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99, "price_per": "F"},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price_per": "F"}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


# consulted: https://stackoverflow.com/questions/7999935/python-datetime-to-string-without-microsecond-component for datetime help

# turned datetime into string

user_date = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%p")) 

total_price = 0
selected_ids = []
new_price = 0

#used try/except for error handling to ensure that any invalid input will redirect user to input prompt

while True: 
    try: 
        user_input = input("Please input a product identifier: ")

#used lower function to account for different forms of entering 'done.' Recommended by Zach Diamond!

        if user_input.lower() == "done": 
            break

#converted user input back to int for comparison

        elif int(user_input) > 20: #converted back to int for > comparison
            print("Error, please enter valid number")
        elif int(user_input) <= 0:
            print("Error, please enter a valid number")
        else: 
            selected_id = str(user_input)
            selected_ids.append(selected_id)
    except ValueError:
        print("Error, please enter valid number")

#print receipt text 

print("-----------")
print("Amy's Market")
print("www.amys-market.com")
print("-----------")
print("CHECKOUT AT:" + user_date)
print("-----------")

#set up for loop to account for any user selection, match price of selected item, and calculate the total price of user selection

for selected_id in selected_ids:
    matching_products = [p for p in products if int(p["id"]) == int(selected_id)]
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    print("SELECTED PRODUCT: " + matching_product["name"] + " " + str(matching_product["price"]))

tax = total_price * 0.0875
final_price = total_price + tax

#print subtotoal/tax/total and convert prices to USD using $"${0:.2f}".format() command

print("SUBTOTAL: " + "${0:.2f}".format(total_price)) 
print("TAX: " + "${0:.2f}".format(tax))
print("TOTAL: " + "${0:.2f}".format(final_price))

print("-----------")
print("THANK YOU, COME BACK SOON!")
print("-----------")

# Write receipt to file. Tailored from course notes on writing to file

# revised from datetime in receipt for filename, %p; including AM/PM threw off code

my_receipt = (datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) 

# use html coding for nicer format in output file

# open(), 'w' commands creates and opens new file for writing

# file.write() will write the text to the new file

with open("receipt-" + my_receipt + ".txt", "w") as file: 
    file.write("-----------")
    file.write("\n")
    file.write("Amy's Market")
    file.write("\n")
    file.write("www.amys-market.com")
    file.write("\n")
    for selected_id in selected_ids:
        matching_products = [p for p in products if int(p["id"]) == int(selected_id)]
        matching_product = matching_products[0]
        new_price = new_price + matching_product["price"] #needed to create new variable from final_price; otherwise price was doubled in receipts
        file.write("SELECTED PRODUCT: " + matching_product["name"] + " " + str(matching_product["price"]) + "\n")
    file.write("CHECKOUT AT:" + user_date)
    file.write("\n")
    file.write("SUBTOTAL: " + "${0:.2f}".format(total_price))
    file.write("\n")
    file.write("TAX: " + "${0:.2f}".format(tax))
    file.write("\n")
    file.write("TOTAL: " + "${0:.2f}".format(final_price))
    file.write("\n")
    file.write("-----------")
    file.write("\n")
    file.write("THANK YOU, COME BACK SOON!")
    file.write("\n")
    file.write("-----------")

# Send email receipt; tailed code off notification exercise

# input prompt allows email to be sent to any user email

user_email = input("Please enter your email for an electronic copy of your receipt: ")

# from email saved in env file with API key

from_email = Email(MY_EMAIL_ADDRESS)
to_email = Email(user_email)
subject = "Your receipt from Amy's Market"

# must concatenate strings for message

message_text = "-----" + " " + "Amy's Market " + " " + " www.amys-market.com" + " ----- " + " " + "CHECKOUT AT:" + " " + user_date + " " + " ----- " + " SUBTOTAL: " + "${0:.2f}".format(total_price) + " " + "TAX: " + "${0:.2f}".format(tax)+ " " + "TOTAL: "+ " " + "${0:.2f}".format(final_price) + "-----------" + " " + "THANK YOU, COME BACK SOON!" + "-----------"
content = Content("text/plain", message_text) #message delivered in plain text format
mail = Mail(from_email, subject, to_email, content)


response = sg.client.mail.send.post(request_body=mail.get())



pp = pprint.PrettyPrinter(indent=4)

print("----------------------")
print("EMAIL")
print("----------------------")
print("RESPONSE: ", type(response))
print("STATUS:", response.status_code) 
print("HEADERS:")
pp.pprint(dict(response.headers))
print("BODY:")
print(response.body) 


