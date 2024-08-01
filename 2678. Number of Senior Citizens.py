class Solution:
    def countSeniors(self, details: List[str]) -> int:
        age = [x for x in details if int(x[11:13]) > 60]
        return len(age)
