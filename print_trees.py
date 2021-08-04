from datastructures import *


n1 = BinaryTreeNode(1)
n2 = BinaryTreeNode(2)
n3 = BinaryTreeNode(3)
n4 = BinaryTreeNode(4)
n5 = BinaryTreeNode(5)

n1.left = n2
n2.left = n4
n1.right = n3
n3.right = n5

b = BinaryTree(n1)

print(b)

n = [BinaryTreeNode(i) for i in range(100)]

n[1].left = n[2]
n[1].right = n[3]
n[2].left = n[4]
n[4].left = n[7]
n[7].right = n[11]
n[11].left = n[12]
n[11].right = n[13]
n[3].left = n[5]
n[3].right = n[6]
n[5].left = n[8]
n[8].left = n[14]
n[14].left = n[16]
n[14].right = n[17]
n[8].right = n[15]
n[15].left = n[18]
n[15].right = n[19]
n[6].right = n[9]


b = BinaryTree(n[1])

print(b)


