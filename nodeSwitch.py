import random

def node_switch_2n2m():
    # Nodes switch with probability 0.5
    n, m, v = 2, 2, 1
    conflict, non_conflict = 0, 0
    count = 0
    
    while count < 10000:
        n1_choice = False
        n2_choice = False
        if random.random() < 0.5:
            n1_choice = True
        if random.random() < 0.5:
            n2_choice = True
        
        if n1_choice == n2_choice: conflict += 1
        else: non_conflict += 1
        count += 1
        
    print(f"Conflict count: {conflict}")
    print(f"Non-conflict count: {non_conflict}")
    
def node_switch_2n3m():
    # Nodes switch with probability 0.67
    n, m, v = 2, 3, 1
    conflict, non_conflict = 0, 0
    count = 0
    
    while count < 10000:
        n1_channel = 0
        n2_channel = 0
        if random.random() < 0.67:
            if random.random() < 0.5: 
                n1_channel = 1
            else: n1_channel = 2
        if random.random() < 0.67:
            if random.random() < 0.5:
                n2_channel = 1
            else: n2_channel = 2
            
        
        if n1_channel == n2_channel: conflict += 1
        else: non_conflict += 1
        count += 1
        
    print(f"Conflict count: {conflict}")
    print(f"Non-conflict count: {non_conflict}")


def node_switch(n, m):
    # n = number of nodes, m = number of channels, v = number of vacant channels
    v = m - 1
    conflict = 0
    non_conflict = 0
    count = 0
    # TODO: complete this general case function
        

node_switch_2n3m()