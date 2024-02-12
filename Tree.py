#Tree(General Tree)
#Ex:                              Electronics (Parent) (Root Node) (lvl 0)
#    Laptops (Children)            Cellphones (Children)            Television(Children)  < -- Nodes (lvl 1)
#    Macbook, ThinkPad             iPhone, Google Pixel             Samsung, LG    < -- Leaf Nodes (lvl 2)

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Electronics")

    root.add_child(laptop)

    return root

build_product_tree()