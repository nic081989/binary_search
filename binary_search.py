# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: Recursive Binary Search
#
# NAME:        Nicholas Ngobi
# ASSIGNMENT:   Project 4: Sorting & Searching

# Write a recursive function `search` that
# takes an ordered array of numbers as a parameter
# and a number to search for and returns the index
# of the number in the array using binary, or -1 otherwise. For
# full credit, the search should be implemented using
# recursion, rather than a loop.

#high=None if high is not given when calling the function, then it defaults to none.
# In the function body if hign is None, it is set to the last index of the array.(len(array)-1) and this ensures the initial search
#search space covers the entire array. low =0 if low is not provided when calling the function, it defaults to 0 and this means that by default the initial search space starts
# starts from the beginning of the array.
# def binary_search(array, n , low=0,high=None):
#   if high is None:              # if high is not provided, set it to the last index of the array
#      high = len(array)-1        # high is set to the last index of the array
#   if low <= high:               #check if the search space is not empty
#      mid = (high + low ) // 2   #Calculate the middle index of the current search space.
#      if array[mid] == n: 
#          return mid
#      elif array[mid] < n:
#         low  = mid +1
#      else: 
#         high  = mid -1
def binary_search(array, target):
    low  = 0
    high = len(array) - 1
    while low <= high:
        mid = (high + low) // 2
        if array[mid]  == target:
            return mid
        elif array[mid]  <  target:
            low =  mid  +  1
        else:
            high = mid  -  1
    return -1
def main():
        
        array = [-1, 1, 3, 5, 7, 9,10]
        #result= binary_search(array,1)
        print("element is present at index",binary_search(array, 9) )
    

main()
