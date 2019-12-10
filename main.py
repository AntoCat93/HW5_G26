import pandas as pd
import networkx as nx
import numpy as np

G = nx.read_gpickle("graph_test.gpickle.gz")

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

def functionality2():
    print("soon..")

def functionality3():
    print("soon..")

def functionality4():
    print("soon..")

i = int(input("What function do you want to call?\n"))
getFunction(i)