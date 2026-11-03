class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1

        while (current := numbers[index1] + numbers[index2]) != target:
            if current < target:
                index1 += 1
            else:
                index2 -= 1

        return [index1 + 1, index2 + 1]

        