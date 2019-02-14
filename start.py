import code

num = int(input('Give me a number!'))
code.single_row_stars(num)

code.rewrite(6)

print('Hello!')

day_number = code.today()
print('Today is ' +str(day_number) + ' in the month.')

a = input ('What is your name? ')

code.hello(a)

b = input('And how is your friend called? ')

code.hello2(a,b)

r = float(input('what is the radius?'))
z = code.circle_area(r)
print('the are is ' + str(z))



