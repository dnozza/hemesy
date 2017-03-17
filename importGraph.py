# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 17:24:18 2017

@author: debora.nozza
"""

import networkx as nx
import pickle 
import os
import sys, getopt

#%%

def saveConnectedComponents(file_input, path_output):
    G=nx.read_edgelist(file_input,delimiter="\t",nodetype=int, data=(('weight',float),))
    con_comp = list(nx.connected_components(G))
    n_con_comp = len(con_comp)
    
    print ("Number of Connected Components : " + str(n_con_comp) + "\n")
    print ("Distribution : ")
    for i in range(0,n_con_comp):
        print (str(len(con_comp[i]))+"\t")
    print ("\n")
    if not os.path.exists(path_output):
        os.makedirs(path_output)
    pickle.dump( con_comp, open(path_output+"connected_components.pickle", "wb" ) )


if __name__ == "__main__":

	ifile=''
	ofile=''
	 
	###############################
	# o == option
	# a == argument passed to the o
	###############################
	# Cache an error with try..except 
	# Note: options is the string of option letters that the script wants to recognize, with 
	# options that require an argument followed by a colon (':') i.e. -i fileName
	#
	try:
		myopts, args = getopt.getopt(sys.argv[1:],"i:o:")
	except getopt.GetoptError as e:
		print (str(e))
		print("Usage: %s -i input -o output" % sys.argv[0])
		sys.exit(2)
	 
	for o, a in myopts:
		if o == '-i':
			ifile=a
		elif o == '-o':
			ofile=a
	 
	saveConnectedComponents(ifile,ofile)
