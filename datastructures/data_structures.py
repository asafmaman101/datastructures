from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, List, Union, Dict

import numpy as np
import math

from main import main


class DataStructure:

    def is_empty(self):
        raise NotImplementedError


@dataclass
class Node:
    value: Any = None

@dataclass
class TrieNode(Node):
    end_node: bool = False
    children: dict = field(default_factory=dict)

@dataclass
class Trie(DataStructure):
    root: Node = field(default_factory=lambda: Node())

@dataclass
class LinkedListNode(Node):
    next: LinkedListNode = field(default=None, repr=False)


@dataclass
class BinaryTreeNode(Node):
    right: BinaryTreeNode = field(default=None, repr=False)
    left: BinaryTreeNode = field(default=None, repr=False)


@dataclass
class LinkedList(DataStructure):
    head: Union[LinkedListNode, None] = None
    tail: Union[LinkedListNode, None] = None

    def __init__(self, elements: List[Any] = None):
        self.head = None
        self.tail = None
        if elements:
            for element in elements:
                self.add(element)

    def __repr__(self):
        all = []
        p = self.head
        while p:
            all.append(p.value)
            p = p.next
        return str(all)

    def __getitem__(self, item):
        count = 0
        p = self.head
        while p:
            if count == item:
                return p.value
            p = p.next
            count += 1

    def add(self, element: Any) -> None:
        new_node = LinkedListNode(element)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    def is_empty(self) -> bool:
        if not self.head and not self.tail:
            return True
        return False

    def __iter__(self):
        self.curr = self.head
        return self

    def __next__(self):
        if not self.curr:
            raise StopIteration
        temp = self.curr.value
        self.curr = self.curr.next
        return temp


@dataclass
class BinaryTree(DataStructure):
    root: BinaryTreeNode = None

    def __init__(self, elements: Union[List[int], int]=None):

        if not elements:
            self.root = None
            
        elif isinstance(elements, int):
            self.root = BinaryTreeNode(elements)

        elif isinstance(elements, BinaryTreeNode):
            self.root = elements

        elif isinstance(elements, list):
            if elements:
                def insert(node: BinaryTreeNode, i):
                    if len(elements) > 2 * i + 1:
                        if elements[2 * i + 1]:
                            node.left = BinaryTreeNode(elements[2 * i + 1])
                        if node.left:
                            insert(node.left, 2*i+1)

                    if len(elements) > 2 * i + 2:
                        if elements[2 * i + 2]:
                            node.right = BinaryTreeNode(elements[2 * i + 2])
                        if node.right:
                            insert(node.right, 2*i+2)

                
                self.root = BinaryTreeNode(elements[0])
                insert(self.root, 0)
        else:
            raise TypeError("BinaryTree constructor should be built by int or list of int")

             

    
    def __repr__(self):
        res = [[' '] * (self.width) for _ in range(self.height * 2 + 1)]
        left_width = BinaryTree(self.root.left).width if self.root.left else 0
        queue = [(self.root, 0, left_width)]

        while queue:
            curr, row, col = queue.pop(0)

            if curr.left:
                queue.append((curr.left, row+2, col-len(str(curr.left.value))-BinaryTree(curr.left.right).width))
                res[row+1][col-int(math.ceil((len(str(curr.left.value))+BinaryTree(curr.left.right).width) / 2))] = '/'
            if curr.right:
                queue.append((curr.right, row+2, col+len(str(curr.value))+BinaryTree(curr.right.left).width))
                res[row+1][len(str(curr.value))+col+int(math.ceil((BinaryTree(curr.right.left).width) / 2))] = '\\'

            for i, char in enumerate(str(curr.value)):
                res[row][col+i] = str(curr.value)[i]
                

        return '\n'.join(map(lambda x: ''.join(x), res))



    def is_empty(self):
        return not self.root

    @property
    def height(self):
        def dfs(node: BinaryTreeNode) -> int:
            if not node: return -1
            return max(dfs(node.left), dfs(node.right)) + 1

        return dfs(self.root)

    @property
    def right_width(self):
        def dfs(node: BinaryTreeNode) -> int:
            if not node: return -1
            return dfs(node.right) + 1

        return dfs(self.root)

    @property
    def left_width(self):
        def dfs(node: BinaryTreeNode) -> int:
            if not node: return -1
            return dfs(node.left) + 1

        return dfs(self.root)

    @property
    def width(self):
        def dfs(node: BinaryTreeNode) -> int:
            if not node: return 0
            return dfs(node.left) + len(str(node.value)) + dfs(node.right)
        
        return dfs(self.root)


