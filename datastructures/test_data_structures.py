import datastructures

class TestBinaryTree:

    def test_height(self):
        nodes = []
        for i in range(10):
            nodes.append(datastructures.BinaryTreeNode())
        binary_tree_test = datastructures.BinaryTree()
        binary_tree_test.root = nodes[0]
        nodes[0].left = nodes[1]
        nodes[0].right = nodes[2]

        assert binary_tree_test.height == 1

    def test_width(self):
        nodes = []
        for i in range(10):
            nodes.append(datastructures.BinaryTreeNode(i))
        binary_tree_test = datastructures.BinaryTree()
        binary_tree_test.root = nodes[0]
        nodes[0].left = nodes[1]
        print(binary_tree_test)
        assert binary_tree_test.width == 2

    def test_right_width(self):
        nodes = []
        for i in range(10):
            nodes.append(datastructures.BinaryTreeNode())
        binary_tree_test = datastructures.BinaryTree()
        binary_tree_test.root = nodes[0]
        nodes[0].left = nodes[1]
        nodes[0].right = nodes[2]

        assert binary_tree_test.right_width == 1

        node0 = datastructures.BinaryTreeNode(0)
        node1 = datastructures.BinaryTreeNode(1)
        node2 = datastructures.BinaryTreeNode(2)

        node0.left = node1
        node1.left = node2

        binary_tree_test = datastructures.BinaryTree(node0)
        assert binary_tree_test.right_width == 0



    def test_left_width(self):
        nodes = []
        for i in range(10):
            nodes.append(datastructures.BinaryTreeNode(i))
        binary_tree_test = datastructures.BinaryTree()
        binary_tree_test.root = nodes[0]
        nodes[0].left = nodes[1]
        nodes[0].right = nodes[2]
        print(binary_tree_test)

        assert binary_tree_test.left_width == 1

        node0 = datastructures.BinaryTreeNode(0)
        node1 = datastructures.BinaryTreeNode(1)
        node2 = datastructures.BinaryTreeNode(2)

        node0.left = node1
        node1.left = node2

        binary_tree_test = datastructures.BinaryTree(node0)
        assert binary_tree_test.left_width == 2




