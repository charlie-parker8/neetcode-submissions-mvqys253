class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        n = len(hand) // groupSize
        freq = defaultdict(int)
        for val in hand:
            freq[val] += 1

        for _ in range(n):
            start = min(freq.keys())
            freq[start] -= 1
            if freq[start] == 0:
                    del freq[start]
                    
            for i in range(1, groupSize):
                card = start + i
                if freq[card] < 1:
                    return False
                freq[card] -= 1
                if freq[card] == 0:
                    del freq[card]

        return True