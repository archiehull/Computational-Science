import matplotlib.pyplot as plt
import random

# Plot the movement direction distribution
def vis_bar(i, up, down, left, right):
    counts = [up, down, left, right]
    directions_list = ["Up", "Down", "Left", "Right"]

    plt.figure(figsize=(8, 6))
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

def get_graph(X_vals, Y_vals):
    # Plot the movement path
    plt.figure(figsize=(8, 6))
    plt.plot(X_vals, Y_vals, marker='o', markersize=3, color='grey', linestyle='-')
    plt.title("Movement Path")
    plt.grid(True)
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.show()

# Gompertz model implementation
def gompertz_growth(N, k, M):
    return k * N * np.log(M / N)

def simulate_growth(N0, M, k, h, max_time=1200):
    time = 0
    N = [N0]

    while N[-1] < M * 0.66:  # Relative error condition
        dN = h * gompertz_growth(N[-1], k, M)
        N.append(N[-1]+dN)
        time += h

        if time > max_time:  # Safeguard against infinite loops
            print("Warning: Reached maximum simulation time without convergence.")
            break
    return time  # Return time taken to reach steady state



# Parameters
k = 0.006  # Growth rate
M = 10**13  # Carrying capacity
N0 = 10**9  # Initial tumor cell population
h = 0.01  # Step size
t_max = 1200  # Maximum time
time = np.arange(0, t_max, h)  # Time array

up = 0
down = 0
left = 0
right = 0
up_right=0
up_left=0
down_right=0
down_left=0

# Movement
new_X = pos_X=0
new_Y = pos_Y=0
X_vals=[]
Y_vals=[]

current_pos=0,0
new_pos=0,0

no_moves=False

XY_vals=[]

directional_moves=[(0,1),(0,-1),(1,0),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1)]

for i in range(t_max):    
    steady_time = simulate_growth(N0, M, k, h)

    # print(i)
    while(True):

        current_pos=pos_X,pos_Y

        new_move = random.choice(directional_moves)

        new_X= pos_X+new_move[0]
        new_Y= pos_Y+new_move[1]

        new_pos = new_X, new_Y

        if new_pos not in XY_vals:
            pos_X = new_X
            pos_Y = new_Y
            current_pos = new_pos
            break    

        possible_moves=[]
        new_moves=0

        for move in directional_moves:
            move = tuple(move)  
            potential_pos = (current_pos[0] + move[0], current_pos[1] + move[1])
            possible_moves.append(potential_pos)
        
        for poss in possible_moves:
            if poss not in XY_vals:
                new_moves+=1
            
        if new_moves==0:
            print("All adjacent cells are occupied. Stopping simulation")
            no_moves=True
            break

    if no_moves:
        break


    move_direction = new_move
    if move_direction == (0, 1):
        up += 1
    elif move_direction == (0, -1):
        down += 1
    elif move_direction == (-1, 0):
        left += 1
    elif move_direction == (1, 0):
        right += 1
    elif move_direction == (1, 1):
        up_right += 1
    elif move_direction == (-1, 1):
        up_left += 1
    elif move_direction == (1, -1):
        down_right += 1
    elif move_direction == (-1, -1):
        down_left += 1

    if i!=0 and i % 50 == 0:
            get_dist_diag(i, up, down, left, right, up_right, up_left, down_right, down_left)
            vis_bar_diag(i, up, down, left, right, up_right, up_left, down_right, down_left)
            get_graph(X_vals, Y_vals)
    

    X_vals.append(pos_X)
    Y_vals.append(pos_Y)
    XY_vals.append(new_pos)

    

print(f"Final cell {pos_X},{pos_Y}")
get_dist_diag(i, up, down, left, right, up_right, up_left, down_right, down_left)
vis_bar_diag(i, up, down, left, right, up_right, up_left, down_right, down_left)
get_graph(X_vals, Y_vals)
