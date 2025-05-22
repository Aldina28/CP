class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        current = 0 
        start = 0
        for i in range(len(gas)):
            current += (gas[i]-cost[i])
            if current<0:
                start  = i+1
                current = 0
        return start