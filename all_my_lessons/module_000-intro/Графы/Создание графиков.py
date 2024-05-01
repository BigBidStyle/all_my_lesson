import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_node(1)   # Добавление одного узла.
G.add_nodes_from([2, 3]) # Добавление нескольких узлов одновременно.
# Добавление узлов вместе с атрибутами.
G.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),
])

H = nx.path_graph(10)
G.add_nodes_from(H)
G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam")        # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')

list(G.nodes)
[1, 2, 3, 'spam', 's', 'p', 'a', 'm']
list(G.edges)
[(1, 2), (1, 3), (3, 'm')]
list(G.adj[1])  # or list(G.neighbors(1))
[2, 3]
G.degree[1]  # the number of edges incident to 1
G.edges([2, 'm'])
EdgeDataView([(2, 1), ('m', 3)])
G.degree([2, 3])
DegreeView({2: 1, 3: 2})
# Визуализация графа
nx.draw(G, with_labels="Тестовая визуализация графа", node_color='lightblue', edge_color='gray')
plt.show()