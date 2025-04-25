# Implement a class `RateLimiter` that limits the number of requests a client can make within a time window.
# 
# The class should have:
# - A constructor that takes `max_requests` and `time_window_seconds`
# - A method `allow_request(client_id)` that returns True if the request is allowed and False otherwise
# 
# Your implementation should:
# 1. Support multiple clients with different rate limits
# 2. Be efficient in both time and space complexity
# 3. Handle edge cases like clock drift
# 4. Clean up expired request records
# 
# Example usage:
# limiter = RateLimiter(max_requests=5, time_window_seconds=60)
# limiter.allow_request("client1")  # Returns True
# ... 4 more requests from client1 within 60 seconds
# limiter.allow_request("client1")  # Returns False
# limiter.allow_request("client2")  # Returns True