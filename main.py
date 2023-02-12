from collections import deque
class PriorityQueue(object):
    def __init__(self):
        self.queue = []
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    def isEmpty(self):
        return len(self.queue) == 0
    def incert(self, node):
        if len(self.queue)==0:
            self.queue.append(node)
        else:
            for x in range(0,len(self.queue)):
                if self.queue[x][1]>=node[1]:
                    self.queue.insert(x,node)
                    return 1

            self.queue.append(node)
            return 0
    def pop(self):
        return self.queue.pop(0)
    def __contains__(self, item):
        if len(self.queue) == 0:
            return 0
        else:
            for x in range(0,len(self.queue)):
                if self.queue[x][0]==item:
                    return 1
                else:
                    return 0
    def replace(self,node):
        self.queue[self.__contains__(node[0])][1]=node[1]

    
city_graph_dict={
    "Ellensburg":{"Pendleton":(168,0),"Spokane":(175,1)},
    "Spokane":{"Missoula":(199,1),"Bonners_Ferry":(112,1)},
    "Missoula":{"Helena":(111,1)},
    "Bonners_Ferry":{"West_Glacier":(176,1)},
    "Helena":{"Butte":(65,0),"Great_Falls":(91,1)},
    "West_Glacier":{"Helena":(243,0),"Great_Falls":(211,0),"Havre":(231,0)},
    "Great_Falls":{"Havre":(115,0)}
}

def ucs():
    node=("Ellensburg",0)
    finalNode="Havre"
    frontier=PriorityQueue()
    frontier.incert(node)
    visited={node[0]:node[1]}
    while not frontier.isEmpty():
        print("Padre: ",node[0],"  Costo= ",node[1])
        node=frontier.pop()
        if node[0]==finalNode:
            print("Final: ",node[0]," Costo= ",node[1])
            return 1
        visited[node[0]]=node[1]
        if city_graph_dict.__contains__(node[0]):
            for child in city_graph_dict[node[0]]:
                print("Hijo: ", child,"Costo= ",city_graph_dict[node[0]][child][0])
                if frontier.__contains__(child)==0:
                    frontier.incert((child,city_graph_dict[node[0]][child][0]))
                elif frontier.__contains__(child):
                    frontier.replace((child,city_graph_dict[node[0]][child][0]))

ucs()



