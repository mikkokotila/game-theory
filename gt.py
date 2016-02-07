#!/usr/bin/python
import time
import random

# starting turn and per turn cost for players

turn = 0
tax_rate = 0.3
cost_of_living = 0.05
players = 2
service_cost = 0.01
minimum = 1
gdp = 1
demand = 1

# productivity and resource settings

productivity = 1
current_account = 100
motivation_adjustment = 0.01

# player one starting settings

p1_productivity = 1
p1_bank = 0
p1_motivation = 1
# p1_give = 0.4

# player two starting settings

p2_productivity = 1
p2_bank = 0
p2_motivation = 1
# p2_give = 0.3

# extra configuration values initialised

total_last_resources = 99
p1_thisround = 0 
p1_lastround = 0
p2_thisround = 0 
p2_lastround = 0
gdplastround = 1

# game starts 

# user input for contribution levels is collected

p1_give = input("What ratio will player 1 give back at : ")
p2_give = input("What ratio will player 2 give back at : ")
sleeptime = input("Delay in seconds between rounds : ")

while (current_account - total_last_resources) > 0.01 or current_account > minimum:
	turn = turn + 1

# set randomness factor for both players

	p1_random = round(random.uniform(0.9, 1.1), 3)
	p2_random = round(random.uniform(0.9, 1.1), 3)


# adjusting the cost of living for the round 

	cost_of_living = cost_of_living * (gdp / gdplastround)

# player 1 cost of living reduction 
	
	if p1_bank >= cost_of_living * p1_random:
		p1_bank = p1_bank - cost_of_living * p1_random
	elif p1_bank < cost_of_living * p1_random:
		current_account = current_account - cost_of_living * p1_random

# player 2 cost of living reduction 

	if p2_bank >= cost_of_living * p2_random:
		p2_bank = p2_bank - cost_of_living * p2_random
	elif p2_bank < cost_of_living * p2_random:
		current_account = current_account - cost_of_living * p2_random

# player 1 production and earnings turn
	
	productivity_temp1 = (p1_productivity * p1_motivation) * p1_random
	p1_bank = productivity_temp1 + p1_bank

# player 2 production and earnings turn

	productivity_temp2 = (p2_productivity * p2_motivation) * p2_random
	p2_bank = productivity_temp2 + p2_bank

# deducting the turn cost for both players 

	p1_bank = p1_bank - (tax_rate * p1_random) * productivity_temp1
	p2_bank = p2_bank - (tax_rate * p2_random) * productivity_temp2

# the money goes to the bank (current_account)

	current_account = current_account + (tax_rate * productivity_temp1)
	current_account = current_account + (tax_rate * productivity_temp2)

# player 1 contribution to the current_account

	bank_temp1 = p1_bank * p1_give
	p1_bank = p1_bank - bank_temp1
	current_account = current_account + bank_temp1

# player 2 contribution to the current_account

	bank_temp2 = p2_bank * p2_give
	p2_bank = p2_bank - bank_temp2
	current_account = current_account + bank_temp2

# player 1 motivation adjustment (neg)

    	if bank_temp2 <= bank_temp1:
    		p1_motivation = p1_motivation - (p1_motivation * motivation_adjustment * p1_random)
    	else:
    		p1_motivation = p1_motivation + (p1_bank / p2_bank) * (p1_give / p2_give) * demand * p1_random
    	
# player 2 motivation adjustment (neg)

    	if bank_temp1 <= bank_temp2:
    		p2_motivation = p2_motivation + (p2_motivation * motivation_adjustment * p1_random)
    	else:
    		p2_motivation = p2_motivation + (p2_bank / p1_bank) * (p2_give / p1_give) * demand * p2_random

# admin fee is deducted from the current_account
	
	current_account = current_account - (productivity_temp1 + productivity_temp2) * service_cost * 0.1

# GDP adjustment

	gdplastround = gdp
	gdp = gdp + (productivity_temp1 + productivity_temp2)


# Demand adjustment for both players

	p1_lastround = p1_thisround
	p2_lastround = p2_thisround 

	p1_thisround = productivity_temp2 - (tax_rate * p1_random) * productivity_temp1
	p2_thisround = productivity_temp2 - (tax_rate * p2_random) * productivity_temp2

	if p1_lastround >= p1_thisround:
		demand = demand * 0.99 * p1_random
	elif p1_lastround <= p1_thisround:
		demand = demand * 1.01 * p1_random

	if p2_lastround >= p2_thisround:
		demand = demand * 0.99 * p2_random
	elif p1_lastround <= p1_thisround:
		demand = demand * 1.01 * p2_random

# creating the printed values 

	p1 = round(productivity_temp1, 2)
	p2 = round(productivity_temp2, 2)
	b1 = round(p1_bank, 2)
	b2 = round(p2_bank, 2)
	m1 = round(p1_motivation, 2)
	m2 = round(p2_motivation, 2)
	de = round(demand, 2)
	gd = round(gdp, 2)
	cu = round(current_account, 2)
	ex = round(gdp * service_cost)
	cl = round(cost_of_living, 2)

# results for the turn are printed on the screen

	print(turn," : ",p1,p2,b1,b2,m1,m2,de,gd,cu,ex,cl)

# the delay before next round is set

	time.sleep(sleeptime)	

print("GAME OVER")
