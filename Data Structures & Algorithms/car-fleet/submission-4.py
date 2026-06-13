class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_sorted = sorted(position, reverse=True)
        p_s = {}
        for i in range(len(position)):
            p_s[position[i]] = speed[i]

        t_stack = []

        for pos in p_sorted:
            t = (target - pos) / p_s[pos]

            if not t_stack or t > t_stack[-1]:
                t_stack.append(t)

        return len(t_stack)

