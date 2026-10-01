class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid_triplets = []

        for t in triplets:
            x = t[0]
            y = t[1]
            z = t[2]

            if x <= target[0] and y <= target[1] and z <= target[2]:
                valid_triplets.append(t)

        tx = False
        ty = False
        tz = False

        for t in valid_triplets:
            if t[0] == target[0]:
                tx = True
            if t[1] == target[1]:
                ty = True
            if t[2] == target[2]:
                tz = True

        if tx and ty and tz:
            return True

        return False


            