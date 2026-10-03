import time


class RateLimiter:
    def __init__(self, limit, window):
        self.limit = limit
        self.window = window
        self.requests = {}

    def allow_request(self, client_id):
        now = time.time()

        requests = self.requests.get(client_id, [])

        requests = [
            timestamp
            for timestamp in requests
            if now - timestamp < self.window
        ]

        if len(requests) >= self.limit:
            self.requests[client_id] = requests
            return False

        requests.append(now)
        self.requests[client_id] = requests

        return True


if __name__ == "__main__":
    limiter = RateLimiter(limit=3, window=10)

    for i in range(5):
        print(f"Request {i + 1}: {limiter.allow_request('user-1')}")