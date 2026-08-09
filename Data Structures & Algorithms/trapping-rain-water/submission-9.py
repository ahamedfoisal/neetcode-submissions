class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        # maxLeft = [0]
        # maxRight = [0]
        # sum = 0
        # for i in range(len(height) - 1):
        #     maxLeft.append(max(maxLeft[i], height[i]))
        # for i in range(len(height) - 1, 0, -1):
        #     maxRight.insert(0, (max(maxRight[0], height[i])))
        # for i in range(len(height)):
        #     sum+=max(min(maxLeft[i], maxRight[i])-height[i], 0)
        # return sum

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax > rightMax:
                r-=1
                res +=max(rightMax - height[r], 0)
                rightMax = max(rightMax, height[r])
            else:
                l += 1
                res += max(leftMax - height[l], 0)
                leftMax = max(leftMax, height[l])
        return res