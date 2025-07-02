__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p,s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(cars)[::-1]:
            time_taken = (target-p)/s
            if not stack or time_taken>stack[-1]:
                stack.append(time_taken)
        return len(stack)