"""
Let's say a binary tree is excellent if:
  1) all its non-leaf nodes have two children
  2) all its leaves have the same depth from the root

For example here is an excellent binary tree (its vertices are labeled 0 through 6):

             6
           /   \
         2      0
        / \    / \
       1   5  3   4


            6
        NULL NULL
        Not excellent

Imagine a tree with N vertices, labeled 0, 1, ..., N-1. Write a function which does the following:

Input: Adjacency list of the tree. In other words, a list of N lists, with the i-th list being a
       list of vertex i's neighbors. For example the above tree could be described as:
       [[3, 4, 6], [2], [1, 5, 6], [0], [0], [2], [2, 0]]

Output: Boolean. True if the input tree qualifies as an excellent binary tree for some choice of the root; False otherwise



             5
           /   \
         2      0
        /      / \
       1      3   4

    [[3, 4, 5], [2], [1, 5], [0], [0], [2, 0]]



            2
           / 
          1
         /
        0

             1
           /   \
         0      2
    [[1], [0, 2], [1]]


             1
           /   \
         0      2
                 \
                  3



                2
               / \
              0   3
             /
            1   
    [[1], [0, 2], [1, 3], [2]]

Don't worry about efficiency at first. Focus first on writing a correct function, then worry about optimizations later.

"""


"""
We need to check that depth of both subtrees is equal

Empty tree: root [] -> imperfect
Tree with one branch: root [<number>] -> imperfect
Tree with two branches: root[<number>, <nubmer>]

If we have two pairs with two numbers -> imperfect
"""


from tabnanny import check


def check_perfect_tree(adjacency_list: list[list[int]]) -> bool:

    def check_perfect_subtree(root_index: int, prev_index: int) -> bool:
        children = [n for n in adjacency_list[root_index] if n != prev_index]
        
        if len(children) == 0:
            return 0
        if len(children) == 1:
            return -1
        
        d1 = check_perfect_subtree(children[0], root_index)
        d2 = check_perfect_subtree(children[1], root_index)
        if d1 != d2:
            return -1
        return d1

    for root_candidate in range(len(adjacency_list)):
        if len(adjacency_list[root_candidate]) == 2 and check_perfect_subtree(root_candidate, -1) != -1:
            return True

    return False

print(check_perfect_tree([[3, 4, 6], [2], [1, 5, 6], [0], [0], [2], [2, 0]]))
adj_list = [[3, 4, 5], [2], [1, 5], [0], [0], [2, 0]]
print(check_perfect_tree(adj_list))
adj_list = [[1], [0, 2], [1]]
print(check_perfect_tree(adj_list))
print(check_perfect_tree([[0]]))

adj_list = [[1], [0, 2], [1, 3], [2]]
print(check_perfect_tree(adj_list))
