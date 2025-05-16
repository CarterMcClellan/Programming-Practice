################################################################################
# Question:
################################################################################
# Implement a simple distributed cache in Python using a consistent hashing algorithm.
# Your implementation should include:
# 
# A ConsistentHash class that maps keys to cache nodes
# A DistributedCache class that uses the consistent hash to store and retrieve values
# 
# Methods to add and remove cache nodes dynamically
# 
# Your solution should:
# 
# Minimize the number of keys that need to be remapped when a node is added or removed
# Handle node failures gracefully
# Balance the load across available nodes
# 
# Example usage:
# 
# cache = DistributedCache(nodes=["node1", "node2", "node3"])
# cache.put("user:1001", user_data)
# cache.get("user:1001")
# cache.add_node("node4") # should distribute a fraction of the keys to the new node
# cache.remove_node("node2") # should redistribute only the keys that were on the removed node
################################################################################
# Solution:
################################################################################
# Consistent Hashing:
# 
# Lets start with a fairly naive hashing implementation,
# where we call hash() on the key, and insert it into a node
#
# When we add a new node to the cluster
#   we want all data which we would have expected to be on that node
#   to be on that node
#
# And when we remove a node from the cluster
#   we expect that when we query for data on that removed node
#   for it to have been shuffled to the correct replacements
#
# So how do we handle this?
#
# We need to imagine our data space on the range of all hash values
#
# 0 ... 25 ... 50 ... 75 ... 100 ... 20
#
#   n1     n2     n3     n4      n1
# 
# At present we have the a node sitting on each of these interval
#
# 00-25  -> n1
# 25-50  -> n2
# 50-75  -> n3
# 75-100 -> n4
#
# imagine we insert a new node we'd have
# 
# 0 ... 20 ... 40 ... 60 ... 80 ... 100/0 ... 20
#
#   n1     n2     n3     n4     n5        n1
# 
# 00-20  -> n1
# 20-40  -> n2
# 40-60  -> n3
# 60-80  -> n4
# 80-100 -> n5
#
# and we could use this information to go and find how all this data
# should be rebalanced.
#
# values in range (20-25) on n1 need to go to n2
# values in range (40-50) on n2 need to go to n3
# values in range (60-75) on n3 need to go to n4
# values in range (80-100) on n4 need to go to n5
#
# now lets think in reverse and imagine we are deleting a node from the cluster
# 
# 0 ... 20 ... 40 ... 60 ... 80 ... 100/0 ... 20
#
#   n1     n2     n3     n4     n5        n1
# 
# 00-20  -> n1
# 20-40  -> n2
# 40-60  -> n3
# 60-80  -> n4
# 80-100 -> n5
#
# and we are going down to
#
# 0 ... 25 ... 50 ... 75 ... 100 ... 20
#
#   n1     n2     n3     n4      n1
#
# 00-25  -> n1
# 25-50  -> n2
# 50-75  -> n3
# 75-100 -> n4
#
# and thus every node is going to be taking a bit from its successor now
class ConsistentHash:
    def __init__(self, nodes: list[str]):
        self.nodes = nodes
        self.N = len(nodes)

    def get_node(self, key: str) -> int:
        return hash(key) % self.N

    def add_node(self, node: str):
        self.nodes.append(node)
        self.N += 1

    def remove_node(self, node: str):
        self.nodes.remove(node)
        self.N -= 1

class DistributedCache:
    def __init__(self, nodes: list[str]):
        self.consistent_hash = ConsistentHash(nodes)

        # node storage
        self.nodes = {node: {} for node in nodes}

        self.node_2_idx = {node: idx for idx, node in enumerate(nodes)}
        self.idx_2_node = {idx: node for idx, node in enumerate(nodes)}

    def put(self, key: str, value: str):
        node_idx = self.consistent_hash.get_node(key)
        node = self.idx_2_node[node_idx]
        self.nodes[node][key] = value

    def get(self, key: str) -> str:
        node_idx = self.consistent_hash.get_node(key)
        node = self.idx_2_node[node_idx]
        return self.nodes[node][key]

    def add_node(self, node: str):
        # add the node
        self.consistent_hash.add_node(node)
        self.nodes[node] = {}
        self.idx_2_node[self.consistent_hash.N - 1] = node
        self.node_2_idx[node] = self.consistent_hash.N - 1

        # for each node pull the appropriate data from its predecessor
        for curr_node in self.nodes:
            to_delete = []
            for key, value in self.nodes[curr_node].items():
                new_node_idx = self.consistent_hash.get_node(key)
                new_node = self.idx_2_node[new_node_idx]
                if key in self.nodes[new_node]:
                    continue

                else:
                    to_delete.append(key)
                    self.nodes[new_node][key] = value

            for key in to_delete:
                self.nodes[curr_node].pop(key)

    def remove_node(self, node: str):
        # remove the node from consistent hashing
        # so that when we re-enumerate the data
        # it correctly rebalances
        self.consistent_hash.remove_node(node)

        node_2_idx, idx_2_node = {}, {}
        idx = 0
        for curr_node in self.nodes:
            if curr_node == node:
                continue
            node_2_idx[curr_node] = idx
            idx_2_node[idx] = curr_node
            idx += 1

        self.node_2_idx = node_2_idx
        self.idx_2_node = idx_2_node

        # re-enumerate the data
        for curr_node in self.nodes:
            to_delete = []
            for key, value in self.nodes[curr_node].items():
                new_node_idx = self.consistent_hash.get_node(key)
                new_node = self.idx_2_node[new_node_idx]

                if key in self.nodes[new_node]:
                    continue
                else:
                    to_delete.append(key)
                    self.nodes[new_node][key] = value

            for key in to_delete:
                self.nodes[curr_node].pop(key)

        # once data has been correctly reshuffled
        # remove the node from the cluster
        self.nodes.pop(node)