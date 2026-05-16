# Ralston Ryan, lab 2 

# Question 1

messy_menu = "    PizZA, burGER, SaLAd "

#a Used .strip to remove the white space.
removed_menu = messy_menu.strip()
print(removed_menu)

#b Used .lower to make sure that the whole string is lowercase
lower_case = removed_menu.lower()
print(lower_case)

#c Outputted the message along with the menu list.

print(f"Today’s special menu list: {lower_case}" )

# Question 2 

#a  Used list() and range() to create a list of even number from 2-50.
even_numList = list(range(2, 51, 2))

#b Used print() to display the numbers.
print(even_numList)

#c Used len() and print() to calculate and print the total number of items in the list.
total_items = len(even_numList)
print(total_items)

#d used sum() and print() to calcuate and print the sum of all numbers.
num_sum = sum(even_numList)
print(num_sum)

#e Used a constant multiplier.
MULTIPLIER = 5

max_num = max(even_numList)
min_num = min(even_numList)

calculation = MULTIPLIER * (max_num + min_num)
print(f"The product is: {calculation}")

# Question

#a  Used [] to creat a list with four names.
guest_list = ['Martin', 'David', 'Shanice', 'Riley']
print(guest_list)

#b Used .append to add the name Linus to the end of the list.
guest_list.append("Linus")
print(guest_list)

#c Used .insert(0) to insert Guido at the beginning of the list.
guest_list.insert(0, "Guido")
print(guest_list)

#d Used sort() to to sort the list alphabetically and permanently
guest_list.sort()
print(guest_list)

#e Created a new invitations list using list comprehension
invitations = [f"You are invited, {i.capitalize()}!" for i in guest_list]
print(invitations)

#f Used [:3] to print only the first three invitatioins.
print(invitations[:3])



