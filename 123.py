class Node(object):

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def __repr__(self):
        return self.name


N_1 = Node('1')
N_2 = Node('2')
N_3 = Node('3')
N_4 = Node('4')
N_5 = Node('5')
N_6 = Node('6')
N_7 = Node('7')
N_8 = Node('8')
N_9 = Node('9')


N_1.neighbors = [N_7, N_4, N_9]
N_2.neighbors = [N_5, N_8]
N_3.neighbors = [N_5, N_6, N_8, N_7]
N_4.neighbors = [N_1, N_7, N_9]
N_5.neighbors = [N_2, N_6, N_8, N_3]
N_6.neighbors = [N_8, N_5, N_3, N_7]
N_7.neighbors = [N_3, N_6, N_1, N_4, N_9]
N_8.neighbors = [N_2, N_5, N_3, N_6]
N_9.neighbors = [N_1, N_7, N_4]




def find_cliques(remaining_nodes=[],  potential_clique=[], skip_nodes=[], depth=0):
    if len(remaining_nodes) == 0 and len(skip_nodes) == 0:
        print('This is a clique:', potential_clique, '<=這裡是max clique')
        return 1

    found_cliques = 0
    for node in remaining_nodes:
        print('now: ', node)
        new_remaining_nodes = [n for n in remaining_nodes if n in node.neighbors]
        print('p ^ N(V): ', new_remaining_nodes)   # 把p和node的鄰居做交集

        new_potential_clique = potential_clique + [node]
        print('R v {V}: ', new_potential_clique)   # 將目前的node加入clique中

        new_skip_list = [n for n in skip_nodes if n in node.neighbors]
        print('X ^ N(v): ',new_skip_list)           # 將X和node的鄰居做交集
        print(' ')

        found_cliques += find_cliques(new_remaining_nodes, new_potential_clique, new_skip_list, depth + 1)

        remaining_nodes.remove(node)
        print('P \\ {v}: ', remaining_nodes)

        skip_nodes.append(node)
        print('X v {v}: ', skip_nodes)
        print("depth: ",depth)
        print('this is the end of the loop for the ', node, 'node')

    return found_cliques


all_nodes = [N_1, N_2, N_3, N_4, N_5, N_6, N_7, N_8, N_9]
total_cliques = find_cliques(remaining_nodes=all_nodes)
print('Total cliques found:', total_cliques)
