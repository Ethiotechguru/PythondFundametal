# # ***************************************************************************************
# # string
gross_income = 200
tax_rate = 0.1
tax_paid = gross_income*tax_rate
net_income = gross_income - tax_paid

# # ***************************************************************************************
# # list
my_list = [1,2,3]
new_list = ['sam', '34', 90]
added_list =my_list  + new_list
added_list.append('2000')
# # Dictionary
# name = 'name'
my_dictionary = {"name":'Alex', "age":23}

print(my_dictionary.items())
# # ***************************************************************************************
# # Tuples
my_tuples = ('a', 'b', 'c', 'a', [1, 5])

print(my_tuples[4][0])

# # Sets
my_set = set([1,2,3])
my_set.add(2)
my_set.add(6)
my_set.add(6)
print(my_set)

# #*Boolean***********************************************************************************
num_list = [5,1,7,3,8,3]
num_list.sort()
num_list.reverse()
str_list = ['sam', 'age', 'tum', 'chala', 'meles']
print(num_list)
str_list.sort()
print(str_list)
print(type(35) == type(3))
l_one = [4,2*3]
l_two = [2*2,6]
l_three = l_two
print(3==3 and 3==9/3)
# # ***************************************************************************************
# # STATEMENT
# # name = ''
age = 20
if name and age > 21:
    print('hello ' + name + ' you can drink')
elif name and age < 21:
    print('hello ' + name + ' sorry you can\'t enter')
else:
    print('sorry unknown person you are to young and don\'t have an Id')


# # ***************************************************************************************
# # FOR LOOP

list_of_num = [2,4,7,8,9,9]
even_sum = 0
odd_sum = 0
for p in list_of_num:
    if p%2==0:
        even_sum = even_sum + p
        print(f'{p} is even')
    else:
        odd_sum = odd_sum + p
        print(f'{p} is odd')

myString = 'Hello Africa'
v_letter = ''
c_letter = ''
for letter in myString:
    if(letter == 'a' or letter == 'e' or letter == 'o' or letter == 'i' or letter == 'A'):
        v_letter = v_letter + letter
    elif letter == ' ':
        print('there is nothing at this index')
    else:
        c_letter = c_letter + letter
print(v_letter)
print(c_letter)

my_list2 = [(1,2), (3,4), (5,6), (7,8)]
for item in my_list2:
    print(item[1])

d = {'k1':1, 'k2':2, 'k3':3}
for k, v in d.items():
    print(v)

# # ******************************************************************************************
# # WHILE LOOPS

x = 10
while x<4:
    print(f'the value is {x}')
    x += 1
else:
    print('x is not less than 4')
myString = 'EJIGAYEHUSHIBABAW'
myList = []

for lett in myString:
    myList.append(lett)
print(myList)
myList = [lett for lett in myString]
print(myList)
myList = [let for let in myString]

print(myList)
sqr = []
listNum = [num for num in range(0, 11)]
for numb in listNum:
    sqr.append(numb**2)

myWord = 'sammy'
my_wordAnd_myNum = [w for w in myWord]
print(my_wordAnd_myNum)

for num in range(0,101):
    if num%3==0 and num%5==0:
        print('FizBuzz is multiple of both 3 and 5')
    elif num%3 == 0:
        print('Fizz is multiple of 3 only')
    elif num%5 == 0:
        print('Buzz is multiple of 5')
    else:
        print(num)
# # ******************************************************************************************
# # ******************************************************************************************
even_num = []
def add(n):
    for num in n:
        if num%2==0:
            even_num.append(num)
        else:
            pass
    return even_num
    
result = add(6, 6)
print(add([3,2,8,6,5,9,20,23,46]))

work_hours = [('sam', 500), ('alex',350), ('Jhon',400)]
def employee_of_the_month():
    max_hours = 0
    employeeName = ''
    for a,b in work_hours:
        if(b>max_hours):
            max_hours = b
            employeeName = a
        else:
            pass
    return (employeeName, max_hours)
name, hours = employee_of_the_month()
print(name, hours)

def sum(*args):
    added = 0
    for a in args:
        added = added+a
    return added

def myfunc(*args):
    return sum(*args)*0.05

