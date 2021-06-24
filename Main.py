from Board import gen_board, print_board, get_Sol_Len
from BnB_Search import BnB_Search
import time

# --------------------------------------------------------------
# Generating N  puzzles
# --------------------------------------------------------------
# This method keeps creating new boards until
# the list of puzzles reach a number of given count
def generate_n_puzzles(N):
    unique_puzzles = [] * N
    counter = 0
    temp = 1
    while temp > 0:
        board = gen_board()

        # Check if current created board is created 
        # and added to our list of boards before
        if board not in unique_puzzles:
            unique_puzzles.append(board)
            counter += 1
            if (counter == N):
                temp = -1

    return unique_puzzles

# --------------------------------------------------------------
# MAIN
# --------------------------------------------------------------
"""
    The program will solve 25 puzzles. The number of puzzles can be changed right under here. "N = 25"
    If a state takes too long to solve consider waiting for it for about a few minutes. All puzzles are solveable
    and 2 sample outputs are attached below this main class. 


    It iterates through the tree, finds all possible moves from the current node, and checks for loops,
    and same destinations dynamically. If the parent of two same states are equal, then it is considered a loop
    and if the two states are equal but have different parents, then it is considered that one of them should be removed
    from the tree, regarding their costs. The one with the higher cost is not considered again.

    Once a state has been added to the tree. We keep checking other nodes and kepe repeating until we have a big tree structure.
    The program always finds the most efficient path to solution.

    When the puzzle has been solved we print the 2 first puzzles' sequence both in text and graphical puzzles, and print the rest
    in text sequence. The nodes generated to find the path are also printed to get a sense of the time took to solve them afterwards.

    After successfully solving all puzzles, A simple "graph" is printed out. Since we had to print the graph in the output prompt,
    we print using simple texts, The x axis is for states such as; S1, S2, etc... And Y axis is considered the number of moves for each puzzle
"""


# define a number of unique puzzles wanted
N = 25

# Now create them and add them into boards_arr
boards_arr = generate_n_puzzles(N)

# print all the boards
for i in range (N):
    print("Board S{:d}: \n".format(i+1))
    print_board(boards_arr[i])
    print("\n\n")

# Solution lengths for each puzzle
# Define an array of size N
sol_data = [1]*N

# Loop search BnB dynamic
for k in range (N):
    print("For board S{:d}: \n".format(k+1))
    BnB_Search(boards_arr[k])
    sol_data[k] = get_Sol_Len()
    print("\n\n\n")

sum = 0
for i in range (N):
    sum = sum + sol_data[i]

# This calculation divides total moves to puzzle size and rounds it to
# 3 decimal places. If the result has 2 decimal places that is because
# the division is perfect to 2 decimals
avg = float("{0:.3f}".format(sum / N))

# Print "graph"
# x axis is state names
# y axis number of moves
for i in range(N):
    print("|\t",sol_data[i],end="")
print("\t",avg,end="")
print("|")
print("|")
print("|")
print("|")
print("|___________________________________________________________________")
for i in range (N):
    print("\tS{:d}".format(i+1),end="")

# lastly add average to the end state name
print("\tAvg",end="")
print()






