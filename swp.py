edgeFilename = 'edges.txt'

def loadGraph(edgeFilename):
    l1=[]
    l2=[]
    d={}
    read_file = open(edgeFilename,'r')

    # d = {}
    # for line in open(edgeFilename):
    #     l1, l2 = line.split()
    #     d[l1] = str(l2)
    # print (d)

    split = [line.split() for line in read_file]
    for line in split:

        l1.append(line[0].strip())

        l2.append(line[1].strip())

    # d = dict(zip(l1,l2))
    # # l1, l2 = zip(*d)
    nodes = set(l1+l2)
    n = len(nodes)

    adjList = [[] for node in nodes] #range(n)

    for i in range(len(l1)):
        newl1 = int(l1[i])
        newl2 = int(l2[i])
        adjList[newl1].append(newl2)
        adjList[newl2].append(newl1)

    # print("Adjacency list: ")
    # for i in range(len(adjList)):
    #     print(i, ":", adjList[i])

    return adjList

# loadGraph(edgeFilename)

class MyQueue(object):
    def __init__(self, size):
        self.queue = []
        self.size = size

    def __str__(self):
        MyString = ' '.join(str(i) for i in self.queue)
        return MyString

    def enqueue(self, item):
        if(self.Full() != True):
            self.queue.insert(0, item)
        else:
            print('Full Q')

    def dequeue(self):
        if(self.Empty() != True):
            return self.queue.pop()
        else:
            print('Empty Q')

    def Empty(self):
        return self.queue == []

    def Full(self):
        return len(self.queue) == self.size


def bfs(graph, start):
    # keep track of all visited nodes    
    visited = [False] * (len(graph))
    distance_list = [0] * (len(graph))
    # keep track of nodes to be checked
    queue = [start]
    visited[start] = True
    # queue = MyQueue(start)
    # keep looping until there are nodes still to be checked
    distance_list[start] = 0
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)

        distance = distance_list[node]

        neighbors = graph[node]

        # add neighbours of node to queue
        for i in neighbors:
            if visited[i] == False:
                distance_list[i] = distance + 1
                queue.append(i)
                visited[i] = True

    return distance_list

def distanceDistribution(G):
    histogram = [0] * (len(G))

    for i in range(len(G)):
        print("Calculating Distance From", i)
        distance_list = bfs(G, i)

        for d in distance_list:
            histogram[d] += 1

    # calculate percent
    sum = 0
    for h in histogram:
        sum += h

    for i in range(len(histogram)):
        histogram[i] /= sum

    return histogram

histogram = distanceDistribution(loadGraph(edgeFilename))
print(histogram)