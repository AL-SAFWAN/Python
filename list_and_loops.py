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
