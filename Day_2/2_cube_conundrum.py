"""
Day 2: Cube Conundrum
Author: dnicolauit
Date: 2023-12-02
Answer 1: 
Answer 2: 
"""

# Part 1
data = open("Day_2/2_cube_conundrum_data.txt").read().splitlines()
data_dict={key: [] for key in range(1,len(data)+1)}
colors = {
    'red': 0,
    'green': 1,
    'blue': 2
}
limits = [12,13,14]
for i in range(len(data)):
    line =data[i].split(':')[1]
    for j in line.split(';'):
        got_balls = [0,0,0]
        for w in j.split(','):
            balls, color = w.split()
            balls = int(balls)
            # Array format [red, green, blue]
            got_balls[colors[color]] = balls
        data_dict[i+1].append(got_balls)

solution = 0

for key in data_dict.keys():

    if all(all(val <=limits[i] for i, val in enumerate(data)) for data in data_dict[key]):
        solution += key

print('Part 1 solution:',solution)
