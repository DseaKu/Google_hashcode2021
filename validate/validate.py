import os
import sys
import numpy

sol_filename = "e.out"
inp_filename = "e_many_teams.in"

# open solution file
input_sol = open(os.path.realpath(os.path.join(os.path.dirname(__file__)+'/'+sol_filename)),'r')
# read first line of solution file
list_ind_sol = [int(i) for i in (input_sol.readline()).split()]

# count number of teams of 2, 3 and 4 people, respectively, and perform some basic tests:
# - first line of solution file shall contain only one integer
# - other lines shall start with 2, 3 or 4
# - other lines shall start with number of entries (-1)
if len(list_ind_sol) != 1:
    sys.exit("Too many entries in line 1 of submission")

# D is the number of deliveries specified in the solution file
D = list_ind_sol[0]

# team_count holds the number of 2-, 3- and 4-person teams in the solution file
team_count = [0, 0, 0]

# read solution file from line 2
lines_sol = [[int(i) for i in line.split()] for line in input_sol.readlines() if line.strip()]


if(len(lines_sol) != D):
    sys.exit("There are " + str(len(lines_sol)) + " lines specifying delieries, but the first line states that there shall be " + str(D))

for line in lines_sol:
    if line[0] != 2 and line[0] != 3 and line[0] != 4:
        sys.exit("Number of team members does not equal 2, 3 or 4 in line " + str(lines_sol.index(line) + 2))
    if line[0] != len(line) - 1:
        sys.exit("Number of team members does not match number of pizzas delivered in line " + str(lines_sol.index(line) + 2))
    team_count[line[0]-2] += 1

# open input file
input_inp = open(os.path.realpath(os.path.join(os.path.dirname(__file__)+'/'+inp_filename)),'r')
# read first line of input file
list_ind_inp = [int(i) for i in (input_inp.readline()).split()]

# M holds the number of pizzas
M = list_ind_inp[0]

# check if the number of deliveries to 2-, 3- and 4-person teams does not exceed T2, T3 and T4, respectively
for i in range(0, 2):
    if team_count[i] > list_ind_inp[i + 1]:
        sys.exit("Deliveries to too many " + str(i + 2) + "-person teams")


pizzas = [i for line in lines_sol for i in line[1:]]

# check if pizza indices are not out of range
if max(pizzas) > M - 1:
    sys.exit("Pizza " + str(max(pizzas)) + " does not exist; there are only " + str(M) + " pizzas, indexed from 0 to " + str(M-1))
if min(pizzas) < 0:
    sys.exit("Pizza " + str(min(pizzas)) + " does not exist")

# check if each pizza is delivered to at most one team
pizza_count = [pizzas.count(i) for i in pizzas]
if max(pizza_count) > 1:
    sys.exit("Pizza " + str(pizzas[numpy.argmax(pizza_count)]) + " is delivered more than once")

# calculate score
# to do this, read ingredients
lines_inp = [[i for i in line.split()] for line in input_inp.readlines()]
score = 0
for line in lines_sol:
    ingredients = set()
    for i in line[1:]:
        ingredients.update(set(lines_inp[i][1:]))
    score += (len(ingredients)**2)

print("Datei getestet, keine Fehler gefunden. Erreichte Punktzahl: " + str(score))