@dataclass
class MaxHeap(DataStructure):
    elements: list = field(default_factory=list)

    def __init__(self, elements):
        self.elements = list()
        for element in elements:
            self.add(element)

    def add(self, element):
        self.elements.append(element)

        child_pointer = self.amount - 1

        while child_pointer:
            child = self.elements[child_pointer]
            parent_pointer = self.get_parent(child_pointer)
            parent = self.elements[parent_pointer]
            if parent < child:
                self.elements[parent_pointer], self.elements[child_pointer] = \
                    self.elements[child_pointer], self.elements[parent_pointer]
            else:
                break
            child_pointer = parent_pointer

    def pop(self):
        if self.amount == 0: return None
        if self.amount == 1: return self.elements.pop()
        self.elements[0], self.elements[-1] = self.elements[-1], self.elements[0]
        res = self.elements.pop()
        parent_pointer = 0

        while True:
            parent = self.elements[parent_pointer]
            rchild_pointer, lchild_pointer = self.get_rchild(parent_pointer), self.get_lchild(parent_pointer)

            rchild = self.elements[rchild_pointer] if rchild_pointer != -1 else None
            lchild = self.elements[lchild_pointer] if lchild_pointer != -1 else None

            if rchild and lchild:
                if parent < max(rchild, lchild):
                    maxchild_pointer = [rchild_pointer, lchild_pointer][np.argmax([rchild, lchild])]
                    self.elements[maxchild_pointer], self.elements[parent_pointer] = self.elements[parent_pointer], \
                                                                                     self.elements[maxchild_pointer]
                    parent_pointer = maxchild_pointer
                else:
                    break
            elif rchild:
                if parent < rchild:
                    self.elements[rchild_pointer], self.elements[parent_pointer] = self.elements[parent_pointer], \
                                                                                   self.elements[rchild_pointer]
                    parent_pointer = rchild_pointer
                else:
                    break
            elif lchild:
                if parent < lchild:
                    self.elements[lchild_pointer], self.elements[parent_pointer] = self.elements[parent_pointer], \
                                                                                   self.elements[lchild_pointer]
                    parent_pointer = lchild_pointer
                else:
                    break
            else:
                break

        return res

    @property
    def amount(self):
        return len(self.elements)

    @staticmethod
    def get_parent(i):
        if i == 0:
            return 0
        elif i % 2 == 0:
            return (i - 2) // 2
        else:
            return (i - 1) // 2

    def get_rchild(self, i):
        res = 2 * i + 2
        if res < self.amount:
            return res
        return -1

    def get_lchild(self, i):
        res = 2 * i + 1
        if res < self.amount:
            return res
        return -1


@dataclass
class UndirectedGraph(DataStructure):
    nodes: dict

    def __init__(self, nodes=None):
        self.nodes = defaultdict(set)
        if nodes is not None: self.nodes.update(nodes)
        self.verify_undirected()

    def __repr__(self):
        if not self.nodes:
            return 'Empty Undirected Graph'
        str = ''
        for node, neighs in list(self.nodes.items()):
            str += f'{node}: {list(neighs)}\n'

        return str

    def verify_undirected(self):
        for node, neighs in list(self.nodes.items()):
            for neigh in neighs:
                self.nodes[neigh].add(node)

    def bfs(self, start):
        seen = {start}
        queue = [start]
        distances = {start: 0}

        while queue:
            current = queue.pop(0)
            for neigh in list(self.nodes[current]):
                if neigh not in seen:
                    queue.append(neigh)
                    distances[neigh] = distances[current] + 1
                    seen.add(neigh)

        return distances
