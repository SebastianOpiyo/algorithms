# Graph Representation

- Graph is a data structure that consists of the following 2 components:
    1. finite set of vertices(nodes)
    2. finite set of ordered pair of form(u, v) called edges.
    Note:
    - edges may contain weight/value/cost
    - edges may be directed/undirected.
- The 2 most used graph representation include:
    --> Adjacency matrix
    --> Adjacency list
    --> Others include incidence Matric/List
- The choice of graph use is situation specific.

## Adjacency Matrix
- Is a 2D array of size VxV (v is the number of nodes/vertices in a graph)
- the 2D array will be adj[][], a slot will be adj[i][j]=1/0 (1 indicates existence of an edge from v[i] to v[j] and 0 indicates otherwise.)
- adjacency matrix for undirected graph is always symmetric. 
- adjacency matrix is also used to represent weighted graphs. i.e adj[i][j] = w (there is an edge from vertex i-j with weight=w)

** Pros: Representation is easier to implement and follow. Removing an edge takes O(1) time. Queries like whether there is an edge from vertex ‘u’ to vertex ‘v’ are efficient and can be done O(1).

** Cons: Consumes more space O(V^2). Even if the graph is sparse(contains less number of edges), it consumes the same space. Adding a vertex is O(V^2) time.
Please see this for a sample Python implementation of adjacency matrix.