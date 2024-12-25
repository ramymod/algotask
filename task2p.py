'''
a.
    = Kruskal's algorithm    
        1- Sort the edges of the graph in non-decreasing order of their weights.
        2- Initialize a forest where each vertex is its own separate tree.
        3- Iterate through the sorted edges:
            - If the edge connects two disjoint sets (no cycle is formed), include it in the MST.
            - Use the Union-Find data structure to check and merge sets efficiently.
        4- Repeat until ∣V∣−1 edges are added to the MST, where ∣V∣ is the number of vertices.

    # ===Pseudocode for Kruskal's Algorithm===
        KRUSKAL(G):
        MST = {}
        SORT the edges of G by weight
        MAKE-SET(v) for all vertices v in G

        for each edge (u, v) in sorted edges:
            if FIND-SET(u) != FIND-SET(v):   // u and v are in different sets
                MST = MST ∪ {(u, v)}
                UNION(u, v)

            if size(MST) == |V| - 1:
                break

        return MST
    # =======================================

    = Auxiliary Algorithm
        - MAKE-SET: Initialize each vertex as its own set.
        - FIND-SET: Find the root of the set containing a vertex (with path compression for efficiency).
        - UNION: Merge two sets (using rank to minimize tree height).

    # ===Pseudocode for Auxiliary's Algorithm===
        MAKE-SET(x):
            parent[x] = x
            rank[x] = 0

        FIND-SET(x):
            if parent[x] != x:
                parent[x] = FIND-SET(parent[x])  // Path compression
            return parent[x]

        UNION(x, y):
            rootX = FIND-SET(x)
            rootY = FIND-SET(y)

            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
            rank[rootX] += 1
    # ==========================================

'''


'''
b.

    1. Time Complexity
        - Sorting the Edges: O(ElogE), where E is the number of edges.
        - Union-Find Operations: Each FIND-SET and UNION operation takes O(α(V)), where α is the inverse Ackermann function. For V vertices and E edges, this is nearly constant in practice.
        - Overall Time Complexity: O(ElogE+Eα(V)), which simplifies to O(ElogE).
    2. Space Complexity
        Storage for edges and parent/rank arrays: O(V+E).
    3. Optimality
        Kruskal's algorithm is optimal for sparse graphs due to its edge-centric approach.
    4. Applicability
        - Works well for undirected, weighted graphs.
        - Cannot handle disconnected graphs unless each connected component is considered separately.
'''


# c.

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.edges = []    # List to store edges

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))  # Store edges as (weight, u, v)

    def find_set(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find_set(parent, parent[i])  # Path compression
        return parent[i]

    def union(self, parent, rank, x, y):
        rootX = self.find_set(parent, x)
        rootY = self.find_set(parent, y)

        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

    def kruskal(self):
        self.edges.sort()  # Sort edges by weight
        parent = []
        rank = []
        mst = []

        # Initialize Union-Find
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Process edges
        for weight, u, v in self.edges:
            rootU = self.find_set(parent, u)
            rootV = self.find_set(parent, v)

            if rootU != rootV:  # If no cycle is formed
                mst.append((u, v, weight))
                self.union(parent, rank, rootU, rootV)

            if len(mst) == self.V - 1:
                break

        return mst

# Example Usage
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

mst = g.kruskal()
print("Edges in MST:")
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")