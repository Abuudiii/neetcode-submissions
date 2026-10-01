class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Input: hand = [1,2,4,2,3,5,3,4], groupSize = 4
        freq = Counter(hand)
        hand.sort()

        '''
            - go through each num, try and form group size windows
            - if we can't, return False immediately
            - return True at the end
        '''

        count = groupSize
        for num in hand:
            if freq[num] < 1:
                continue

            length = 0

            while count:
                if num + length not in freq or freq[num + length] < 1:
                    return False

                freq[num + length] -= 1
                count -= 1
                length += 1

            count = groupSize

        return True


