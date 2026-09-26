class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
            - sort array
            - start l and r pointers
            - when weight fits count as valid, continue itertion until l < r is no longer true
        '''
        people.sort()
        l, r = 0, len(people) - 1
        numBoats = 0

        while l <= r:
            if l == r and people[l] <= limit:
                numBoats += 1
                break

            curr = people[l] + people[r]

            if curr > limit:
                numBoats += 1
                r -= 1
                continue


            numBoats += 1
            l += 1
            r -= 1
        
        return numBoats
