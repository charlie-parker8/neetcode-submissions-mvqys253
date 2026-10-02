class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_idx = {}
        for i in range(len(s)):
            end_idx[s[i]] = i

        res = []
        l = 0
        r = end_idx[s[0]]

        while r < len(s):
            k = l
            while k < r:
                r = max(end_idx[s[k]], r)
                k += 1
            
            res.append(r - l + 1)
            l = r + 1
            r = end_idx[s[l]] if l < len(s) else r + 1

        return res