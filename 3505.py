class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        ans = 0
        while i > 0:
            ans += self.tree[i]
            i -= i & -i
        return ans

    def kth(self, k):
        idx = 0
        step = 1 << (self.n.bit_length() - 1)

        while step:
            nxt = idx + step
            if nxt <= self.n and self.tree[nxt] < k:
                idx = nxt
                k -= self.tree[nxt]
            step >>= 1

        return idx + 1


class Solution:
    def minOperations(self, nums, x, k):
        from bisect import bisect_left, bisect_right

        n = len(nums)
        values = sorted(set(nums))
        m = len(values)

        count = Fenwick(m)
        sums = Fenwick(m)

        def add(v, delta):
            p = bisect_left(values, v) + 1
            count.update(p, delta)
            sums.update(p, v * delta)

        def get_cost():
            mid = count.kth((x + 1) // 2)
            median = values[mid - 1]

            p = bisect_right(values, median)

            lc = count.query(p)
            ls = sums.query(p)
            ts = sums.query(m)

            rc = x - lc
            rs = ts - ls

            return median * lc - ls + rs - median * rc

        costs = []

        for i in range(n):
            add(nums[i], 1)

            if i >= x:
                add(nums[i - x], -1)

            if i >= x - 1:
                costs.append(get_cost())

        INF = float('inf')

        dp = [[INF] * (n + 1) for _ in range(k + 1)]

        for i in range(n + 1):
            dp[0][i] = 0

        for j in range(1, k + 1):
            for i in range(1, n + 1):
                dp[j][i] = dp[j][i - 1]

                if i >= x:
                    dp[j][i] = min(
                        dp[j][i],
                        dp[j - 1][i - x] + costs[i - x]
                    )

        return dp[k][n]
