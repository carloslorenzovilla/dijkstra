import numpy as np

def dijkstra(n, s):
    """ Finds the lowest cost paths between nodes in a network
        of size n, and source node s. Prints predecessor vector.
        
        n: int
        s: int
    """
    c = np.empty((n.size,n.size))                               #initialize nxn matrix
    for i in range(n.size):                                     #init cost matrix, user input
        c[i] = np.asarray(list(map(float,input
                                   ('Enter Cost Row %d '
                                    'separated by spaces. '
                                    '(Ex: 3 inf 17): '
                                    % (i+1)).split())))

    while True:

        p = np.array(c[s-1,:])                                  #initial p vector                        
        w = np.array([s])                                       #accumulating nodes
        y = np.setdiff1d(n,w)                                   #remaining nodes, minus s
        pred = (np.ones(n.size))*s                              #predecessor vector

        while True:

            x = y[np.argmin(np.delete(p, w-1))]                 #find new best friend
            w = np.append(w,x)                                  #update accumulating nodes
            y = np.setdiff1d(n,w)                               #update remaining nodes

            for idx in range(y.size):

                if p[y[idx]-1] > p[x-1] + c[x-1,y[idx]-1]:      #if current cost > new cost
                    p[y[idx]-1] =  p[x-1] + c[x-1,y[idx]-1]     #update p vector
                    pred[y[idx]-1] = x                          #update pred vector

            if w.size == n.size:                                #end loop
                break

        print()                                                 #display results
        print('SOURCE: Node',s,'\n')
        print('p-vector: ',p)
        print()
        print('predecessor vector: ',pred,'\n')

        close = input("Select a New Source(1)? or Exit(2):")    #select new source or exit

        if close == '2':                                        #end loop, exit program
            return

        s = int(input('Source Number: '))                       #input new source
    
n = np.arange(1,int(input('Size of Network: '))+1)              #network size, user input
s = int(input('Source Number: '))                               #souce node, user input
dijkstra(n, s)



