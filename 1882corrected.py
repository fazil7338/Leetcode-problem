
import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []
        t = 0

        for i, duration in enumerate(tasks):
            t = max(t, i)

            # Move all free servers into available heap
            while busy and busy[0][0] <= t:
                end, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            # If all servers are busy, wait
            if not available:
                t = busy[0][0]

                while busy and busy[0][0] <= t:
                    end, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))

            # Select the best available server
            weight, idx = heapq.heappop(available)
            ans.append(idx)

            # Mark server as busy
            heapq.heappush(busy, (t + duration, weight, idx))

        return ans
