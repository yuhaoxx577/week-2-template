'''Representing graphs'''

node_dict={'a':0,'b':1,'c':2,'d':3,'e':4}

def part_1_graph():
    # Initalize a list of 5 empty sets
    graph_representation[set() _ for in range(5)]
    
    # Add edge based on the diagram:

    # a(index of 0) connects to b(index of 1) and e(index of 4)
    graph_representation[0].add(1)
    graph_representation[0].add(4)

    # b(index of 1) connects to c(index of 2) 
    graph_representation[1].add(2)

    # c(index of 2) connects to d(index of 3) and e(index of 4)
    graph_representation[2].add(3)
    graph_representation[3].add(4)

    # d(index of 3) connects to b(index of 1) 
    graph_representation[3].add(1)

    return graph_representation
    
def part_2_graph():
    # Initialize a list of 5 empty lists
    graph_representation[[] _ for in range(5)]

    # Add edges based on the diagram:

    # a(index of 0) connects to a(index of 0) and b(index of 1) and e(index of 4)
    graph_representation[0].add(0)
    graph_representation[0].add(1)
    graph_representation[0].add(4)
    
    # b(index of 1) connects to c(index of 2) 
    graph_representation[1].add(2)
    
    # c(index of 2) connects to a(index of 0) and d(index of 3) and e(index of 4)
    graph_representation[2].add(0)
    graph_representation[2].add(3)
    graph_representation[2].add(4)
    
    # d(index of 3) has no outgoing edge
    
    
    # e(index of 4) connects to d(index of 3)
    graph_representation[4].add(3)
    
    return graph_representation

def part_3_graph():
    # Initialize a list of 4 empty dicts
    graph_representation = [{} _ for in range(4)]

    # Add edges and their weight based on the diagram:

    # a -> a with weight 8(self loop)
    graph_representation[0][0] = 8
    # a -> b with weight 1
    graph_representation[0][1] = 1
    # a -> e with weight 4
    graph_representation[0][4] = 4

    # b -> c with weight 3
    graph_representation[1][2] = 3
    # c -> e with weight 3
    graph_representation[2][4] = 4

    return graph_representation
    
def part_4_graph():
    “”“
    Represents the given directed graph using a dictionary of sets.
    The keys of the main dictionary are the nodes names(strings), and the
    values are sets containing the names of nodes to which an edge exits.
    """
    graph_representation = {}

    # Node 'a'
    # a -> a
    # a -> b
    # a -> e
    graph_representation['a'] = {'a', 'b', 'e'} 

    # Node 'b'
    # b -> c
    graph_representation['b'] = {'c'}

    # Node 'c'
    # c -> a
    graph_representation['c'] = {'a'}

    return graph_representation
    
def part_5_graph():
    “”“
    Represents the given directed graph using a dictionary of dictionaries
    The outer dictionnary keys are the source node names(Strings)
    The innner dictionaries have destination node names as keys and 
    edge weights as values.
    """
    # Node 'a'
    # a -> b with weight 5
    graph_representation['a'] = {'b': 5}

    # Node 'b'
    # b -> e with weight 3
    graph_representation['b'] = {'e': 3}

    # Node 'e'
    # e -> b with weight 2
    # e -> a with weight 6
    graph_representation['e'] = {'b': 2}
    graph_representation['e'] = {'a': 6}

    return graph_representation
