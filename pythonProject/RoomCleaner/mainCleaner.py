"""
The minimum number of cells can be n.
 It is the only answer possible as it need to have an element of type
 ‘.  ‘ in every different row and column. If particular column and a given row contain
  ‘*  ‘ in all the cells then, it is known that the house cannot be cleaned.
  Traverse every row and find the
  ‘.  ‘ that can be used for the machine.
   Use this step two times, check every column for every row and then check for every row for every column.
   Then check if any of the two gives answer as n. If yes then house can be cleaned otherwise not.
   This approach will give us the minimum answer required. In the first example the machine will clean cell (1, 1), (2, 1), (3, 1) in order to clean the entire room.
    In the second example every cell in the 1^{st}  row has ‘*  ‘ and every cell in 3^{rd}
 column contains ‘*  ‘, therefore the house cannot be cleaned. 1^{st}  row cannot be cleaned in any way.
 """

# house can be cleaned or not

# Matrix A stores the string
A = [[0 for i in range(105)] for j in range(105)]

# ans stores the pair of indices
# to be cleaned by the machine
ans = []


# Function for printing the
# vector of pair
def printt():
    print("Yes, the house can be cleaned.")
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])


# Function performing calculations
def solve(n):
    global ans

    # push every first cell in
    # each row containing '.'
    for i in range(n):
        for j in range(n):
            if (A[i][j] == '.'):
                ans.append([i + 1, j + 1])
                break

    # If total number of cells are
    # n then house can be cleaned
    if (len(ans) == n):
        printt()
        return 0

    ans = []

    # push every first cell in
    # each column containing '.'
    for i in range(n):
        for j in range(n):
            if (A[j][i] == '.'):
                ans.append([i + 1, j + 1])
                break

    # If total number of cells are
    # n then house can be cleaned
    if (len(ans) == n):
        printt()
        return 0
    print("house cannot be cleaned.")


# Driver function
n = 3
s = ""
s += ".**"
s += ".**"
s += ".**"
k = 0

# Loop to insert letters from
# string to array
for i in range(n):
    for j in range(n):
        A[i][j] = s[k]
        k += 1

solve(n)

# This code is contributed by shubhamsingh10