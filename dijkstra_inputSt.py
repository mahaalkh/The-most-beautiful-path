import pqdict
import parse

def dijkstra(graph, source, target=None):
    """
    Computes the shortests paths from a source vertex to every other vertex in
    a graph

    """
    # The entire main loop is O( (m+n) log n ), where n is the number of
    # vertices and m is the number of edges. If the graph is connected
    # (i.e. the graph is in one piece), m normally dominates over n, making the
    # algorithm O(m log n) overall.

    dist = {}   
    pred = {}

    # Store distance scores in a priority queue dictionary
    pq = pqdict.PQDict()
    for node in graph:
        if node == source:
            pq[node] = 0
        else:
            pq[node] = float('inf')

    # Remove the head node of the "frontier" edge from pqdict: O(log n).
    for node, min_dist in pq.iteritems():
        # Each node in the graph gets processed just once.
        # Overall this is O(n log n).
        dist[node] = min_dist
        if node == target:
            break

        # Updating the score of any edge's node is O(log n) using pqdict.
        # There is _at most_ one score update for each _edge_ in the graph.
        # Overall this is O(m log n).
        for neighbor in graph[node]:
            if neighbor in pq:
                new_score = dist[node] + graph[node][neighbor]
                if new_score < pq[neighbor]:
                    pq[neighbor] = new_score
                    pred[neighbor] = node

    return dist, pred

def shortest_path(graph, source, target):
    dist, pred = dijkstra(graph, source, target)
    end = target
    path = [end]
    while end != source:
        end = pred[end]
        path.append(end)        
    path.reverse()
    return path

ggggg = parse.getGraph()
Graph = ggggg[0]
SN = ggggg[1]
##Graph = input('Enter Graph - with distances "example: {"a":{"b": 12.00},  "b": {"a": 11.99}} : ')
print('Graph', str(Graph))

GraphB = input('Enter Graph - with beauty "example: {"a":1.00(very beautiful),  "b":x(not beautiful) x < 100.00}" : ')
print('Graph Beauty ', str(GraphB))

StartNode = input('Enter "StartNode": ')
print('StartNode', StartNode)

EndNode = input('Enter "EndNode": ')
print('EndNode', EndNode)

## increments the edge weights by the beauty on the node


newGraph={}
for key in Graph.keys():
    newGraph[key]={};
    for keykey in Graph[key]:
        if  isinstance(GraphB.get(key),float):
            newGraph[key][keykey]= float(GraphB.get(key)) + Graph[key][keykey]
        else:
            newGraph[key][keykey] =  Graph[key][keykey] + 100.00
print newGraph
                                           
## get the physical length of the path

sspp = shortest_path(newGraph, StartNode, EndNode)

dddd = 0
for iiii in range(len(sspp) - 1):
    dddd += Graph[sspp[iiii]][sspp[iiii+1]]


nnmm = []
for iiii in range(len(sspp) - 1):
    nnmm.append(SN[sspp[iiii]][sspp[iiii+1]])


if __name__ == '__main__':
    
    # A simple edge-labeled graph using a dict of dicts
    graph = newGraph

    dist, path = dijkstra(graph, source = StartNode)
    print "dist from: " + StartNode + ":" + str(dist)
    print "path : " + str(path)
    print "shortest_path: " + str(sspp)
    print "beauty weighted distance: " + str(dist[EndNode])
    print "physical world distance: " + str(dddd) + " meters"
    print "street names: " + str(nnmm) 
    
    
