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
for x in range(columns): #looping over the columns
    for y in range(rows):  # looping over the rows
        #50/50 chance for starting cells being alive or dead
        if random.randint(0, 1) == 0:
            next_sim[(x, y)] = living_cells
        else:
            next_sim[(x, y)] = dead_cells
