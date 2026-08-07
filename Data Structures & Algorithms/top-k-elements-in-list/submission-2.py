class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        # for n, c in count.items():
        #     freq[c].append(n)
        
        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res

        freq = [[] for i in range(len(nums) + 1)]
        dic = {}
        result = []
        for c in nums:
            dic[c] = 1 + dic.get(c, 0)
        for a, b in dic.items():
            freq[b].append(a)
        
        for i in range(len(freq) - 1,0,-1):
            for c in freq[i]:
                result.append(c)
                if len(result) == k:
                    return result