def christmas_tree(n):
    for i in range(n):
        print(" "*(n-i-1) + "*"*(2*i + 1))

christmas_tree(5)


"""
    *        # 1 star 4 spaces 
   ***       # 3 star 3 spaces
  *****      # 5 star 2 spaces
 *******     # 7 star 1 spaces 
*********    # 9 star 0 spaces
"""

"""
n  spc  * 
0   4    1   
1   3    3   
2   2    5
3   1    7
4   0    9

"""