# EXAMPLE OUTPUT 
# -------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------
"""
Board S1: 

1 2 3 4
2 3 4 5
3 4 5 _
4 5 5 5



Board S2:

1 2 4 5
2 3 3 5
3 _ 5 4
4 4 5 5



Board S3:

1 2 3 4
3 2 4 5
_ 3 4 5
4 5 5 5



Board S4:

1 2 3 4
3 _ 4 5
2 3 4 5 
4 5 5 5



Board S5:

_ 2 3 4
1 3 4 5
2 4 5 5
3 4 5 5



Board S6:

1 _ 2 3
2 3 4 4
3 4 5 5
4 5 5 5



Board S7:

1 2 3 4
2 3 4 5
3 5 5 _
4 4 5 5



Board S8:

1 2 3 4
2 4 3 4 
3 5 5 5
4 5 _ 5



Board S9:

1 2 3 4
2 4 3 5
3 _ 4 5
4 5 5 5



Board S10:

1 2 3 4
2 3 4 5
3 4 5 5
4 _ 5 5



Board S11:

1 2 3 4
2 3 4 5
3 4 5 5
4 5 5 _



Board S12:

1 2 3 4
2 4 _ 5
3 3 5 5 
4 4 5 5



Board S13:

1 2 3 4
2 3 4 5
3 5 5 5
4 4 _ 5



Board S14:

1 2 3 4
2 3 5 4
3 4 _ 5
4 5 5 5



Board S15:

1 2 3 4
2 3 _ 4
3 4 5 5
4 5 5 5 



Board S16:

1 2 3 4
2 4 3 4
3 _ 5 5
4 5 5 5



Board S17:

1 2 3 4
2 3 4 5
3 _ 4 5
4 5 5 5



Board S18:

1 2 3 4
2 _ 4 5
4 3 5 5
4 3 5 5



Board S19:

1 _ 3 4
3 2 4 5
2 3 4 5
4 5 5 5



Board S20:

1 2 3 4
2 3 4 5
3 4 5 5
4 5 _ 5 



Board S21:

1 2 3 4
2 _ 3 5
3 4 5 4
4 5 5 5



Board S22:

1 2 3 4
2 3 4 5
3 _ 5 5
4 4 5 5



Board S23:

1 2 3 4
2 _ 4 5
3 3 5 5
4 4 5 5



Board S24:

1 2 3 4 
2 4 3 5 
_ 3 4 5
4 5 5 5



Board S25:

1 2 3 4
2 _ 4 5
4 3 5 5
3 4 5 5 



For board S1:

1
Solution found!
Solution Length:  1
1 2 3 4
2 3 4 5
3 4 5 _
4 5 5 5
Move 0:  Empty tile moved:  start

1 2 3 4
2 3 4 5
3 4 5 5 
4 5 5 _
Move 1:  Empty tile moved:  down

Total nodes generated: 1
Loop break...




For board S2:

11
Solution found!
Solution Length:  11
1 2 4 5
2 3 3 5
3 _ 5 4
4 4 5 5
Move 0:  Empty tile moved:  start

1 2 4 5
2 3 3 5
3 4 5 4
4 _ 5 5
Move 1:  Empty tile moved:  down

1 2 4 5
2 3 3 5
3 4 5 4
4 5 _ 5
Move 2:  Empty tile moved:  right

1 2 4 5
2 3 3 5
3 4 _ 4
4 5 5 5
Move 3:  Empty tile moved:  up

1 2 4 5
2 3 3 5
3 4 4 _ 
4 5 5 5
Move 4:  Empty tile moved:  right

1 2 4 5
2 3 3 _
3 4 4 5
4 5 5 5
Move 5:  Empty tile moved:  up

1 2 4 _
2 3 3 5
3 4 4 5
4 5 5 5
Move 6:  Empty tile moved:  up

1 2 _ 4
2 3 3 5
3 4 4 5
4 5 5 5
Move 7:  Empty tile moved:  left

1 2 3 4
2 3 _ 5
3 4 4 5
4 5 5 5
Move 8:  Empty tile moved:  down

1 2 3 4
2 3 4 5
3 4 _ 5
4 5 5 5
Move 9:  Empty tile moved:  down

1 2 3 4
2 3 4 5
3 4 5 _
4 5 5 5
Move 10:  Empty tile moved:  right

1 2 3 4
2 3 4 5
3 4 5 5
4 5 5 _
Move 11:  Empty tile moved:  down

Total nodes generated: 7780
Solution Path ['start', 'down', 'right', 'up', 'right', 'up', 'up', 'left', 'down', 'down', 'right', 'down', 'goal']
Total nodes generated: 7780
Loop break...




For board S3:

6
Solution found!
Solution Length:  6
Solution Path ['start', 'up', 'right', 'down', 'right', 'right', 'down', 'goal']
Total nodes generated: 172
Loop break...




For board S4:

12
Solution found!
Solution Length:  12
Solution Path ['start', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'right', 'right', 'down', 'goal']
Total nodes generated: 16298
Loop break...




For board S5:

6
Solution found!
Solution Length:  6
Solution Path ['start', 'down', 'down', 'down', 'right', 'right', 'right', 'goal']
Total nodes generated: 167
Loop break...




For board S6:

13
Solution found!
Solution Length:  13
Solution Path ['start', 'down', 'right', 'down', 'left', 'up', 'up', 'right', 'right', 'down', 'left', 'down', 'right', 'down', 'goal']
Total nodes generated: 31623
Loop break...




For board S7:

5
Solution found!
Solution Length:  5
Solution Path ['start', 'left', 'left', 'down', 'right', 'right', 'goal']
Total nodes generated: 50
Loop break...




For board S8:

7
Solution found!
Solution Length:  7
Solution Path ['start', 'up', 'left', 'up', 'right', 'right', 'down', 'down', 'goal']
Total nodes generated: 233
Loop break...




For board S9:

5
Solution found!
Solution Length:  5
Solution Path ['start', 'up', 'right', 'down', 'right', 'down', 'goal']
Total nodes generated: 100
Loop break...




For board S10:

2
Solution found!
Solution Length:  2
Solution Path ['start', 'right', 'right', 'goal']
Total nodes generated: 3
Loop break...




For board S11:

Solution found!
Solution Length:  0
Solution Path []
Total nodes generated: 0
0
Solution found!
Solution Length:  0
Solution Path ['start', 'goal']
Total nodes generated: 3
Loop break...




For board S12:

13
Solution found!
Solution Length:  13
Solution Path ['start', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left', 'down', 'right', 'right', 'goal']
Total nodes generated: 37289
Loop break...




For board S13:

5
Solution found!
Solution Length:  5
Solution Path ['start', 'up', 'left', 'down', 'right', 'right', 'goal']
Total nodes generated: 54
Loop break...




For board S14:

4
Solution found!
Solution Length:  4
Solution Path ['start', 'up', 'right', 'down', 'down', 'goal']
Total nodes generated: 50
Loop break...




For board S15:

11
Solution found!
Solution Length:  11
Solution Path ['start', 'down', 'right', 'up', 'left', 'down', 'right', 'up', 'left', 'down', 'right', 'down', 'goal']
Total nodes generated: 10844
Loop break...




For board S16:

5
Solution found!
Solution Length:  5
Solution Path ['start', 'up', 'right', 'right', 'down', 'down', 'goal']
Total nodes generated: 75
Loop break...




For board S17:

11
Solution found!
Solution Length:  11
Solution Path ['start', 'down', 'right', 'up', 'left', 'down', 'right', 'up', 'left', 'down', 'right', 'right', 'goal']
Total nodes generated: 7085
Loop break...




For board S18:

8
Solution found!
Solution Length:  8
Solution Path ['start', 'down', 'down', 'left', 'up', 'right', 'down', 'right', 'right', 'goal']
Total nodes generated: 1012
Loop break...




For board S19:

7
Solution found!
Solution Length:  7
Solution Path ['start', 'down', 'left', 'down', 'right', 'right', 'right', 'down', 'goal']
Total nodes generated: 271
Loop break...




For board S20:

1
Solution found!
Solution Length:  1
Solution Path ['start', 'right', 'goal']
Total nodes generated: 1
Loop break...




For board S21:

12
Solution found!
Solution Length:  12
Solution Path ['start', 'down', 'right', 'right', 'down', 'left', 'left', 'up', 'up', 'right', 'down', 'right', 'down', 'goal']
Total nodes generated: 15019
Loop break...




For board S22:

3
Solution found!
Solution Length:  3
Solution Path ['start', 'down', 'right', 'right', 'goal']
Total nodes generated: 11
Loop break...




For board S23:

4
Solution found!
Solution Length:  4
Solution Path ['start', 'down', 'down', 'right', 'right', 'goal']
Total nodes generated: 46
Loop break...




For board S24:

14
Solution found!
Solution Length:  14
Solution Path ['start', 'down', 'right', 'up', 'up', 'right', 'down', 'left', 'down', 'left', 'up', 'right', 'right', 'right', 'down', 'goal']
Total nodes generated: 52042
Loop break...




For board S25:

6
Solution found!
Solution Length:  6
Solution Path ['start', 'down', 'left', 'down', 'right', 'right', 'right', 'goal']
Total nodes generated: 161
Loop break...




|         1       11      6       12      6       13      5       7       5       2       0       13      5       4       11      5       11      8       7       1       12      3       4       14      6        6.88
|
|
|
|
|___________________________________________________________________
        S1      S2      S3      S4      S5      S6      S7      S8      S9      S10     S11     S12     S13     S14     S15     S16     S17     S18     S19     S20     S21     S22     S23     S24     S25      Avg


"""

