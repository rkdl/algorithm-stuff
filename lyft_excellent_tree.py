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


def check_perfect_tree(adjacency_list: list[list[int]]) -> bool:
    """
             6
           /   \
         2      0
        / \    / \
       1   5  3   4
    [[3, 4, 6], [2], [1, 5, 6], [0], [0], [2], [2, 0]]
    """
    root_idx = None
    for idx, entry in enumerate(adjacency_list):
        if len(entry) == 2:
            if root_idx is not None:
                return False
            root_idx = idx
    
    if root_idx is None:
        return False


    # root_idx = 6

    def traverse(root_index: int, prev_index: int) -> int:
        # root_idx = 2 prev_index = 6
        neighbors = adjacency_list[root_index]  # [1, 5, 6]
                                                # root_idx = 1 prev = 2

        if len(neighbors) == 1 and neighbors[0] == prev_index:
            return 0

        common_depth = -1

        for neighbor in neighbors:
            if neighbor == prev_index:
                continue
            
            res = traverse(neighbor, root_index)
            if res == -1:
                return -1
            depth = 1 + traverse(neighbor, root_index)

            if common_depth == -1:
                common_depth = depth
            elif common_depth != depth:
                return -1
        
        return common_depth
    
    root = adjacency_list[root_idx]

    return traverse(root[0], root_idx) == traverse(root[1], root_idx)


print(check_perfect_tree([[3, 4, 6], [2], [1, 5, 6], [0], [0], [2], [2, 0]]))
adj_list = [[3, 4, 5], [2], [1, 5], [0], [0], [2, 0]]
print(check_perfect_tree(adj_list))
adj_list = [[1], [0, 2], [1]]
print(check_perfect_tree(adj_list))
print(check_perfect_tree([[0]]))

adj_list = [[1], [0, 2], [1, 3], [2]]
print(check_perfect_tree(adj_list))
