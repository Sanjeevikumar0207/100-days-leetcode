# Day02_MaximumWealth.py
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        return max(sum(customer) for customer in accounts)

accounts = [[1,2,3],[3,2,2]]
print(Solution().maximumWealth(accounts))  