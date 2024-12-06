import copy, random, time, sys

# Ctrl+C to stop the simulations

# representing living and dead cells
living_cells = "+"
dead_cells = "."

# setting up the cell grid variables
rows = 79
columns = 20

next_sim = {}

# put random dead and alive cells into next_sim
for x in range(columns):  # looping over the columns
    for y in range(rows):  # looping over the rows
        # 50/50 chance for starting cells being alive or dead
        if random.randint(0, 1) == 0:
            next_sim[(x, y)] = living_cells  # add a living cell
        else:
            next_sim[(x, y)] = dead_cells  # add a dead cell

# main loop
while True:
    # clear the screen
    print("\n" * 50)
    cells = copy.deepcopy(next_sim)

    # print the cells
    for y in range(rows):
        for x in range(columns):
            print(cells[(x, y)], end="")
        print()
    print("Press Ctrl-C to stop.")
    
