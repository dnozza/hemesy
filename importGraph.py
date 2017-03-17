# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 17:24:18 2017

@author: debora.nozza
"""

import networkx as nx
import pickle 

#%%

if __name__ == "__main__":
    G=nx.read_edgelist('data/edges_500.tsv',delimiter="\t",nodetype=int, data=(('weight',float),))
    con_comp = list(nx.connected_components(G))
    n_con_comp = len(con_comp)
    
    print ("Number of Connected Components : " + str(n_con_comp) + "\n")
    print ("Distribution : ")
    for i in range(0,n_con_comp):
        print (str(len(con_comp[i]))+"\t")
    print ("\n")
    pickle.dump( con_comp, open( "output/connected_components.pickle", "wb" ) )
