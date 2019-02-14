import math
import datetime
import os

def hello(a_name):
	print ('Hello '+a_name)

def hello2(a_name, b_name):
	print ('Hello ' +a_name+' and '+b_name+'!')

def sum_two(x,y):
	z=x+y
	return z

def circle_area(radius):
	area = radius**2*math.pi
	return area

def today ():
	now = datetime.datetime.now()
	return now.day

def my_sum(a_list):
	total = 0
	for n in a_list:
		total = n + total
	return total

def my_prod(a_list):
	total = 1
	for n in a_list:
		total = n * total
	return total

def my_count(a_list):
	count = 0
	for n in a_list:
		count = count + 1
	return count

def my_count_less_5(a_list):
	count = 0
	for n in a_list:
		if n < 5:
			count = count + 1
	return count

def my_count_ones(a_list):
	count = 0
	for n in a_list:
		if n == 1:
			count = count + 1
	return count

def my_max(a_list):
	if is_list_empty(a_list):
		return None
	count = a_list[0]
	for n in a_list:
		if n > count:
			count = n
	return count

def is_list_empty(a_list):
	if my_count(a_list) == 0:
		return True
	else:
		return False		



def get_filenames2(a_dirname):
	list_of_files = os.listdir(a_dirname)
	print('list of file names: ')
	print(list_of_files)
	print('--------------------')
	all_files = []
	for filename in list_of_files:
		full_path = os.path.join(a_dirname,filename)
		if not os.path.isdir(full_path): #if the file is a dir we skip it
			all_files.append(full_path)
	return all_files

def flatten(a_list_with_lists): #[12, 34, [56, 67]] --> [12, 34, 56, 67]
	new_list = []
	for n in a_list_with_lists:
		if isinstance(n,list): #is it a list? Yes --> add the numbers in the list n
			for i in n: #now n is our list
				new_list.append(i)
		else: #is it a list? No, just a number --> add it
			new_list.append(n)
	return new_list


#[12, 34, [56, 67], 78] -->
#12
#34
#5667
#78
a_list_with_lists = [12, 34, [56, 67], 78]

def print_right(a_list_with_lists):
    for n in a_list_with_lists:
        if isinstance(n,list): #is it a list? Yes --> add the numbers in the list n
            for i in n: #now n is our list
                print(i, end='')
            print('')
        else: #is it a list? No, just a number --> add it
            print(n)

#single_row_stars(4) --> ****

def single_row_stars (number):
    for n in range(number):
        print('*',end ='')
    print()

code.single_row_stars(4)

def rewrite(mnumber):
	for each in range(mnumber):
		print('*',end="")
	print("")

#single_row_stars(4, "-+") --> -+-+-+
#single_row_stars(4) --> ****

def single_row_stars_of (number,string):
	for n in range(number):
		print(string, end='')
	print('')

#square_of_stars(4)
#->
#****
#****
#****
#****

def square_of_stars(number):
    for n in range(number):
        for each in range(number):
            print('*', end='')
        print()

def rectangle_of_stars(rows,cols):
    for n in range(rows):
        for each in range(cols):
            print('*', end='')
        print()

#list_by_2([1,2,3]) --> [2,4,6]
a_list = [1,2,3]

def list_by_2(a_list):
    new_list = []
    for n in a_list:
        new_list.append(n*2)
    return new_list #or just print(new_list)

#create_grid(4)
#[['-','-','-','-'],['-','-','-','-'],['-','-','-','-'],['-','-','-','-']]

def create_grid(size):
    new_grid = []
    for row in range(size):
        new_list = []
        for column in range(size):
            new_list.append('-')
        new_grid.append(new_list)
    return new_grid


#change the content of list
a = ['x','y','z','b']

for i in range(len(a)):
	a[i] = 'rrr'

#is_duplicate_there([1,2,3], [4,5,1]) --> True
#is_duplicate_there([1,2,3], [4,5,6]) --> False

list_a = [1,2,3]
list_b = [4,5,1]

def is_duplicate_there(list_a, list_b):
    counter = 0
    for n in list_a:
        for m in list_b:
            if n==m:
                counter = counter + 1
            else:
                pass
    if counter != 0:
        print ('True')
    else:
        print('False')

is_duplicate_there(list_a, list_b)

def is_duplicate_there2(list_a, list_b):
    for n in list_a:
        for m in list_b:
            if n==m:
                return True
	return False

def is_duplicate_there2(list_a, list_b):
    for n in list_a:
        if (n in list_b):
            return True
	return False


