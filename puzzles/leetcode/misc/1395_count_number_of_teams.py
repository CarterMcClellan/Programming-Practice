# there is a very trivial o n^3 solution
#
# for i in range(N):
#     for j in range(i, N):
#         for k in range(j, N):
#             pass

# [2, 5, 3, 4, 1]
# 
# [2, 5, 3]
# [2, 5, 4]
# [2, 5, 1]
# 
# [2, 3, 4]
# [2, 3, 1]
# 
# [2, 4, 1]
#
# [5, 3, 4]

# it would be kind of nice if we could say something like
# "oh there k values greater than j starting at index f"
# 
# the first half we could get from a sort. then the inner loop
# could be log n to find the index of the element in the sorted
# array which is greater, but we dont know that their indices are greater
# so not quite what we are looking for. 
#
# ok but sorting here still feels relevant. if we sort the array first
# could we then do an easy traversal to find what we are looking for
# [(1,4), (2,0), (3,2), (4,3), (5,1)]
#
# we are looking for a value greater than 4 amongst the remaining
# [(2,0), (3,2), (4,3), (5,1)]
#
# no, but this still feels like o n^3, the inner loop is now checking
# for the right indices...
#
# is there a way we can think of this problem like a graph?
#   draw an edge between every node and the node which is in front of
#   it (if the node is also greater)
#
# enque all the nodes in the graph as starts for the path
# if the len of the path is 3 pop, otherwise enqueue all of the
# neighbors.
#
# we don't actually have to enque all the neighbors we can increment the
# sum by the number of neighbors for the len 2 node.

# graph construction is o (n^2)

# lets think through the exploration thing
# for n in nums: # o(n)
#   successor_n = graph[n]
#   for succ in successor_n: # o(n)
#       ans += len(graph[succ_n])

# so I think this soluton is o (n^2)

# note that we will have to repeat this construction for descending
# ok lets try it
# nums = [2,5,3,4,1]

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        ans = 0

        # count up
        graph = {}
        for i in range(N):
            i_val = rating[i]
            for j in range(i, N):
                val = rating[j]
                if i_val < val:
                    graph[i] = graph.get(i, []) + [j]

        for i in range(N):
            successors = graph.get(i, [])
            for s in successors:
                ans += len(graph.get(s, []))

        # count down
        graph_down = {}
        for i in range(N-1, -1, -1):
            i_val = rating[i]
            for j in range(i, -1, -1):
                val = rating[j]
                if i_val < val:
                    graph_down[i] = graph_down.get(i, []) + [j]

        for i in range(N):
            successors = graph_down.get(i, [])
            for s in successors:
                ans += len(graph_down.get(s, []))

        return ans