# explanations for member functions are provided in requirements.py
from __future__ import annotations
import math

class FibNode:
    def __init__(self, val: int):
        self.val = val
        self.parent = None
        self.children = []
        self.flag = False

    def get_value_in_node(self):
        return self.val

    def get_children(self):
        return self.children

    def get_flag(self):
        return self.flag

    def __eq__(self, other: FibNode):
        return self.val == other.val

class FibHeap:
    def __init__(self):
        # you may define any additional member variables you need
        self.roots = []
        self.least = None
        self.count = 0

    def get_roots(self) -> list:
        return self.roots

    def insert(self, val: int) -> FibNode:
        new_node = FibNode(val)
        self.roots.append(new_node)
        #min_node = self.find_min()
        if self.least is None or val < self.least.val:
            self.least = new_node
        self.count += 1
        return new_node

    def delete_min(self) -> None:
        M = 0
        for node in self.roots:
            M = max(len(node.children), M)
        #print(M)
        least_node = self.least

        self.roots.remove(least_node)
        self.count -= 1
        for child in least_node.children:
            child.flag = False
            child.parent = None
            self.roots.append(child)
        #self.roots.remove(self.least)
        #self.count = self.count - 1
        #print(self.roots[4].val)
        #self.least = self.roots[0]

        #M = 0
        #for node in self.roots:
            #M = max(len(node.children), M)

        #C = (math.ceil(math.log(self.count) / math.log(1.618)) + 1) * [None]
        #R = self.roots.copy()
        self.merge()
        #i = 0
        #for node in R:
        #while self.roots != []:
         #   x = self.roots[0]
          #  self.roots.remove(x)
           # if C[len(x.children)] is not None:
            #    y = C[len(x.children)]
             #   if x.val > y.val:
              #      self.merge(x,y)
                    #print(y.val)
               # else:
                #    self.merge(y,x)
                #C[len(x.children)] = None
            #else:
             #   C[len(x.children)] = x
        self.least = self.roots[0]
        for k in range(1, len(self.roots)):
            if self.roots[k].val < self.least.val:
                self.least = self.roots[k]
        #print(self.roots[0].val)
        #self.roots = R
        #print(self.roots[0].val)

    def merge(self) -> None:
        #val1 = node1.val
        #val2 = node2.val
        #if val1 < val2:
            #node1.children.append(node2)
            #node2.parent = node1
            #self.roots.remove(node2)
            #return node1
        #else:
        C = (math.ceil(math.log(self.count) / math.log(1.618)) + 1) * [None]

        R = []
        for root in self.roots:
            R.append(root)

        while len(R) > 0:
            root = R.pop()

            if C[len(root.children)] is None:
                C[len(root.children)] = root
            else:
                node = C[len(root.children)]
                if root.val > node.val:
                    node.children.append(root)
                    root.parent = node
                    R.append(node)
                    self.roots.remove(root)
                else:
                    root.children.append(node)
                    node.parent = root
                    R.append(root)
                    self.roots.remove(node)

                index = -100
                for i, val in enumerate(C):
                    if val is None:
                        continue

                    if val == node:
                        index = i

                C[index] = None
        #self.roots.remove(node1)
        #return node2

        #i = 0
        #while(i < len(self.roots)):
            #if(self.roots[i].val < self.least.val):
                #self.least = self.roots[i]
            #i += 1
        #self.roots.remove(self.least)
        #self.least = self.roots[0]
        #i = 0
        #while(i < len(self.roots)):
            #if(self.roots[i].val < self.least.val):
                #self.least = self.roots[i]
            #i += 1

    def find_min(self) -> FibNode:
        if self.least is None :
            return None
        return self.least

    def decrease_priority(self, node: FibNode, new_val: int) -> None:
        node.val = new_val
        if new_val < self.least.val:
            self.least = node
        if node not in self.roots:
            self.promote(node)

    def promote(self, node: FibNode):
        parent_node = node.parent
        if node not in self.roots:
            parent_node.children.remove(node)
            node.parent = None
            self.roots.append(node)
            node.flag = False
            if parent_node.flag:
                self.promote(parent_node)
            elif parent_node not in self.roots:
                parent_node.flag = True



    # feel free to define new methods in addition to the above
    # fill in the definitions of each required member function (above),
    # and for any additional member functions you define
