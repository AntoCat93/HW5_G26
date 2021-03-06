import pandas as pd
import networkx as nx
import numpy as np

def create():
  # Read data, clean data, craete dataframe
  nodes_info = pd.read_csv('data/USA-road-d.CAL.co', skiprows= 7, sep=" ", delimiter = " ", names = ["char", "node_id", "longitude", "latitude"],
                        index_col=None, usecols=None, encoding='ISO-8859-1')
  nodes_info.drop(columns=["char"], inplace = True)
  distance_file = pd.read_csv('data/USA-road-d.CAL.gr', skiprows=7 ,sep=" ", delimiter = " ", names= ["char", "node_a", "node_b", "distance"],index_col=None, encoding='ISO-8859-1')
  time_file = pd.read_csv('data/USA-road-t.CAL.gr', skiprows=7 ,sep=" ", delimiter = " ", names= ["char", "node_a", "node_b", "time"],index_col=None, encoding='ISO-8859-1')
  time_file.drop(columns=["char"], inplace=True)
  distance_file.drop(columns=["char"], inplace=True)
  time_distance_df = pd.merge(time_file, distance_file, on=["node_a", "node_b"])
  nodes_info['latitude'] = nodes_info["latitude"].apply(lambda x: x/1_000_000)
  nodes_info['longitude'] = nodes_info["longitude"].apply(lambda x: x/1_000_000)

  # Create Graph
  G = nx.DiGraph()
  for index, row in nodes_info.iterrows():
      G.add_node(index, attr_dict = row.to_dict())
  for index, row in time_distance_df.iterrows():
      G.add_edge(row['node_a'], row['node_b'], attr_dict = row.to_dict())
  nx.write_gpickle(G, "directed_graph.gpickle.gz")