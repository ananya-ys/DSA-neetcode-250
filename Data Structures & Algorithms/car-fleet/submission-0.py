class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Pair each car's position with its speed
        cars = list(zip(position, speed))

        # Sort cars from closest to target to farthest
        cars.sort(reverse=True)

        stack = []

        for pos, spd in cars:

            # Time needed to reach the target
            time = (target - pos) / spd

            stack.append(time)

            # If current car catches the fleet ahead,
            # merge them into one fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)