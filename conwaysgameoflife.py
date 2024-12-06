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

    # calculate the next simulation's cells based on current simulation's cells
    for x in range(columns):
        for y in range(rows):
            # get the neighboring coordinates
            left = (x - 1) % columns
            right = (x + 1) % columns
            above = (y - 1) % rows
            below = (y + 1) % rows

            # count the number of living neighbors
            num_neighbors = 0
            if cells[(left, above)] == living_cells:
                num_neighbors += 1 #top left neighbor is alive
            if cells[(x, above)] == living_cells:
                num_neighbors += 1 #top neighbor is alive
            if cells[(right, above)] == living_cells:
                num_neighbors += 1 #top right neighbor is alive
            if cells[(left, y)] == living_cells:
                num_neighbors += 1 #left neighbor is alive
            if cells[(right, y)] == living_cells:
                num_neighbors += 1 #right neighbor is alive
            if cells[(left, below)] == living_cells:
                num_neighbors += 1 #bottom left neighbor is alive
            if cells[(x, below)] == living_cells:
                num_neighbors += 1 #bottom neighbor is alive
            if cells[(right, below)] == living_cells:
                num_neighbors += 1 #bottom right neighbor is alive

            # set cell based on Conway's Game of Life rules
            if cells[(x, y)] == living_cells and (num_neighbors == 2 or num_neighbors == 3):
                next_sim[(x, y)] = living_cells # cell stays alive
            elif cells[(x, y)] == dead_cells and num_neighbors == 3:
                next_sim[(x, y)] = living_cells # cell becomes alive
            else:
                next_sim[(x, y)] = dead_cells # cell dies

    # pause for a moment
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("\nConway's Game of Life simulation stopped.")
        sys.exit() # exit the program when Ctrl-C is pressed