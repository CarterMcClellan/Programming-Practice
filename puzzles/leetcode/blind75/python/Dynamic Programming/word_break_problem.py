from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # convert word dict into a set, so there is o(1)
        # lookup
        wordSet = set(wordDict)
        
        if s in wordDict:
            return True
        
        # looks like a graph problem
        # find a path from 0, to N
        N = len(s)
        paths = []
        
        # check all possible substrings
        for i in range(N+1):
            for j in range(i):
                if s[j:i] in wordSet:
                    paths += [(j, i)]
        
        # Construct a Graph
        # Elements of path look like (s, e)
        # 
        # Nodes in the graph are labeled: s
        # An edge exists between (s1, e1), (s2, e2)
        # if e1 equals s2 (graph is directed)
        graph = defaultdict(list)
        for (s, e) in paths:
            if s in graph:
                graph[s] += self.findNeighbors(e, paths)
            else:
                graph[s] = self.findNeighbors(e, paths)
        
        return self.bfs(graph, 0, N)
    
    def findNeighbors(self, target, paths):
        res = [target]
        for (s, e) in paths:
            if s == target:
                res += [s]
        return res
    
    def bfs(self, graph, start, finish):
        queue = graph[start]
        visited = set()
        while queue:
            curr = queue.pop(0)
            if curr in visited:
                continue
            visited.add(curr)
            
            for neighbor in graph[curr]:
                if neighbor == finish:
                    return True
                queue += [neighbor]
        
        return False
