# Implement a simple distributed cache in Python using a consistent hashing algorithm.
# Your implementation should include:
# 
# A ConsistentHash class that maps keys to cache nodes
# A DistributedCache class that uses the consistent hash to store and retrieve values
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
# cache.get("user:1001")  # Should return the data from the appropriate node
# cache.add_node("node4")  # Should redistribute only a portion of the keys