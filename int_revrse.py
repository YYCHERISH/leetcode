class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        nums_list = []
        if x > 0:
            flag = 1
        else:
            flag = -1
        x = abs(x)
        while x != 0:
            nums_list.append(abs(x%10))
            x = x//10
        m = 0
        for i in nums_list:
            m = m*10 + i
        t = m*flag
        if -2**31 <= t <= 2**31-1:
            return t
        else:
            return 0
        
