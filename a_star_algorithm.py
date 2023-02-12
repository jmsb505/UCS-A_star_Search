"""
    ALGORITMO DE BÚSQUEDA A*
    Realizado por:
    - Carlos Montiel
    - Juan Sanchez
    - Esteban Alvarado
"""


def a_star_algorithm(start, goal):

    open_list = [(start.value, start)]
    closed_list = []
    expanded_nodes = 0
    while open_list:
        open_list.sort(key=lambda x: x[1].f, reverse=False)
        node = open_list.pop(0)[1]
        closed_list.append((node.value, node))
        if node.value == goal:
            print(f"\n--> Nodos expandidos: {expanded_nodes}")
            return dict(closed_list)
        print(f"Nodo Padre: {node.value} -> Costo desde Ellensburg hasta {node.value}: {node.g} millas")
        for child in node.children:
            print(f"   Nodo Hijo: {child.value} -> Costo desde {node.value} hasta esta ciudad: {child.weight} millas")
            expanded_nodes += 1
            child.set_f_value(child.h + child.g)
            if child not in dict(open_list) and child not in dict(closed_list):
                open_list.append((child.value, child))
                child.set_g_value(node.g + child.weight)
            if child.value in dict(open_list) and child.f > dict(open_list)[child.value].f:
                continue
            if child.value in dict(closed_list) and child.f > dict(open_list)[child.value].f:
                continue


class TreeNode:

    def __init__(self, value, h, weight = 0):
        
        self.value = value
        self.weight = weight
        self.h = h
        self.g = 0
        self.f = 0
        self.children = []
        
    def add_children(self, children):
        self.children.extend(children)
    
    def set_g_value(self, value):
        self.g = value
    
    def set_f_value(self, value):
        self.f = value


n1 = TreeNode('Ellensburg', 516.03)
n2 = TreeNode('Pendleton', 472.53, 168)
n3 = TreeNode('Spokane', 362.93, 175)
n4 = TreeNode('Missoula', 232.19, 199)
n5 = TreeNode('Bonners Ferry', 303.57, 112)
n6 = TreeNode('Helena', 174.65, 111)
n7 = TreeNode('West Glacier', 197.21, 176)
n8 = TreeNode('Great Falls', 104.1, 91)
n9 = TreeNode('Butte', 221.04, 65)
n10 = TreeNode('Helena', 174.65, 243)
n11 = TreeNode('Great Falls', 104.1, 211)
n12 = TreeNode('Havre', 0, 231)
n13 = TreeNode('Havre', 0, 115)

n1.add_children([n2, n3])
n3.add_children([n4, n5])
n4.add_children([n6])
n5.add_children([n7])
n6.add_children([n9, n8])
n7.add_children([n10, n11, n12])
n8.add_children([n13])

result = a_star_algorithm(n1, 'Havre')
print(f"Camino optimo: {list(result.keys())}")
print(f"Costo: {sum([item.weight for item in result.values()])} millas")
