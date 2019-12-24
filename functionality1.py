import folium
import webbrowser
import os

def functionality1(G, src, d, param = 'network'):
    lenG = len(G.nodes())
    dist = [float('inf')] * lenG
    dist[src] = 0
    shortest_path = [False] * lenG
    res = []
    queue = {src: 0}
    res.append(src)
    routes = {src: [src]}
    for _ in range(lenG):
        u, mind = minDistance(lenG, dist, shortest_path, queue)
        if mind > d:
            break
        queue.pop(u)
        shortest_path[u] = True
        neigs = findNeigb(G,u)
        for v in neigs: 
            current_weight = float(getWeight(G, u, v, param))
            if current_weight > 0 and shortest_path[v] == False and dist[v] > dist[u] + current_weight: 
                dist[v] = dist[u] + current_weight
                if dist[v] <= d and v not in res:
                    routes[v] = routes[u] + [v]
                    res.append(v)
                    queue[v] = dist[v]
    plotResults(G, src, res, routes, param)

def minDistance(length, dist, sp, queue): 
    min = float('inf')
    ## remove this shit
    min_index = float('inf')
    for v, val in queue.items(): 
        if sp[v] == False:
            if  val < min:
                min = val 
                min_index = v 
    return min_index, min

def findNeigb(graph, node):
    return [n[1] for n in list(graph.edges(node))]

def getWeight(graph, node_a, node_b, param = 'network'):
    if graph.get_edge_data(node_a, node_b) != None:
        if param == 'network':
            return 1
        else:
            return graph.get_edge_data(node_a, node_b)['attr_dict'][param]
    else:
        return 0

def plotResults(G, src, res, routes, param):
    my_map4 = folium.Map(location = [G.nodes[src-1]['attr_dict']['latitude'], G.nodes[src-1]['attr_dict']['longitude']], zoom_start = 12)
    for s in res:
        if s == src:
            icon = 'home'
            color = 'red'
        elif s in res:
            icon = 'map-pin'
            color = 'blue'
        else:
            icon = 'map-marker'
            color = 'lightgray'
        folium.Marker([G.nodes[s-1]['attr_dict']['latitude'], G.nodes[s-1]['attr_dict']['longitude']], 
                    popup = 'Node '+ str(s), icon=folium.Icon(color=color, icon=icon, prefix='fa') ).add_to(my_map4)
        old_step_tmp = ''
        for s_tmp in routes[s]:
            if old_step_tmp != '':
                folium.PolyLine(locations = [old_step_tmp, (G.nodes[s_tmp-1]['attr_dict']['latitude'], G.nodes[s_tmp-1]['attr_dict']['longitude'])], 
                      line_opacity = 0.5, color = getParamColor(param)).add_to(my_map4)
            old_step_tmp = (G.nodes[s_tmp-1]['attr_dict']['latitude'], G.nodes[s_tmp-1]['attr_dict']['longitude'])
    my_map4.save("my_map_new.html")
    webbrowser.open('file://' + os.path.realpath('my_map_new.html'))

def getParamColor(param):
  if param == 'time':
    return 'green'
  elif param == 'distance':
    return 'blue'
  else:
    return 'gray'