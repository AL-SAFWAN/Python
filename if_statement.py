is_adult = True
age= 18

# you need to have correct indentation 
# for the if statement to function correctly
# or you will get a indentation error 

if is_adult: 
    print('is adult')

if age > 18:
    print('adult')
elif age == 18:
    print("is 18")
else:
    print("not an adult")

# ternary opperator 
message = 'adult' if age>=18 else 'not an adult'
print(message)


# logical opperators -> and or not=
