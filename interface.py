from neo4j import GraphDatabase

class Interface:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password), encrypted=False)
        self._driver.verify_connectivity()

    def close(self):
        self._driver.close()

    def bfs(self, start_node, last_node):
        # TODO: Implement this method
        #creating an in memory graph query:
        in_memory_graph_query = """ 
            CALL gds.graph.project.cypher(
                'myInMemoryGraph',
                'MATCH (pickup:Location) RETURN id(pickup) AS id',
                'MATCH (pickup:Location)-[trip:TRIP]->(dropoff:Location) RETURN id(pickup) AS source, id(dropoff) AS target, trip.distance AS distance'
        )"""


        with self._driver.session() as session:
            try:
                flag = session.run("RETURN gds.graph.exists('myInMemoryGraph') as flag").data()[0]
                if(flag['flag'] == False):
                    #creating an in memory graph
                    print("\nCreating an in memory graph called myInMemoryGraph")
                    session.run(in_memory_graph_query)
                    print("Graph Created Successfully")
                    
                else:
                    print("\nmyInMemoryGraph already exists")
                #running BFS query 
                result = session.run("""
                    MATCH (a:Location{name: $start}), (d:Location{name: $last})
                    CALL gds.bfs.stream('myInMemoryGraph', {
                    sourceNode: id(a),
                    targetNodes: [id(d)]
                    })
                    YIELD path
                    RETURN path
                """, start=start_node, last=last_node)
                # Extract the data from the result
                path = result.data()
                print("\nPath: ", path)
                #return the path
                return path
            
            except :
                raise NotImplementedError

    def pagerank(self, max_iterations, weight_property):
        # TODO: Implement this method

        #creating an in memory graph query:
        in_memory_graph_query = """ 
            CALL gds.graph.project.cypher(
                'myInMemoryGraph',
                'MATCH (pickup:Location) RETURN id(pickup) AS id',
                'MATCH (pickup:Location)-[trip:TRIP]->(dropoff:Location) RETURN id(pickup) AS source, id(dropoff) AS target, trip.distance AS distance'
        )"""
        

        with self._driver.session() as session:
            try:
                #check if the graph already exists
                flag = session.run("RETURN gds.graph.exists('myInMemoryGraph') as flag").data()[0]
                if(flag['flag'] == False):
                    #creating an in memory graph
                    print("\nCreating an in memory graph called myInMemoryGraph")
                    session.run(in_memory_graph_query)
                    print("Graph Created Successfully")
                    print("Running page rank algorithm")
                else:
                    print("\nmyInMemoryGraph already exists")
                
                #fecthing highest rank 
                highest = session.run("""
                    CALL gds.pageRank.stream('myInMemoryGraph', {
                    maxIterations: $max_iter,
                    dampingFactor: 0.85,
                    relationshipWeightProperty: $prop})
                    YIELD nodeId, score
                    RETURN gds.util.asNode(nodeId).name AS name, score
                    ORDER BY score DESC, name ASC
                    LIMIT 1 """, max_iter = max_iterations, prop = weight_property).data()[0]
                
                #fetching least rank
                lowest =session.run("""
                    CALL gds.pageRank.stream('myInMemoryGraph', {
                    maxIterations: $max_iter,
                    dampingFactor: 0.85,
                    relationshipWeightProperty: $prop})
                    YIELD nodeId, score
                    RETURN gds.util.asNode(nodeId).name AS name, score
                    ORDER BY score ASC, name ASC
                    LIMIT 1 """, max_iter = max_iterations, prop = weight_property).data()[0]
                
                #print the results.
                print("\nResults: \n")
                print("Highest: ", highest)
                print("Lowest: ", lowest)
                result = []
                result.append(highest)
                result.append(lowest)
                return result

            except :
                raise NotImplementedError

