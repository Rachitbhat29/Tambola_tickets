import random
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt


def generate_col(start, end):
    col = []
    l = [0, 1]
    l_num = list(range(start,end))
    for i in range(3):
        if random.choices(l)[0] == 1:
            o= random.choices(l_num)[0]
            col.append(o)
            l_num.remove(o)
        else:
            if len([i for i in col if i == 0]) == 2:
                o = random.choices(l_num)[0]
                col.append(o)
                l_num.remove(o)
            else:
                col.append(0)
    return (col)

def generate_ticket():
    ticket = []
    r,c = 1, 10

    for i in range(9):
        f = generate_col(r,c)
        ticket.append(f)
        r+=10
        c+=10

    y=np.array([np.array(xi) for xi in ticket])
    y = y.transpose()
    df = pd.DataFrame(y)
    df[df==0]= ' '
    return df



def print_ticket(gname=None,file_name=None):
    df = generate_ticket()
    fig, ax = plt.subplots() # no visible frame
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    ax.table(cellText=df.values,loc='center')  # where df is your data frame
    fig.tight_layout()
    try:
        os.mkdir(gname)
    except:
        pass
    file_name = file_name + '.png'
    file_name = os.path.join(gname,file_name)
    plt.savefig(file_name)


if __name__ == '__main__':
    gname = input('Enter game name')
    n = int(input('Enter the count of ticket to gererate for the game'))
    for i in range(n):
        print_ticket(gname,'Ticket'+str(i))
