class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        curr_hour = int(current[:2])
        corr_hour = int(correct[:2])
        total_curr = (curr_hour * 60) + int(current[3:])
        total_corr = (corr_hour * 60) + int(correct[3:])
        difference = total_corr - total_curr
        if difference < 0:
            difference += 24 * 60 
        count = 0
        operations = [60, 15, 5, 1]
        for op in operations:
            count += difference // op
            difference %= op
        return count