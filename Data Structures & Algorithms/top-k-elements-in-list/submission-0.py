class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for num in nums:
            m[num] = m.get(num, 0) + 1

        # buckets[i] = list of numbers that appear exactly i times
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in m.items():
            buckets[freq].append(num)

        result = []
        for freq in range(len(buckets) - 1, 0, -1):  # walk from highest freq down
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result