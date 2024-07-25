class Solution:
    def survivedRobotsHealths(
        self, positions: list[int], healths: list[int], directions: str
    ) -> list[int]:
        position_to_index = {
            position: index for index, position in enumerate(positions)
        }
        stack: list[int] = []
        positions.sort()

        for position in positions:

            current_index = position_to_index[position]

            if directions[current_index] == "R":
                stack.append(current_index)
            else:
                while stack and healths[current_index]:

                    last_right_index = stack.pop()

                    if healths[current_index] > healths[last_right_index]:
                        healths[last_right_index] = 0
                        healths[current_index] -= 1
                    elif healths[current_index] < healths[last_right_index]:
                        healths[current_index] = 0
                        healths[last_right_index] -= 1

                        stack.append(last_right_index)
                    else:
                        healths[current_index] = healths[last_right_index] = 0

        return [health for health in healths if health > 0]
