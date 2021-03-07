cars = ['bmw', 'tesla', 'ford']

print(len(cars))
print(cars)
print(cars[0])

# loops


for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.capitalize())


# while loops

number = 0

while number <= 10:
    print(number)
    number = number+1
else:
    print('the while loop has ended with the number '+ str(number) )

print("\n sets, they have no duplicates ")

number_sets ={1,1,1,1,2,2,2,3,3,3}
# order is not preservered 
print(number_sets)

print('\ndictionaries---') 
person ={
    'age': 20,
    'name': 'Bob',
    'address':"London"
}

for key in person:
    print(key)

print(person, person['age'])