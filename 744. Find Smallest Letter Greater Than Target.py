class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in range(len(letters)):
            if letters[i] > target and i != 0 and letters[i-1] <= target:
                return letters[i]

        return letters[0]
