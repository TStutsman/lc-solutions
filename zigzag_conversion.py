class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        x = numRows-1
        res = []
        # first row = 0 + wavelength(i)
        for i in range(0, len(s), 2*x):
            res.append(s[i])

        # zipper rows = period -/+ j; where 0 < j <= numRows-2
        for j in range(x-1,0,-1): # j= 2, 1
            for i in range(x, len(s)+x, 2*x): # 3, 9, 15
                if i-j < len(s):
                    res.append(s[i-j])
                if i+j < len(s):
                    res.append(s[i+j])

        # last row = wavelength/2 + wavelength(i)
        for i in range(x, len(s), 2*x):
            res.append(s[i])
            
        return "".join(res)