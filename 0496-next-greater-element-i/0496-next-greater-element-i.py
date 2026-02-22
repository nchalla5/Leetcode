class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answers = [-1] * len(nums2)
        stack = deque()
        hashMap = defaultdict()
        for i in range(len(nums2)-1,-1,-1):
            # print(i, stack)
            hashMap[nums2[i]] = i
            while(len(stack) != 0 and stack[-1] <= nums2[i]):
                stack.pop()
            if len(stack) != 0:
                answers[i] = stack[-1]
            stack.append(nums2[i])
        # print(answers)
        solution = []
        for i in nums1:
            solution.append(answers[hashMap[i]])
        return solution


            
