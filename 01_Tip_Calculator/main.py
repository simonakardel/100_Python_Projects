# This is a simple tip calculator
total = float(input('Enter the total amount of the bill :\n$'))
people = int(input('Enter the number of people splitting the bill:\n'))
tip = int(input('Enter the tip percentage:\n%'))

amount = round((total/people) * ((tip + 100)/100), 2)
print(f'Each person should pay ${amount}')
