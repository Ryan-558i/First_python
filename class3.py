animals = ['dog', 'cat', 'cow', 'donkey', 'sheep']
if 'cow' in animals:
    print('moooo')

if 'pig' not in animals:
    print('no pigs found')


age = 17
if age >= 18: 
    print("You are eligible to vote")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!\n") 


toppings = ['mushrooms', 'green peppers', 'extra cheese']

for topping in toppings: 
    if topping =='green peppers':
        print("Sorry, we are out of green peppers right now")
    else:
        print(f"Adding {topping}.")
print("\nFinished making your pizza!")


status = 401
match status:
    case 400:
        print("Bad request")
    case 401 |403 |404:
        print("Not allowed")
    case 418:
        print("I'm a teapot")
    case _:
        print("Something's wrong with the teapot\n")


dict = { 
    'id':"rRyan",
    'first': 'Ralston',
    'last' : 'Ryan',
    'title' : 'Dr',
    'age' : 20,
    'married': False  
}

for k in dict: 
    print(k)

print(dict)
print(dict.items())
print(dict.keys())
print(dict.values())

for key, value in dict.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for key in dict.keys():
    print(f"\nKey: {key}")

for value in dict.values():
    print(f"Value: {value}")