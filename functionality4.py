import folium
import webbrowser
import os 
import functionality3 as func3 
from math import radians, cos, sin, asin, sqrt

def functionality4(Gd, src, nodes, param= 'network'):
    node_from = src
    ordered_destination = []
    last_node = nodes[-1]
    while len(ordered_destination) != len(nodes) -1:
        min_d = float('inf')
        min_node = float('inf')
        for s in nodes:
            if s not in ordered_destination:
                dist = getnodedistance(Gd, node_from, s)
                if dist < min_d:
                    min_d = dist
                    min_node = s
        node_from = min_node
        ordered_destination.append(node_from)
    ordered_destination.append(last_node)
    func3.routes(Gd, src, ordered_destination, param)

def getnodedistance(Gd, node_a, node_b):
    return haversine(Gd.nodes[node_a-1]['attr_dict']['longitude'],Gd.nodes[node_a-1]['attr_dict']['latitude'],Gd.nodes[node_b-1]['attr_dict']['longitude'],Gd.nodes[node_b-1]['attr_dict']['latitude'])

def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6371* c
    return km