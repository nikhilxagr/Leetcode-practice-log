# 657. Robot Return to Origin
# revised 
# There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

# You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

# Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

# Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

# Example 1:

# Input: moves = "UD"
# Output: true
# Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
# Example 2:

# Input: moves = "LL"
# Output: false
# Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.

# Solution:

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0

        for move in moves:
            if move == 'R':
                x += 1
            elif move == 'L':
                x -= 1
            elif move == 'U':
                y += 1
            elif move == 'D':
                y -= 1

        return x == 0 and y == 0
    
# Algorithm:
# 1. Initialize two variables, x and y, to keep track of the robot's position on the 2D plane. Start both at 0.
# 2. Iterate through each move in the input string moves.
# 3. For each move, update the x and y coordinates based on the direction of the move:
#    - If the move is 'R', increment x by 1.    
#    - If the move is 'L', decrement x by 1.
#    - If the move is 'U', increment y by 1.
#    - If the move is 'D', decrement y by 1.
# 4. After processing all moves, check if the robot has returned to the origin by verifying if both x and y are equal to 0.
# 5. Return true if the robot is at the origin, otherwise return false.