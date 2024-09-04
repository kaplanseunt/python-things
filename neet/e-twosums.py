class SolutionTwoSums:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i
        return


"""
nums = [10, 20, 30, 40]

for i, n in enumerate(nums):
    print(f"İndeks: {i}, Değer: {n}")
**
İndeks: 0, Değer: 10
İndeks: 1, Değer: 20
İndeks: 2, Değer: 30
İndeks: 3, Değer: 40


"""

class SolutionValidPandrome:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr +=c.lower()
        return newStr == newStr[::-1]

