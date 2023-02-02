# Function #1: Write a Python function called max_num()to find the maximum of three numbers.

def max_num(int1,int2,int3):
    return max([int1,int2,int3])

print(max_num(22,51,76))

# Function #2: Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(list):
    total = 1

    if len(list) == 0:
        return 0
    elif len(list) == 1:
        return list[0]
    else:
        for x in list:
            total = total * x
    return total

print(mult_list([3,3,6,5]))

# Function #3: Write a Python function called rev_string() to reverse a string.

def rev_string(str):
    return ''.join(reversed(str))

print(f'Christopher in reverse is: {rev_string("Christopher")}')

# Function #4: Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(num,beg,end):
    return num in range(beg,end+1)

print(num_within(8,1,6))

# Function #5: Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# Default Triangle Values
triangle = [[1],[1,1]]
def pascal(int):
    if int < 1:
        print("Please choose more rows!")
    elif int == 1:
        print(triangle[0])
    else:
        row = 2
        # Create more rows
        while len(triangle) < int:
            curr_row = []
            prev_row = triangle[row - 1]
            length = len(prev_row)+1
            for i in range(length):
                if i == 0:
                    curr_row.append(1)
                elif i > 0 and i < length-1:
                    curr_row.append(triangle[row-1][i-1]+triangle[row-1][i])
                else:
                    curr_row.append(1)
            triangle.append(curr_row)
            row += 1

        for row in triangle:
            print(row)

pascal(8)