# SECOND SAMPLE OUTPUT
# 
"""
Board S1: 

1 2 3 4
2 3 4 5
3 4 5 5
4 5 5 _



Board S2:

1 2 3 4
2 3 4 _
3 4 5 5
4 5 5 5



Board S3:

1 2 4 _
2 3 3 4
3 4 5 5
4 5 5 5



Board S4:

1 2 _ 3
2 3 4 4
3 4 5 5
4 5 5 5



Board S5:

1 _ 2 4
2 3 3 5
3 4 4 5
4 5 5 5



Board S6:

1 2 3 4
2 3 4 5
3 4 5 5
4 5 _ 5



Board S7:

2 1 2 4 
_ 3 3 4
3 4 5 5
4 5 5 5



Board S8:

1 2 3 4
3 2 4 5
3 _ 4 5
4 5 5 5



Board S9:

1 2 3 4
3 2 4 5
4 3 5 5
4 5 _ 5



Board S10: 

_ 1 2 4
2 3 3 5
3 4 4 5
4 5 5 5



Board S11:

1 2 3 4
2 3 4 5
3 4 _ 5
4 5 5 5



Board S12:

1 2 3 4
2 _ 4 5
4 3 5 5
3 4 5 5



Board S13:

1 2 3 4
2 3 4 5
3 4 5 5
4 _ 5 5



Board S14:

1 2 3 4
2 3 4 5
4 _ 5 5
3 4 5 5



Board S15:

1 2 3 4
2 3 4 5
3 5 4 5
4 _ 5 5



Board S16:

1 2 3 4
2 3 4 5
3 4 5 _
4 5 5 5



Board S17:

1 2 4 3
2 3 5 4 
3 4 _ 5
4 5 5 5



Board S18:

1 2 3 4
2 3 4 5
3 5 4 5
4 5 5 _



Board S19:

1 2 3 4
2 3 4 5
4 3 5 5
_ 4 5 5



Board S20:

1 2 3 4
2 3 4 5
3 _ 4 5
4 5 5 5



Board S21:

1 2 3 4 
2 _ 3 5
3 4 4 5
4 5 5 5



Board S22:

1 2 3 4
2 5 3 5
3 4 _ 5
4 4 5 5



Board S23:

1 2 3 _
2 3 4 4
3 4 5 5
4 5 5 5



Board S24:

1 2 3 4
2 4 3 5
3 _ 4 5
4 5 5 5



Board S25:

1 2 3 4
_ 3 4 5
2 3 4 5
4 5 5 5



For board S1:

Solution found!
Solution Length:  0
Total nodes generated: 0
0
Solution found!
Solution Length:  0
1 2 3 4
2 3 4 5
3 4 5 5
4 5 5 _
Move 0:  Empty tile moved:  start

Total nodes generated: 3
Solution Path ['start', 'goal']
Total nodes generated: 3
Loop break...




For board S2:

2
Solution found!
Solution Length:  2
Solution Path ['start', 'down', 'down', 'goal']
Total nodes generated: 5
Loop break...




For board S3:

11
Solution found!
Solution Length:  11
Solution Path ['start', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'down', 'down', 'goal']
Total nodes generated: 8337
Loop break...




For board S4:

12
Solution found!
Solution Length:  12
Solution Path ['start', 'down', 'right', 'up', 'left', 'down', 'right', 'up', 'left', 'down', 'right', 'down', 'down', 'goal']
Total nodes generated: 18771
Loop break...




For board S5:

13
Solution found!
Solution Length:  13
Solution Path ['start', 'down', 'right', 'down', 'right', 'up', 'left', 'left', 'up', 'right', 'down', 'right', 'down', 'down', 'goal']
Total nodes generated: 30593
Loop break...




For board S6:

1
Solution found!
Solution Length:  1
Solution Path ['start', 'right', 'goal']
Total nodes generated: 1
Loop break...




For board S7:

7
Solution found!
Solution Length:  7
Solution Path ['start', 'up', 'right', 'right', 'down', 'right', 'down', 'down', 'goal']
Total nodes generated: 445
Loop break...




For board S8:

11
Solution found!
Solution Length:  11
Solution Path ['start', 'up', 'left', 'down', 'right', 'up', 'left', 'down', 'right', 'right', 'right', 'down', 'goal']
Total nodes generated: 8073
Loop break...




For board S9:

9
Solution found!
Solution Length:  9
Solution Path ['start', 'left', 'left', 'up', 'up', 'right', 'down', 'down', 'right', 'right', 'goal']
Total nodes generated: 1014
Loop break...




For board S10:

14
Solution found!
Solution Length:  14
Solution Path ['start', 'down', 'right', 'down', 'left', 'up', 'up', 'right', 'right', 'down', 'left', 'down', 'right', 'right', 'down', 'goal']
Total nodes generated: 48172
Loop break...




For board S11:

2
Solution found!
Solution Length:  2
Solution Path ['start', 'right', 'down', 'goal']
Total nodes generated: 5
Loop break...




For board S12:

6
Solution found!
Solution Length:  6
Solution Path ['start', 'down', 'left', 'down', 'right', 'right', 'right', 'goal']
Total nodes generated: 161
Loop break...




For board S13:

2
Solution found!
Solution Length:  2
Solution Path ['start', 'right', 'right', 'goal']
Total nodes generated: 3
Loop break...




For board S14:

11
Solution found!
Solution Length:  11
Solution Path ['start', 'down', 'left', 'up', 'right', 'down', 'left', 'up', 'right', 'down', 'right', 'right', 'goal']
Total nodes generated: 5489
Loop break...




For board S15:

4
Solution found!
Solution Length:  4
Solution Path ['start', 'up', 'right', 'right', 'down', 'goal']
Total nodes generated: 20
Loop break...




For board S16:

1
Solution found!
Solution Length:  1
Solution Path ['start', 'down', 'goal']
Total nodes generated: 1
Loop break...




For board S17:

12
Solution found!
Solution Length:  12
Solution Path ['start', 'up', 'right', 'up', 'left', 'down', 'right', 'up', 'left', 'down', 'right', 'down', 'down', 'goal']
Total nodes generated: 21931
Loop break...




For board S18:

14
Solution found!
Solution Length:  14
Solution Path ['start', 'up', 'left', 'left', 'up', 'right', 'down', 'right', 'up', 'left', 'left', 'down', 'right', 'right', 'down', 'goal']
Total nodes generated: 20398
Loop break...




For board S19:

5
Solution found!
Solution Length:  5
Solution Path ['start', 'up', 'right', 'down', 'right', 'right', 'goal']
Total nodes generated: 35
Loop break...




For board S20:

11
Solution found!
Solution Length:  11
Solution Path ['start', 'down', 'right', 'up', 'left', 'down', 'right', 'up', 'left', 'down', 'right', 'right', 'goal']
Total nodes generated: 7085
Loop break...




For board S21:

12
Solution found!
Solution Length:  12
Solution Path ['start', 'down', 'right', 'up', 'left', 'down', 'right', 'up', 'left', 'down', 'right', 'right', 'down', 'goal']
Total nodes generated: 18350
Loop break...




For board S22:

10
Solution found!
Solution Length:  10
Solution Path ['start', 'up', 'left', 'down', 'right', 'up', 'left', 'down', 'down', 'right', 'right', 'goal']
Total nodes generated: 4459
Loop break...




For board S23:

3
Solution found!
Solution Length:  3
Solution Path ['start', 'down', 'down', 'down', 'goal']
Total nodes generated: 13
Loop break...




For board S24:

5
Solution found!
Solution Length:  5
Solution Path ['start', 'up', 'right', 'down', 'right', 'down', 'goal']
Total nodes generated: 100
Loop break...




For board S25:

5
Solution found!
Solution Length:  5
Solution Path ['start', 'down', 'right', 'right', 'right', 'down', 'goal']
Total nodes generated: 45
Loop break...




|         0       2       11      12      13      1       7       11      9       14      2       6       2       11      4       1       12      14      5       11      12      10      3       5       5        7.32
|
|
|
|
|___________________________________________________________________
        S1      S2      S3      S4      S5      S6      S7      S8      S9      S10     S11     S12     S13     S14     S15     S16     S17     S18     S19     S20     S21     S22     S23     S24     S25      Avg


"""



