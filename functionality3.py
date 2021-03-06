import folium
import webbrowser
import os 

def functionality3(G, src, destination, param = 'network'):
    lenG = len(G.nodes())
    dist = [float('inf')] * lenG
    dist[src] = 0
    shortest_path = [False] * lenG
    routes = {src: [src]}
    queue = {src:0}
    while dist[destination] == float('inf') or shortest_path[destination] == False:        
        u = minDistanceF3(lenG, dist, shortest_path, queue)
        queue.pop(u)
        shortest_path[u] = True
        neigs = findNeigbV2(G,u)
        for v in neigs: 
            current_weight = float(getWeight(G, u, v, param))
            if current_weight > 0 and shortest_path[v] == False and dist[v] > dist[u] + current_weight: 
                dist[v] = dist[u] + current_weight
                routes[v] = routes[u] + [v]
                queue[v] = dist[v]
    return routes[destination], dist[destination]

def minDistanceF3(length, dist, sp, queue): 
    min = float('inf')
    min_index = float('inf')
    for v, val in queue.items(): 
        if sp[v] == False:
            if  val < min:
                min = val 
                min_index = v 
    return min_index 


def findNeigbV2(graph, node):
    return [n[1] for n in list(graph.edges(node))]


def getWeight(graph, node_a, node_b, param = 'network'):
    if graph.get_edge_data(node_a, node_b) != None:
        if param == 'network':
            return 1
        else:
            return graph.get_edge_data(node_a, node_b)['attr_dict'][param]
    else:
        return 0

def routes(G, src, destinations, param = 'network'):
    source  = src
    tot_steps = []
    tot_weight = 0
    for d in destinations:
        steps, weight = functionality3(G,source,d, param)
        tot_steps += steps
        tot_weight += weight
        source = d
    my_map4 = folium.Map(location = [G.nodes[src-1]['attr_dict']['latitude'], G.nodes[src-1]['attr_dict']['longitude']], zoom_start = 12)
    old_step = (G.nodes[src-1]['attr_dict']['latitude'], G.nodes[src-1]['attr_dict']['longitude'])
    for s in tot_steps:
        if s == src:
            icon = 'home'
            color = 'red'
        elif s in destinations:
            icon = 'map-pin'
            color = 'blue'
        else:
            icon = 'map-marker'
            color = 'lightgray'
        folium.Marker([G.nodes[s-1]['attr_dict']['latitude'], G.nodes[s-1]['attr_dict']['longitude']], 
                    popup = 'Node '+ str(s), icon=folium.Icon(color=color, icon=icon, prefix='fa') ).add_to(my_map4) 
        folium.PolyLine(locations = [old_step, (G.nodes[s-1]['attr_dict']['latitude'], G.nodes[s-1]['attr_dict']['longitude'])], 
                      line_opacity = 0.5).add_to(my_map4)
        old_step = (G.nodes[s-1]['attr_dict']['latitude'], G.nodes[s-1]['attr_dict']['longitude'])
    my_map4.save("my_map_new.html")
    webbrowser.open('file://' + os.path.realpath('my_map_new.html'))