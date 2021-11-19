import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

# 并查集实现Kruskal算法
class kruskal:
    def __init__(self, graph) -> None:
        self.graph = graph
            
    def mst(self):
        n = len(self.graph)
        mst_edges = defaultdict(int)
        parent = [_ for _ in range(n)]
        rank = [0] * n
        
        def find_parent(v):
            while parent[v] != v:
                v = parent[v]
            return v 
        def union(u, v):
            u_root = find_parent(u)
            v_root = find_parent(v)

            if rank[u_root] > rank[v_root]:
                parent[v_root] = u_root
                rank[v] += 1
            else:
                parent[u_root] = v_root
                rank[u] += 1

        
        edge_dict = defaultdict(int)
        for (u, v, w) in self.graph:
            edge_dict[(u, v)] = w
        
        sorted_edge_dict = sorted(edge_dict.items(), key=lambda x: x[1])
        for ((u, v), w) in sorted_edge_dict:
            if find_parent(u) == find_parent(v):
                continue
            else:
                union(u, v)
                mst_edges[(u, v)] = w
        return mst_edges        

def draw(G, mst_edges):
    edges = list(G.edges)
    n = len(edges)
    edge_color = ['b'] * n
    color_edges = set([_ for _ in mst_edges.keys()])

    for i in range(n):
        u, v = edges[i][0], edges[i][1]
        if (u, v) in color_edges or (v, u) in color_edges:
            edge_color[i] = 'r'
    pos = nx.kamada_kawai_layout(G)
    nx.draw(G, pos, with_labels=True, edge_color=tuple(edge_color))
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.savefig("kruskal.png", format="PNG")
    plt.show()

def main():
    graph = [(0, 1, 6), (0, 2, 1), (0, 3, 5), (1, 2, 5), (1, 4, 3), (2, 3, 5), (2, 4, 6), (2, 5, 4), (3, 5, 2), (4, 5, 6)]
    
    mst_edges = kruskal(graph).mst()
    print(mst_edges)
        
    G = nx.Graph()
    G.add_weighted_edges_from(graph)
    draw(G, mst_edges)

if __name__ == '__main__':
    main()