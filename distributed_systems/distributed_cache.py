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
# cache.get("user:1001")
# cache.add_node("node4") # should distribute a fraction of the keys to the new node
# cache.remove_node("node2") # should redistribute only the keys that were on the removed node

class ConsistentHash:
    def __init__(self, nodes: list[str]):
        pass

    def get_node(self, key: str) -> str:
        pass

class DistributedCache:
    def __init__(self, nodes: list[str]):
        self.consistent_hash = ConsistentHash(nodes)

        # node storage
        self.nodes = {node: {} for node in nodes}

    def put(self, key: str, value: str):
        pass

    def get(self, key: str) -> str:
        pass

    def add_node(self, node: str):
        pass

    def remove_node(self, node: str):
        pass

def main():
    cache = DistributedCache(nodes=["node1", "node2", "node3"])

    # verify basic retrieval
    cache.put("user:1001", "hello world")
    user_data = cache.get("user:1001")
    assert user_data == "hello world"

    # try adding data then deleting the node which it is on
    cache.put("user:1002", "foo bar")
    cache.add_node("node4")
    cache.remove_node("node1")
    cache.remove_node("node2")
    cache.remove_node("node3")

    user_data = cache.get("user:1002")
    assert user_data == "foo bar"