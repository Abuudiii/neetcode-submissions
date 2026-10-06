class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
            1. track a total of gas and cost when iterating
            2. when it becomes negative, it means we cannot reach this station from the previous stations
            3. since we already check for total gas < cost, our index i will land on the station that we can reach every other station from
        '''

        # gas  = [1,2,3,4]
        # cost = [2,2,4,1]

        if sum(gas) < sum(cost):
            return -1

        i = 0
        total = 0

        for idx, (g, c) in enumerate(zip(gas, cost)):
            total += (g - c)

            if total < 0:
                i = idx + 1
                total = 0

        return i
            