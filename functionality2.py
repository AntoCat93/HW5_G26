import folium
import webbrowser
import os 
from operator import itemgetter
import networkx as nx

def KruskalMST(Gd, nodes, param = 'network'):
    sG,msg = createSubGraph(Gd, nodes, param)
    if msg == 'OK':
        sorted_edges = sortEdges(sG)
        edges_visited = []
        trees = {}
        i = 0
        for el in nodes:
            trees[i] = [el]
            i += 1
        tot_cost = 0
        i = 0
        while len(edges_visited) != len(nodes) - 1:
            edge = sorted_edges[i]
            for key in trees:
                if edge['nodes'][0] in trees[key]:
                    h = key
            for key in trees:
                if edge['nodes'][1] in trees[key]:
                    k = key  
            if h!=k:
                trees[h] = trees[h] + trees[k]
                edges_visited.append((edge['nodes'][0], edge['nodes'][1]))
                del trees[k]
                tot_cost += sG.get_edge_data(edge['nodes'][0], edge['nodes'][1])['w']
            i += 1
        return edges_visited, tot_cost
    else :
        print("Nodes are not connected!")
        return [], 0

def sortEdges(sG):
    edges_dict = []
    for edge in list(sG.edges()):
        edges_dict.append({ 'nodes' : (edge[0], edge[1]), 'w' : int(sG.get_edge_data(edge[0], edge[1])['w'])})
    sorted_dict = sorted(edges_dict, key=lambda k: k['w']) 
    return sorted_dict

def createSubGraph(Gd, nodes, param = 'network'):
    msg = "OK"
    subGraph = nx.DiGraph()
    for n in nodes:
        subGraph.add_node(n, attr_dict = Gd.nodes[n-1]['attr_dict'])
    for n in nodes:
        for s in nodes:
            if s != n:
                if s in findNeigb(Gd,n):
                    if param == 'network': 
                        w = 1
                    else:
                        w =  Gd.get_edge_data(n, s)['attr_dict'][param]
                    subGraph.add_edge(n, s, w = w)
    for n in nodes:
        if len(list(subGraph.edges(n))) == 0:
            msg = "Not connected"
    return subGraph, msg

def findNeigb(graph, node):
    return [n[1] for n in list(graph.edges(node))]

def functionality2(Gd, nodes, param = 'network'):
    res, distance = KruskalMST(Gd, nodes, param = 'network')
    if len(res) > 0:
        my_map4 = folium.Map(location = [Gd.nodes[nodes[0]-1]['attr_dict']['latitude'], Gd.nodes[nodes[0]-1]['attr_dict']['longitude']], zoom_start = 12)
        for s in res:
            folium.PolyLine(locations = [(Gd.nodes[s[0]-1]['attr_dict']['latitude'], Gd.nodes[s[0]-1]['attr_dict']['longitude']), (Gd.nodes[s[1]-1]['attr_dict']['latitude'], Gd.nodes[s[1]-1]['attr_dict']['longitude'])], 
                          line_opacity = 0.5, color = getParamColor(param)).add_to(my_map4)
        for s in nodes:
            folium.Marker([Gd.nodes[s-1]['attr_dict']['latitude'], Gd.nodes[s-1]['attr_dict']['longitude']], 
                        popup = 'Node '+ str(s), icon=folium.Icon(color='lightgray', icon='map-pin', prefix='fa') ).add_to(my_map4)
        my_map4.save("my_map_new.html")
        webbrowser.open('file://' + os.path.realpath('my_map_new.html'))

def getParamColor(param):
  if param == 'time':
    return 'green'
  elif param == 'distance':
    return 'blue'
  else:
    return 'gray'