# Ralston Ryan 
# Date: 19/05/2026

#Task 1

# Created a nested dictionary with the following information.
product_list = {
    "el2234" : { 
        "name" : "Head Phones", 
        "category" : "Electronics", 
        "price" : 19.99, 
        "quantity" : 2 
        },
    "sh9989" : {
        "name" : "Running Shoes",
        "category" : "Footwear", 
        "price" : 99.99, 
        "quantity" : 1 

    },
    "ap0098" : {
        "name" : "Smart Toaster",
        "category" : "Appliance", 
        "price" : 130.00, 
        "quantity" : 1

    },
    "cl3321" : {
        "name" : "Cotton Shirt",
        "category" : "Clothing", 
        "price" : 10.00, 
        "quantity" : 4
    },
    }



#Task 2

# Created a dictionary to hold the customer data
cus_dict = {
    'customername': "Hannah Davis",
    'loyaltytier' : 'Gold'
}

# Printed the message along with the customer name 'Hannah Davis' and her loyalty tier.
print(f"Processing Order for: {cus_dict['customername']} [{cus_dict['loyaltytier']} Tier Member]...")



#Task 3 

# Used to loop through each productin the dictionary
for product, info in product_list.items():

    # CalculatE the total by multiplying the price time the quantity.
    subtotal = info["price"] * info["quantity"]

    # Match-case for the discounts
    # Apply the discount based on the product category
    match info["category"]:
        case "Appliance":
            product_disc = 0.20
        case "Clothing":
            product_disc = 0.10
        case _:
            product_disc = 0

    # calculate the saled discount amount 
    sales_disc = subtotal * product_disc

    # Calculate the final product price.
    finalproduct_price = subtotal - sales_disc

    # Display the  product information. 
    print(f"\nProduct ID: {product}")
    print(f"Product Name: {info['name']}")
    print(f"Subtotal: ${subtotal}")
    print(f"Sales Discount: ${sales_disc}")
    print(f"Final Product Price: ${finalproduct_price}")


#Task 4

# The variable used to store the running total after the discounts.
total = 0

for product, info in product_list.items():

    # Calculate subtotal
    subtotal = info["price"] * info["quantity"]

    # Apply product discount based on category
    match info["category"]:
        case "Appliance":
            product_disc = 0.20
        case "Clothing":
            product_disc = 0.10
        case _:
            product_disc = 0

    # Calculate the discount and final product price
    sales_disc = subtotal * product_disc
    finalproduct_price = subtotal - sales_disc

    # Add the discounted price to running total
    total = total + finalproduct_price

# Print the total after sales discounts
print(f"\nTotal after the discounts applied: ${total}")

# Membership discount calculation if-statement.
if cus_dict["loyaltytier"] == "Platinum":
    member_discount_rate = 0.16
elif cus_dict["loyaltytier"] == "Gold":
    member_discount_rate = 0.11
elif cus_dict["loyaltytier"] == "Silver":
    member_discount_rate = 0.05
else:
    member_discount_rate = 0


membership_discount = total * member_discount_rate
final_owed = total - membership_discount

# Print the membership discount details
print(f"Membership Discount: ${membership_discount:.2f}")
print(f"Final Total Owed: ${final_owed:.2f}")