# print(myfunc(40, 60, 60, 70, 70))
def fruit_args(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print(kwargs['fruit'])
fruit_args(fruit='apple', veggies='lettuce')
def myfunc(**kwargs):
    sum = 0
    for a,b in kwargs.items():
        sum = sum+b
    return sum

def myfunc(*args):
    my_list = []
    for a in args:
        if a%2 == 0:
            my_list.append(a)
    return my_list
print(myfunc(2, 3, 4,6,8,7,5))

my_name = 'samuel'
return 'SaMuEl
maching_string = ''
for i in range(0, len(my_name)):
    if(i%2==0):
        maching_string = maching_string+my_name[i].upper()
    else:
        maching_string = maching_string+my_name[i].lower()
print(maching_string)

print(my_name.index())
# # ************************************************************************************
# # Function that return the lesser Number if both arguments are even 
# # or
# # returns the greater if either of the number are Odd
def lesser_of_two_even(a,b):
    if(a%2 == 0 and b%2==0):
        return min(a, b)
    else:
        return max(a, b)

print(lesser_of_two_even(20,2))

def animal_crackers(word1, word2):
    return word1[0].lower()==word2[0].lower()
    
print(animal_crackers('Samule', 'senait'))
# # *************************************************************************************
# # check either argument is 20 or the sum of the arguments is 20
def check_twenty(a, b):
    return a == 20 or b==20 or a+b == 20

print(check_twenty(10,9))
# # *******************************************************************************************
# # capitalize the first letter of the argument and the 4th letter of the argument

def capital(word):
    result = ''
    for i in range(0, len(word)):
        if(i==0 or i==3):
            result = result+word[i].upper()
        else:
            result = result+word[i]
    return result
    first_half = word[:3]
    second_half = word[3:]
    return first_half.capitalize() + second_half.capitalize()
print(capital('macdonal'))

def word_reversed(word):
    wordList = word.split()
    wordList = wordList[::-1]
    return ' '.join(wordList)
print(word_reversed('helen befekadu tamirat urgesa'))

print(''.join(['a', 'b', 'c','d', 'e','f']))
# # ***********************************************************************************
# # write a function that checks if list contain the number 3 in consecutive order
def myfunc(arr):
    for i in range(0, len(arr)-1):
        if(arr[i]==3 and arr[i+1]==3):
            print(i, i+1)
            return True
    return False
print(myfunc([2,4,4,3,6,3,3,4,6,9,3,8,3]))#return True

def add_three_char_for_each_char(word):
    modifid_word = ''
    for char in word:
        modifid_word+=char*3
    return modifid_word
print(add_three_char_for_each_char('samuel'))

def black_jack(a, b, c):
    sum = a+b+c
    if(sum <= 21):
        return sum
    elif(sum>21 and (a==11 or b==11 or c ==11)):
        if(sum-10>21):
            return 'Bust'
        else:
            return sum -10
    else:
        return 'Bust'
print(black_jack(5,6,7))

def myfunc(list_of_num):
    code = [0,0,7]
    for num in list_of_num:
        if len(code) == 0:
            break
        elif code[0] == num:
            print(num)
            code.pop()
        else:
            pass
    print(code)
myfunc([1,0,3,0,7,7])

def find_con_num(my_list):
    j=0
    for i in range(0, len(my_list)):
        j = i+1
        if my_list[i] == my_list[i+1]:
            print(my_list[i+1])
            return True
    print(my_list[j])
    return False

print(find_con_num([1,2,1,5,6,8]))

print(len([])==0)
upper_count = 0
def count_upper_lower(text):
    for letter in text:
        print(letter)
    return upper_count
print(count_upper_lower('Samuel'))

arr = [2,5,4,7,6,9,8,11]
def multiply_by_givenNum(a):
    return a%2==0
print(list(reduce(multiply_by_givenNum, arr)))

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total = total + num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

print(summer_69([1,3,5, 6, 6,6, 9, 9]))

def check_for_given_num(nums):
    code = [0,0,7]
    repeated_morethan_three_times = []
    for i in range(0, len(nums)-2):
        if nums[i] == nums[i+1] and nums[i] == nums[i+2]:
            print(nums[i]) #(2), [4], [10]
            repeated_morethan_three_times.append(nums[i])
        else:
            pass
    for n in repeated_morethan_three_times:
        print(f'{n} is repeated three times in {nums}')

print(check_for_given_num([3,3,3,7,7,7,5,0,2,6,7, 9, 9, 9]))

def multiple_of_num_in_range(num, ran):
    result = []
    while ran >= 1:
        result.append(num*ran)
        ran = ran -1
    return result

print(multiple_of_num_in_range(3,5))

def func(l):
    div_by_two = []
    for n in l:
        tr = n*3
        if tr%2 == 0:
            div_by_two.append(tr)
    return div_by_two
print(list(filter(func, [2,3,4,5,6,7,8,9])))
print(func([2,3,4,5,6,7,8,9]))
fl = lambda n:n%2 == 0
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18]
print(list(map(lambda n:n%2 == 0, nums)))
import math
x = [50,80]
def findX():
    def isChangedX():
        x[0]=500
        print(x[0])
    isChangedX()
    x = 100
    print(x[0])
    
