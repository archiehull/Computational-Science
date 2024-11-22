import matplotlib.pyplot as plt
import random

# Initialize counters for movement directions
up = 0
down = 0
left = 0
right = 0
up_right = 0
up_left = 0
down_right = 0
down_left = 0

# Position trackers
pos_X = 0
pos_Y = 0
X_vals = []
Y_vals = []

# Define possible movements
directional_moves = {
    (0, 1): "Up",
    (0, -1): "Down",
    (-1, 0): "Left",
    (1, 0): "Right",
    (1, 1): "Up-Right",
    (-1, 1): "Up-Left",
    (1, -1): "Down-Right",
    (-1, -1): "Down-Left",
}

# Perform random movements
for i in range(10000):
    new_move = random.choice(list(directional_moves.keys()))
    pos_X += new_move[0]
    pos_Y += new_move[1]
    
    # Update counters
    move_direction = directional_moves[new_move]
    if move_direction == "Up":
        up += 1
    elif move_direction == "Down":
        down += 1
    elif move_direction == "Left":
        left += 1
    elif move_direction == "Right":
        right += 1
    elif move_direction == "Up-Right":
        up_right += 1
    elif move_direction == "Up-Left":
        up_left += 1
    elif move_direction == "Down-Right":
        down_right += 1
    elif move_direction == "Down-Left":
        down_left += 1

    # Record position
    X_vals.append(pos_X)
    Y_vals.append(pos_Y)

# Print results
print(f"up= {up} down= {down} left= {left} right= {right}")
print(f"up_right= {up_right} down_right= {down_right} up_left= {up_left} down_left= {down_left}")

# Plot the movement path
plt.figure(figsize=(8, 6))
plt.plot(X_vals, Y_vals, marker='o', markersize=3, color='grey', linestyle='-')
plt.title("Movement Path")
plt.grid(True)
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.show()

# Plot the movement direction distribution
counts = [up, down, left, right, up_right, up_left, down_right, down_left]
directions_list = ["Up", "Down", "Left", "Right", "Up-Right", "Up-Left", "Down-Right", "Down-Left"]

plt.figure(figsize=(8, 6))
plt.bar(directions_list, counts, color='skyblue')
plt.title("Directional Movement Distribution")
plt.xlabel("Direction")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
