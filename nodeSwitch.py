import random
import matplotlib.pyplot as plt

def node_switch_2n2m():
    # Nodes switch with probability 0.5
    conflict, non_conflict = 0, 0
    count = 0
    
    while count < 10000:
        n1_choice = 0
        n2_choice = 0
        if random.random() < 0.5:
            n1_choice = 1
        if random.random() < 0.5:
            n2_choice = 1
        
        if n1_choice == n2_choice: conflict += 1
        else: non_conflict += 1
        count += 1
    
    x = [f'Conflict: {str(conflict)}', f'Non-conflict: {str(non_conflict)}']
    result = [conflict, non_conflict]

    x_pos = [i for i, _ in enumerate(x)]
    
    fig, ax = plt.subplots() 
    
    ax.bar(x_pos[0], result[0])
    ax.bar(x_pos[1], result[1])

    plt.ylabel("Simulation result")
    plt.title(f"Proportion of non-conflicting result to 10,000 simulations: {non_conflict/10000}")
    plt.xticks(x_pos, x)
    plt.show()

    
def node_switch_2n3m():
    # Nodes switch with probability 0.67
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
        
    x = [f'Conflict: {str(conflict)}', f'Non-conflict: {str(non_conflict)}']
    result = [conflict, non_conflict]

    x_pos = [i for i, _ in enumerate(x)]
    
    fig, ax = plt.subplots() 
    
    ax.bar(x_pos[0], result[0])
    ax.bar(x_pos[1], result[1])

    plt.ylabel("Simulation result")
    plt.title(f"Proportion of non-conflicting result to 10,000 simulations: {non_conflict/10000}")
    plt.xticks(x_pos, x)
    plt.show()
    
def node_switch_3n3m():
    # Nodes switch with probability 0.67
    # Result in non-conflict 22.2% of the time
    conflict, non_conflict = 0, 0
    count = 0
    p = 0.67

    while count < 10000:
        n1_channel = 0
        n2_channel = 0
        n3_channel = 0
        if random.random() < p:
            if random.random() < 0.5: 
                n1_channel = 1
            else: n1_channel = 2
            
        if random.random() < p:
            if random.random() < 0.5:
                n2_channel = 1
            else: n2_channel = 2
            
        if random.random() < p:
            if random.random() < 0.5:
                n3_channel = 1
            else: n3_channel = 2
            
        
        if n1_channel == n2_channel or n2_channel == n3_channel or n1_channel == n3_channel: conflict += 1
        else: non_conflict += 1
        count += 1
        
    x = [f'Conflict: {str(conflict)}', f'Non-conflict: {str(non_conflict)}']
    result = [conflict, non_conflict]

    x_pos = [i for i, _ in enumerate(x)]

    fig, ax = plt.subplots() 

    ax.bar(x_pos[0], result[0])
    ax.bar(x_pos[1], result[1])

    plt.ylabel("Simulation result")
    plt.title(f"Proportion of non-conflicting result to 10,000 simulations: {non_conflict/10000}")
    plt.xticks(x_pos, x)
    plt.show()

node_switch_2n2m()