def vol(rad):
    return 4/3*math.pi*rad**3
print(vol(2))
# #******************************************************************************
# #COUNT LOWER CASE AND UPPER CASE IN A GIVEN STRING
def is_upper(text):
    count ={'countUpper': 0, 'countLower': 0}
    for l in text:
        if(l.isupper()):
            count['countUpper'] += 1
        elif(l.islower()):
            count['countLower'] += 1

    print(count)   
is_upper('Samuel Tamiru Kirkos')
def in_range(num, low, high):
    print(high+1)
    return num in range(low, high+1)

print(in_range(9,2,9))
print(in_range(5,4,5))
print(is_upper('Sam Chala kebede'))

# #********************************************************************************
# #RETURN A UNIQUE SET OF A GIVEN LIST

def unique(lists):
    return set(lists)

p = print(unique([1,2,1,2,3,1,4,5,1,3,5,6]))
print(len(p))
print(len(p))

def unique_list(lists):
    unique_val = []
    for num in lists:
        if num not in unique_val:
            unique_val.append(num)
    return unique_val

print(unique_list([1,2,1,2,3,1,4,5,1,3,5,6]))

def multiply(nums):
    total = 1
    for num in nums:
        total = total*num
    return total
print(multiply([2,4,6,7,8]))

def palindrome(s):
    s = s.replace(' ', '').lower()
    return s == s[::-1]

print(palindrome('My gym'))

obj = {'name':'samuel', 'age':23}
obj2 = {'name':'samuel', 'age':23}
obj['name'] = 'Lidet'
obj3 = obj
obj3['age']= 54
print(obj2==obj3)


def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('player1: choose X or Y').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
player1_marker, player2_marker = player_input()

print(player1_marker, player2_marker)
my_list = []
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        my_list.append(self.__dict__)
sam = Person(name='samuel', age=23)
sam.greet()
lidet = Person('Lidet', 12)
lidet.greet()
mihiret = Person('Mihiret', 18)
mihiret.greet()
def filter_it(a):
    return a['age']>=18
age_qualified =filter(lambda x:x['name']=='samuel', my_list)
print(list(age_qualified))

class Cylinder():
    def __init__(self, height, radius=1):
        self.height = height
        self.radius = radius
    def volume(self):
        return self.height*math.pi*(self.radius)**2
    def surface_area(self):
        return (2*math.pi*self.radius*self.height)+(2*math.pi*self.radius**2)

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())

class Line():
    def __init__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2
    def distance(self):
        x1,y1 = self.coord1
        x2, y2 = self.coord2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    def slop(self):
        x1,y1 = self.coord1
        x2, y2 = self.coord2
        return (y2-y1)/(x2-x1)
 
my_line = Line((3,2),(8, 10))
print(my_line.distance())
print(my_line.slop())

accout_holders = []
class Account():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.save()
    def save(self):
        accout_holders.append(self.__dict__)
        print(accout_holders)
    def deposit(self,amount):
        self.balance = self.balance + amount
        print('deposit accepted')
        print(self.balance)
    def withdrawal(self,amount):
        if(self.balance<amount):
            print('not enough fund available to withdraw')
        else:
            self.balance = self.balance - amount
            print(f'you withdraw ${amount}')
            print(self.balance)
    def fetch():
        rich_person = filter(lambda x:x['balance']>1000, accout_holders)
        return rich_person
jose = Account('Jose', 200)
jose.deposit(50)
jose.withdrawal(75)

under_1000 = filter(lambda x:x['balance']>1500, accout_holders)
print(accout_holders)
print(Account.fetch())
try:
    print('hello word')
except:
    print('no file found')
finally:
    print('I am here to stay')

class Card():
    def __init__(self, )

arr = [x for x in range(1000) if x%3==0]
print('All Numbers')
print(arr)

