from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # cycle detection algorithm
        # 3 stages -> 
        # 0) Unvisited
        # -1) Currently Traversing
        # 1) Marked as NOT a Cycle
        
        # Step 1) Construct a graph from the prerequisites
        self.graph = defaultdict(list)
        for [course_a, course_b] in prerequisites:
            # in order to take course_a you must take course_b
            # b -> a
            self.graph[course_b] += [course_a]
        
        # store the state of each node
        self.visited = [0 for _ in range(numCourses)]
        
        nodes = list(self.graph.keys())
        for node in nodes:
            if self.cycleDetection(node):
                return False
            
        return True
    
    def cycleDetection(self, node):
        # we reached this node again
        # before finishing iterating through
        # its neighbors -> Cycle
        if self.visited[node] == -1:
            return True
        
        # if this node has already been
        # set to 1 -> No Cycles
        if self.visited[node] == 1:
            return False
        
        self.visited[node] = -1
        for neighbor in self.graph[node]:
            if self.cycleDetection(neighbor):
                return True
        
        self.visited[node] = 1    
        return False
