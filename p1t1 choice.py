import matplotlib.pyplot as plt
import random


# Plot the movement direction distribution
def vis_bar(i, up, down, left, right):
    _i = up + down + left + right
    counts = [up, down, left, right]
    directions_list = ["Up", "Down", "Left", "Right"]

    plt.figure(figsize=(8, 6))
    bars = plt.bar(directions_list, counts, color="skyblue", edgecolor="black")
    
    # Add percentages on top of the bars
    for bar, count in zip(bars, counts):
        percentage = (count / _i) * 100
        plt.text(
            bar.get_x() + bar.get_width() / 2,  # Center of the bar
            bar.get_height() + 0.5,  # Slightly above the bar
            f"{percentage:.2f}%",  # Percentage text
            ha="center", va="bottom", fontsize=10, color="black"
        )

    plt.title(f"Directional Movement Distribution - {i} runs")
    plt.xlabel("Direction")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


def get_dist(i ,up, down, left, right):
    _i = up + down + left + right
    print(f"\n after {i} runs")
    print(f"up= {up} down= {down} left= {left} right= {right}")
    print(f"up= {(up/_i)*100:.4f}% down= {(down/_i)*100:.4f}% left= {(left/_i)*100:.4f}% right= {(right/_i)*100:.4f}%\n")


def get_graph(X_vals, Y_vals):
    # Plot the movement path
    plt.figure(figsize=(8, 6))
    plt.plot(X_vals, Y_vals, marker='o', markersize=3, color='grey', linestyle='-')
    plt.title("Movement Path")
    plt.grid(True)
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.show()

# Initialize counters for movement directions
up = 0
down = 0
left = 0
right = 0

# Position trackers
pos_X = 0
pos_Y = 0
X_vals = []
Y_vals = []

grid_size=100

# Define possible movements
directional_moves = {
    (0, 1): "Up",
    (0, -1): "Down",
    (-1, 0): "Left",
    (1, 0): "Right",
}

total_runs = 10000

# Perform random movements
for i in range(total_runs):
        new_move = random.choice(list(directional_moves.keys()))
        pos_X += new_move[0]
        pos_Y += new_move[1]
        
        if -grid_size // 2 <= pos_X <= grid_size // 2 and -grid_size // 2 <= pos_Y <= grid_size // 2:
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


            # Record position
            X_vals.append(pos_X)
            Y_vals.append(pos_Y)

            if i == 100:
                vis_bar(i, up, down, left, right)
                get_dist(i, up, down, left, right)
                get_graph(X_vals, Y_vals)

            if i == 500:
                vis_bar(i, up, down, left, right)
                get_dist(i, up, down, left, right)
                get_graph(X_vals, Y_vals)

            if i == 1000:
                vis_bar(i, up, down, left, right)
                get_dist(i, up, down, left, right)
                get_graph(X_vals, Y_vals)

            if i == 5000:
                vis_bar(i, up, down, left, right)
                get_dist(i, up, down, left, right)
                get_graph(X_vals, Y_vals)
        # else:
        #     break



# Print results
vis_bar(i, up, down, left, right)
get_dist(i, up, down, left, right)
get_graph(X_vals, Y_vals)





