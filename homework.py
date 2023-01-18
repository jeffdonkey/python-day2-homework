# Write a Python function called max_num()to find the Max of three numbers.

def max_num(a,b,c):
  return max([a,b,c])

print(max_num(12,1259,2))

    # 'max' is a built-in function for python
    # line 6 print function is sending the numbers to the function 'max_num'
    # line 4 return calls the 'max' function with the arguments from 'max_num'

# -------------------------------------------------------------------------------------

# Write a Python function called mult_list()  to multiply all the numbers in a list.
def mult_list(lst):  
  if len(lst) == 0:
    return 0 
  prod = lst[0]  
  if len(lst) > 1:
    for i in lst[1:]:
      prod = prod * i

  return prod
    
print(mult_list([1,2,3,10]))


    # lines 16-17 checks the list sent to the function 'mult_list'.
        # if the list is empty it's length is zero.  When the length is zero a zero is returned
    # line 18 is setting the variable 'prod' to '1st[0]'. '1st[0]' is the number from the list
        # at index[0].
    # line 19 checks the list to see if it's length is greater than 1.
        # if the list only has one number inside then the value of 'prod' is the number passed 
        # into 'mult_list'.  If the length is greater than 1 th for loop runs on lines 20-21
    # line 20 iterates over the list starting with index[1].  The part of line 20 'lst[1:]' is
        # saying to start the iteration at index[1] and continue until the end of the list.
        # it is written this way so the programmer does not have to specify the last index
        # of the list
    # line 21 takes the inital value of 'prod' (in this case, 1) and then multiplies 'prod' by
        # the value of lst[1] (2).  The result is 2.  The value of 'prod' is now 2.
        # When the loop runs again the vale of 'prod' (2) is now multiplied by the value of
        # lst[2] (3).  The result is 6. the value of 'prod' is now 6.
        # loop runs again multiplying 'prod' (6) by the value of lst[3] (10).  'prod' is now 10.
        # list has been iterated through so the loop stops that prod is returned

#---------------------------------------------------------------------------------------------------

# Write a Python function called rev_string() to reverse a string.

def rev_string(my_str):
  return my_str[::-1]

print(rev_string(""))
print(rev_string("apple"))
print(rev_string("mt string"))

    # line 51 '...[::-1]' is slicing the string.  The '::' is stating to slice the value received from
        # the beginning to the end.  The '-1" then reversing the order one at a time.  If '-2'
        # was using instead of '-1' then the retruned value would be every-other character
        # in the initial string in reverse order.

#------------------------------------------------------------------------------------------------

# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(x,a,b):
  return x in range(a,b+1)
     
print(num_within(3,2,4))     
print(num_within(3,1,3))     
print(num_within(10,2,5))

    # This function is checking a list to see if the first number is the list is within the range of the 
        # next two numbers of a list.
    # True or False is returned.
    # note line 62 '...range(a,b+1)'.  'b+1' is used so that if the value of x is equal to the last number of the
        # range (value b) then x will be considered within range.
        # If line 62 was written '...range(a,b)' then when x is equal to b it would not be in range.

#--------------------------------------------------------------------------------------------------------------------------

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)

    # much math, very wow