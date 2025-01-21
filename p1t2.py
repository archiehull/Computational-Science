from collections import Counter
import matplotlib.pyplot as plt
import random

def get_graph(X_vals, Y_vals):
    # Plot the movement path
    plt.figure(figsize=(8, 6))
    plt.plot(X_vals, Y_vals, marker='o', markersize=3, color='grey', linestyle='-')
    plt.title("Movement Path")
    plt.grid(True)
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.show()

# Plot the movement direction distribution
def vis_bar_diag(i, up, down, left, right, up_right, up_left, down_right, down_left):
    counts = [up, down, left, right, up_right, up_left, down_right, down_left]
    directions_list = ["Up", "Down", "Left", "Right", "Up-Right", "Up-Left", "Down-Right", "Down-Left"]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(directions_list, counts, color="skyblue", edgecolor="black")
    
    # Add percentages on top of the bars
    for bar, count in zip(bars, counts):
        percentage = (count / i) * 100
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


def get_dist_diag(i, up, down, left, right, up_right, up_left, down_right, down_left):
    print(f"\n after {i} runs")
    print(f"up= {up} down= {down} left= {left} right= {right} up-right= {up_right} up-left= {up_left} down-right= {down_right} down-left= {down_left}")
    print(f"up= {(up/i)*100:.4f}% down= {(down/i)*100:.4f}% left= {(left/i)*100:.4f}% right= {(right/i)*100:.4f}% up-right= {(up_right/i)*100:.4f}% up-left= {(up_left/i)*100:.4f}% down-right= {(down_right/i)*100:.4f}% down-left= {(down_left/i)*100:.4f}%\n")


# Initialize counters for movement directions
up = 0
down = 0
left = 0
right = 0
up_right=0
up_left=0
down_right=0
down_left=0

visit_counts = Counter()

# Position trackers
pos_X = 0
pos_Y = 0
X_vals = [0]
Y_vals = [0]

grid_size=100

# Define possible movements
directional_moves = {
    (0, 1): "Up",
    (0, -1): "Down",
    (-1, 0): "Left",
    (1, 0): "Right",

    (-1, 1): "Up-Left",  
    (1, 1): "Up-Right",  
    (-1, -1): "Down-Left", 
    (1, -1): "Down-Right", 
}

total_runs = 10000

# Perform random movements
for i in range(1, total_runs+1):
        new_move = random.choice(list(directional_moves.keys()))

        t_X = pos_X + new_move[0]
        t_Y = pos_Y + new_move[1]
        
        if -grid_size // 2 <= t_X <= grid_size // 2 and -grid_size // 2 <= t_Y <= grid_size // 2:
            pos_X += new_move[0]
            pos_Y += new_move[1]

            visit_counts[(pos_X, pos_Y)] += 1

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

            if i == 100:
                get_dist_diag(i, up, down, left, right, up_right, up_left, down_right, down_left)
                vis_bar_diag(i, up, down, left, right, up_right, up_left, down_right, down_left)
                get_graph(X_vals, Y_vals)

            # if i == 500:
            #     get_dist_diag(i, up, down, left, right, up_right, up_left, down_right, down_left)
            #     vis_bar_diag(i, up, down, left, right, up_right, up_left, down_right, down_left)
            #     get_graph(X_vals, Y_vals)

            if i == 1000:
                get_dist_diag(i, up, down, left, right, up_right, up_left, down_right, down_left)
                vis_bar_diag(i, up, down, left, right, up_right, up_left, down_right, down_left)
                get_graph(X_vals, Y_vals)

            # if i == 5000:
            #     get_dist_diag(i, up, down, left, right, up_right, up_left, down_right, down_left)
            #     vis_bar_diag(i, up, down, left, right, up_right, up_left, down_right, down_left)
            #     get_graph(X_vals, Y_vals)
        # else:
        #     break



# Print results
get_dist_diag(i, up, down, left, right, up_right, up_left, down_right, down_left)
vis_bar_diag(i, up, down, left, right, up_right, up_left, down_right, down_left)
get_graph(X_vals, Y_vals)

# Display top 5 most visited points
top_5_points = visit_counts.most_common(5)
print("Top 5 Most Visited Points:")
for point, freq in top_5_points:
    print(f"Point: {point}, Frequency: {freq}")