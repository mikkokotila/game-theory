#!/usr/bin/python
import time

# starting turn and per turn cost for players

turn = 0
turn_cost = 0.2
players = 2
cost = 0.012
minimum = 1

# productivity and resource settings

productivity = 1
total_resources = 100
motivation_adjustment = 0.01

# player one starting settings

p1_productivity = 1
p1_bank = 0
p1_motivation = 1
p1_contribution = 0.5

# player two starting settings

p2_productivity = 1
p2_bank = 0
p2_motivation = 1
p2_contribution = 0.49

# extra configuration values

total_last_resources = 99

# game starts 

while (total_resources - total_last_resources) > 0.01 or total_resources > minimum:
	turn = turn + 1

# player 1 production turn
	
	productivity_temp1 = p1_productivity * p1_motivation
	p1_bank = productivity_temp1 + p1_bank

# player 2 production turn

	productivity_temp2 = p2_productivity * p2_motivation
	p2_bank = productivity_temp2 + p2_bank

# turn cost for both players 

	p1_bank = p1_bank - (turn_cost * productivity_temp1)
	p2_bank = p2_bank - (turn_cost * productivity_temp2)

# the money goes to the bank (total_resources)

	total_resources = total_resources + (turn_cost * productivity_temp1)
	total_resources = total_resources + (turn_cost * productivity_temp2)

# player 1 contribution to the total_resources

	bank_temp1 = p1_bank * p1_contribution
	p1_bank = p1_bank - bank_temp1
	total_resources = total_resources + bank_temp1

# player 2 contribution to the total_resources

	bank_temp2 = p2_bank * p2_contribution
	p2_bank = p2_bank - bank_temp2
	total_resources = total_resources + bank_temp2

# player 1 motivation adjustment 

    	if bank_temp2 <= bank_temp1:
    		p1_motivation = p1_motivation - (p1_motivation * motivation_adjustment)
    	
# player 2 motivation adjustment 

    	if bank_temp1 <= bank_temp2:
    		p2_motivation = p2_motivation - (p2_motivation * motivation_adjustment)

# admin fee is deducted from the total_resources
	
	last_total_resources = total_resources
	total_resources = total_resources - (total_resources * cost)

# results for the turn are printed on the screen

	print("--",turn,"--")
	print("prod:",productivity_temp1 - productivity_temp2)
	print("bank:",p1_bank - p2_bank)
	print("motivation:",p1_motivation - p2_motivation)
	print("total resource:",total_resources,total_resources * cost)
	print("---------------")	

print("GAME OVER")
