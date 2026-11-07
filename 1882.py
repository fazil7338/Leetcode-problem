import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []

        for t, duration in enumerate(tasks):

            while busy and busy[0][0] <= t:
                free_time, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            if not available:
                free_time, weight, idx = heapq.heappop(busy)
                t = max(t, free_time)

                while busy and busy[0][0] <= t:
                    ft, w, i = heapq.heappop(busy)
                    heapq.heappush(available, (w, i))

            weight, idx = heapq.heappop(available)

            ans.append(idx)

            heapq.heappush(
                busy,
                (t + duration, weight, idx)
            )

        return ans
