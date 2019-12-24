# HW5_G26 

## Homework 5 - Explore California and Nevada with graphs

## Files

* `README.md`

* `main.py`: execute this to call all the functionalities. If you need to create the graph, you can do it from here. Then the graph is loaded, and you can choose which functionality excute and insert all the params that you need.

* `create_graph.py`: file that contains the function to create and graph. Then it's stored in a file .gz

* `funcionality1.py`: file that contains the functions to execute functionality1. We chose to implement it as a samplification of dijkstra algorithm, that stops when the threshold is exceeded. Then we create an html page with the map of all nodes reached.

* `funcionality2.py`: file that contains the functions to execute functionality2. We chose to implement it with the Kruskal algo, after we create a subgraph with the nodes required by the user. Then we create an html page with the map of the streets that connect all the nodes.

* `funcionality3.py`: file that contains the functions to execute functionality3. We chose to implement it with the Dijkstra algo, then we create an html page with the map of the streets and nodes reached.

* `funcionality4.py`: file that contains the functions to execute functionality4. We chose to simplify this complex problem by applying the formula of the geographical distance of the nodes (derived from latitude and longitude). So we proceed from the starting node to the closest geographically, and so on, until we get to the last one.Then we applied functionality 3 to the ordered list.
  
## Notes

We decided to create the graph using networkx, but we developed all the functions by ourselves. We only used it as a support structure. 
For the graphical part we used Folium.

## Team

* Antonio Cataldi

* Omid Ghamiloo

* Batuhan Yeniceri
