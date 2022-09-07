

class Node:
    def __init__(self):
        self.inDegree = 0
        self.outNodes = []
        

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        from collections import defaultdict, deque
        
        graph = defaultdict(Node)
        
        totalDeps = 0
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].inDegree += 1
            totalDeps += 1
            
        nodepCourses = deque()
        for index, node in graph.items():
            if node.inDegree == 0:
                nodepCourses.append(index)
                
        removeEdges = 0
        while nodepCourses:
            
            course = nodepCourses.pop()
            
            for nextCourse in graph[course].outNodes:
                graph[nextCourse].inDegree -= 1
                removeEdges += 1
                
                if graph[nextCourse].inDegree == 0:
                    nodepCourses.append(nextCourse)
            
        if removeEdges == totalDeps:
            return True
        else:
            return False
                    
        
        