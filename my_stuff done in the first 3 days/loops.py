import code

a_list= [1,2,3]
another_list = ['harry','ron', 'hermione']
yanother_list = [1, 'harry', 3.4, 'blue']

print(another_list[0])
print(len(another_list))

the_sum = code.my_sum(a_list)
print(the_sum)

the_prod = code.my_prod(a_list)
print(the_prod)

the_count = code.my_count(a_list)
print(the_count)

count_ones = code.my_count_ones(a_list)
print (count_ones)

the_max = code.my_max(a_list)
print(the_max)

for numbers in a_list:
    print (numbers)
    print ('years')

numbers = [12,3,12]

for n in numbers:
    z = n*2
    print(z)

total = 0
for n in numbers:
    total = n + total
print (total)

total = 1
for n in numbers:
    total = n * total
print(total)


print(code.get_filenames2('C:\\Users\\JRaimann\\Desktop\\pythoncode'))