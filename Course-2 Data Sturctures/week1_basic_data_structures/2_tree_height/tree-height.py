# python3
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.nodes = {}
                self.root = 0

        def build_tree(self):
                for i in range(self.n):
                        self.nodes[i] = []
                for child_index in range(self.n):
                        parent_index = self.parent[child_index]
                        if parent_index == -1:
                                self.root = child_index
                        else:
                                self.nodes[parent_index].append(child_index)
                for key in self.nodes.keys():
                        self.nodes[key] = tuple(self.nodes[key])
                return self.root

        def compute_height(self, first_check, tree_root):
                if len(tree_root) == 0:
                        return 0
                elif first_check:
                        tree_root = int(tree_root)
                        length = len(self.nodes[tree_root])
                        if length == 0:
                                left_tree = ()
                                right_tree = ()
                        else:
                                mid = length//2
                                left_tree = self.nodes[tree_root][:mid]
                                right_tree = self.nodes[tree_root][mid:]
                        return 1+max(self.compute_height(False, left_tree), self.compute_height(False, right_tree))                        
                elif len(tree_root) == 1:
                        tree_root = int(tree_root[0])
                        length = len(self.nodes[tree_root])
                        if length == 0:
                                left_tree = ()
                                right_tree = ()
                        else:
                                mid = length//2
                                left_tree = self.nodes[tree_root][:mid]
                                right_tree = self.nodes[tree_root][mid:]
                        return 1+max(self.compute_height(False, left_tree), self.compute_height(False, right_tree))
                else:
                       new_length = len(tree_root)
                       new_mid = new_length//2
                       left_tree = tree_root[:new_mid]
                       right_tree = tree_root[new_mid:]  
                       return max(self.compute_height(False, left_tree), self.compute_height(False, right_tree))

def main():
        tree = TreeHeight()
        tree.read()
        tree_root = str(tree.build_tree())
        print(tree.compute_height(True, tree_root))

if __name__ == "__main__":
    while(True):
            main()

threading.Thread(target=main).start()