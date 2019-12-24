import pandas as pd
import networkx as nx
import numpy as np
import functionality1 as f1
import functionality2 as f2
import functionality3 as f3
import functionality4 as f4
import create_graph 

def getFunction(i):
    if i == 1:
        print("functionality 1 called\n")
        functionality1()
    elif i == 2:
        print("Functionality 2 called\n")
        functionality2()
    elif i == 3:
        print("Functionality 3 called\n")
        functionality3()
    elif i ==4:
        print("Functionality 4 called\n")
        functionality4()

def functionality1():
    node_id = int(input("Digit a node\n"))
    dist_funct = int(input("Digit 1 for the distance function, 2 for the time distance function or 3 for the network distance\n"))
    threshold = int(input("Digit the distance threshold\n"))
    if dist_funct == 1:
        param = 'distance'
    elif dist_funct == 2:
        param = 'time'
    else:
        param = 'network'
    f1.functionality1(G, node_id, threshold, param)

def functionality2():
    nodes = list(map(int, input("Digit a list of node (comma separeted) in this way: 'ex. 25,346,456'\n").split(",")))
    dist_funct = int(input("Digit 1 for the distance function, 2 for the time distance function or 3 for the network distance\n"))
    if dist_funct == 1:
        param = 'distance'
    elif dist_funct == 2:
        param = 'time'
    else:
        param = 'network'
    f2.functionality2(G, nodes, param)

def functionality3():
    node_id = int(input("Digit a node\n"))
    nodes = list(map(int, input("Digit a list of node (comma separeted) in this way: 'ex. 25,346,456'\n").split(",")))
    dist_funct = int(input("Digit 1 for the distance function, 2 for the time distance function or 3 for the network distance\n"))
    if dist_funct == 1:
        param = 'distance'
    elif dist_funct == 2:
        param = 'time'
    else:
        param = 'network'
    f3.routes(G, node_id, nodes, param)


def functionality4():
    node_id = int(input("Digit a node\n"))
    nodes = list(map(int, input("Digit a list of node (comma separeted) in this way: 'ex. 25,346,456'\n").split(",")))
    dist_funct = int(input("Digit 1 for the distance function, 2 for the time distance function or 3 for the network distance\n"))
    if dist_funct == 1:
        param = 'distance'
    elif dist_funct == 2:
        param = 'time'
    else:
        param = 'network'
    f4.functionality4(G, node_id, nodes, param)

has_graph = 0
while not has_graph:
  has_graph = int(input("Do you already have the graph ? If yes, digit 1, else digit 0\n"))
  if has_graph == 0:
    print("Creating the graph... \n")
    create_graph.create()
    has_graph = 1

print("Waiting... \n")
print("Setting the map... \n")
G = nx.read_gpickle("directed_graph.gpickle.gz")
print("The map is ready!\n")
int_func = 5
while int_func != 0: 
  int_func = int(input("What functionality do you want (1,2,3 or 4)?\nDigit 0 to stop\n"))
  if int_func in [1,2,3,4]:
    getFunction(int_func)