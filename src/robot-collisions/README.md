# Intuition

To solve the problem of determining the health of surviving robots after all collisions, we need to consider the positions and directions of robots. Robots moving in the same direction will not collide, so we only need to handle collisions between robots moving towards each other.

# Approach

1. **Initialize variables**:
    - Create a mapping from `positions` to their respective indices to keep track of original indices after sorting.
    - Create a `stack` to keep track of robots' movements.
2. **Sort positions**: Sort the `positions` to simulate the movement from left to right.
3. **Handle collision**: If a robot moving left collides with a robot moving right, compare their `healths`:
        - The robot with higher health will survive and lose 1 health.
        - The robot with lower health will be destroyed.
        - If both have the same health, both will be destroyed.
4. **Filter Survivors**: Filter out robots with health greater than zero after processing all `positions`.

# Complexity

- Time complexity: The time complexity of this solution is $O(n \log n)$ where $n$ is the number of robots. This is because we are sorting the positions list which takes $O(n \log n)$ time.

- Space complexity: The space complexity is $O(n)$ because we use a stack to track the robots moving to the right.

# Code

```python
class Solution:
    def survivedRobotsHealths(
        self, positions: list[int], healths: list[int], directions: str
    ) -> list[int]:
        # Create a mapping from positions to their respective indices
        position_to_index = {
            position: index for index, position in enumerate(positions)
        }

        # Create a stack to keep track of collisions
        stack: list[int] = []

        # Sort the positions to simulate the movement from left to right
        positions.sort()

        for position in positions:

            # Get the index of the current position
            current_index = position_to_index[position]

            # Handling collisions:
            if directions[current_index] == "R":
                stack.append(current_index)
            else:
                while stack and healths[current_index]:

                    # Get the last robot moving to the right
                    last_right_index = stack.pop()

                    # Determine the outcome of the collision
                    if healths[current_index] > healths[last_right_index]:
                        healths[last_right_index] = 0
                        healths[current_index] -= 1
                    elif healths[current_index] < healths[last_right_index]:
                        healths[current_index] = 0
                        healths[last_right_index] -= 1

                        # Re-add the right-moving robot to the stack
                        stack.append(last_right_index)
                    else:
                        healths[current_index] = healths[last_right_index] = 0

        # Filter out robots with health greater than zero
        return [health for health in healths if health > 0]
```
