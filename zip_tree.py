# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file.

from typing import TypeVar
import random

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')


class Node:
    def __init__(self, key: KeyType, val: ValType, rank: int):
        self.key = key
        self.val = val
        self.rank = rank
        self.left = None
        self.right = None


class ZipTree:
    def __init__(self):
        self.root = None
        self.size = 0

    @staticmethod
    def get_random_rank() -> int:
        rk = 0
        while True:
            if random.randint(0, 1) == 0:
                return rk
            else:
                rk += 1

    def unzip(self, newNode: Node, top: Node):
        def unzip_lookup(k: int, node: Node):
            if not node:
                return (None, None)
            if node.key < k:
                (P, Q) = unzip_lookup(k, node.right)
                node.right = P
                return (node, Q)
            else:
                (P, Q) = unzip_lookup(k, node.left)
                node.left = Q
                return (P, node)

        return unzip_lookup(newNode.key, top)

    def insert(self, key: KeyType, val: ValType, rank: int = -1):
        if rank == -1:
            rank = self.get_random_rank()
        self.size += 1
        newNode = Node(key, val, rank)
        if not self.root:
            self.root = newNode
            return
        parent = None
        ptr = self.root
        while ptr and ptr.rank > newNode.rank:
            parent = ptr
            if newNode.key < ptr.key:
                ptr = ptr.left
            else:
                ptr = ptr.right
        while ptr and (ptr.rank == newNode.rank) and (ptr.key < newNode.key):
            parent = ptr
            ptr = ptr.right
        (P, Q) = self.unzip(newNode, ptr)
        newNode.left = P
        newNode.right = Q
        if not parent:
            self.root = newNode
        else:
            if newNode.key < parent.key:
                parent.left = newNode
            else:
                parent.right = newNode

    def zip(self, node: Node):
        def zipup(P: Node, Q: Node):
            if not P:
                return Q
            if not Q:
                return P
            if Q.rank > P.rank:
                Q.left = zipup(P, Q.left)
                return Q
            else:
                P.right = zipup(P.right, Q)
                return P

        return zipup(node.left, node.right)

    def remove(self, key: KeyType):
        self.size -= 1
        ptr = self.root
        parent = None
        direction = None
        while ptr.key != key:
            if ptr.key < key:
                parent = ptr
                ptr = ptr.right
                direction = "right"
            else:
                parent = ptr
                ptr = ptr.left
                direction = "left"

        n = self.zip(ptr)
        if not parent:
            self.root = n
        else:
            if direction == "left":
                parent.left = n
            else:
                parent.right = n

    def find(self, key: KeyType) -> ValType:
        ptr = self.root
        while ptr:
            if key == ptr.key:
                return ptr.val
            elif key < ptr.key:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return None

    def get_size(self) -> int:
        return self.size

    def get_height_of_node(self, n: Node) -> int:
        if not n:
            return -1
        hl = self.get_height_of_node(n.left)
        hr = self.get_height_of_node(n.right)
        return 1 + max(hl, hr)

    def get_height(self) -> int:
        return self.get_height_of_node(self.root)

    def get_depth(self, key: KeyType):
        d = 0
        ptr = self.root
        while ptr:
            if key == ptr.key:
                return d
            else:
                d += 1
                if key < ptr.key:
                    ptr = ptr.left
                else:
                    ptr = ptr.right

# feel free to define new classes/methods in addition to the above
# fill in the definitions of each required member function (above),
# and any additional member functions you define
