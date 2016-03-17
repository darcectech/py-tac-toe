import random
import time
import pygame
import math
import sys
import os
import __main__
main = __main__

taskList = []
memory = [["reference","reference2"],
		  ["value","value2"]]
hasMatch = False

def remember(ref, val):
	global memory
	memory[0].append(ref)
	memory[1].append(val)
	print("Remembered that "+memory[0][-1] +" is "+memory[1][-1])

def forget(ref):
	global memory
	index_ref = memory[0].index(ref)
	memory[0].remove(index_ref)
	memory[1].remove(index_ref)

def recallx(ref):
	global memory
	return memory[1][memory[0].index(ref)]

def can_remember(ref):
	if ref in memory[0]:
		return True
	else:
		return False

def play():
	print("Playing main")
	tGrid = main.get_grid()
	if (play_offensive(tGrid) == False):
		print("No winning moves available. Playing defensively. . . ")
		if (play_defensive(tGrid) == False):
			print("No need to defend. Playing with calculations. . . ")
			play_rnd()
	check_if_won(2)

def play_rnd():
	gridCopy = main.possible_wins
	random.shuffle(gridCopy)
	print(gridCopy)
	for matchAtI in range(0,len(main.possible_wins)):
		if check_pattern_match(main.possible_wins[matchAtI], main.get_grid()) == True:
			print("PLACED ##################################")
			break
		else:
			print("RETRYING...................................")

def check_if_won(player_id):
	found_winner = False
	match_count = 0
	player1_grid = main.get_grid(player_id)
	for pattern in main.possible_wins:
		print(pattern + " > " + player1_grid)
		for i in range(0,9):
			if pattern[i] == "1" and player1_grid[i]=="1":
				match_count+=1
			if match_count >=3:
				main.winnings = 'HUMAN' if player_id == 1 else 'COMPUTER'
				found_winner = True
				print("Player "+ str(player_id) + " has WON!!!!!!!!!!!!!!!!!!")
		if found_winner == False:
			match_count = 0

def check_pattern_match(pattern,currentGrid):
	returnVal = False
	pattern = pattern[::-1]
	for e in range(1,10):
		print(str(main.possible_wins.index(pattern)) + " is pattern " + pattern + " at grid of "+ main.get_grid())
		if can_remember(pattern) == True:
			print("not in this pattern")
		elif pattern[e-1]=="1" and get_grid_item_at_loc(e) == "0":
			print("pattern no "+ str(main.possible_wins.index(pattern)) + " at character " + str(e) + " has value "+ pattern[e-1] + ", where grid has value " +  get_grid_item_at_loc(e) + " [moving at " + get_pos_string(e-1) + "] *")
			bar = main.set_pawn(2,get_pos_string(e-1))
			if bar == False:
				print("failed to place")
			else:
				returnVal = True
				break
		elif pattern[e-1]=="0":
			print("pattern no "+ str(main.possible_wins.index(pattern)) + " at character " + str(e) + " has value "+ pattern[e-1] + ", where grid has value " +  get_grid_item_at_loc(e) + " [not moving TO " + get_pos_string(e-1) + "]")
		elif pattern[e-1]=="1" and get_grid_item_at_loc(e) == "2":
			print("Already placed here at " + pattern + " with loc "+ main.get_grid())
		elif pattern[e-1]=="1" and get_grid_item_at_loc(e) == "1":
			print("pattern no "+ str(main.possible_wins.index(pattern)) + " at character " + str(e) + " has value "+ pattern[e-1] + ", where grid has value " +  get_grid_item_at_loc(e) + " [not moving at " + get_pos_string(e-1) + "]")
			remember(pattern,"do not place")
	return returnVal

def get_pos_string(ind):
	switcher = {
		0: "Top left",
		3: "Middle left",
		6: "Bottom left",
		1: "Middle top",
		4: "Middle middle",
		7: "Middle bottom",
		2: "Top right",
		5: "Middle right",
		8: "Bottom right"
	}
	return switcher.get(ind,"nothingz + " + str(ind))

def get_grid_item_at_loc(ind):
	if ind <= 3:
		return see_grid()[ind-1]
	elif ind <= 6 and ind >= 4:
		return see_grid()[ind-1]
	elif ind <= 9 and ind >= 6:
		return see_grid()[ind-1]

def see_grid(playerID = 0):
	return main.get_grid(playerID)

def stop_playing():
	time.sleep(2)
	sys.exit(0)

def play_defensive(tGrid):
	turnPlayed = False
	# check if user is winning and stop them if they are
	if (tGrid[0] == "1") and (tGrid[1] == "1") and (tGrid[2] == "0"):
		main.set_pawn(2,get_pos_string(2))
		turnPlayed = True
	elif (tGrid[0] == "1") and (tGrid[1] == "0") and (tGrid[2] == "1"):
		main.set_pawn(2,get_pos_string(1))
		turnPlayed = True
	elif (tGrid[0] == "0") and (tGrid[1] == "1") and (tGrid[2] == "1"):
		main.set_pawn(2,get_pos_string(0))
		turnPlayed = True
		#end of mode1
	elif (tGrid[0] == "1") and (tGrid[4] == "1") and (tGrid[8] == "0"):
		main.set_pawn(2,get_pos_string(8))
		turnPlayed = True
	elif (tGrid[0] == "1") and (tGrid[4] == "0") and (tGrid[8] == "1"):
		main.set_pawn(2,get_pos_string(4))
		turnPlayed = True
	elif (tGrid[0] == "0") and (tGrid[4] == "1") and (tGrid[8] == "1"):
		main.set_pawn(2,get_pos_string(0))
		turnPlayed = True
		#end of mode2
	elif (tGrid[0] == "1") and (tGrid[3] == "1") and (tGrid[6] == "0"):
		main.set_pawn(2,get_pos_string(6))
		turnPlayed = True
	elif (tGrid[0] == "1") and (tGrid[3] == "0") and (tGrid[6] == "1"):
		main.set_pawn(2,get_pos_string(3))
		turnPlayed = True
	elif (tGrid[0] == "0") and (tGrid[3] == "1") and (tGrid[6] == "1"):
		main.set_pawn(2,get_pos_string(0))
		turnPlayed = True
		#end of mode3
	elif (tGrid[3] == "1") and (tGrid[4] == "1") and (tGrid[5] == "0"):
		main.set_pawn(2,get_pos_string(5))
		turnPlayed = True
	elif (tGrid[3] == "1") and (tGrid[4] == "0") and (tGrid[5] == "1"):
		main.set_pawn(2,get_pos_string(4))
		turnPlayed = True
	elif (tGrid[3] == "0") and (tGrid[4] == "1") and (tGrid[5] == "1"):
		main.set_pawn(2,get_pos_string(3))
		turnPlayed = True
		#end of mode4
	elif (tGrid[1] == "1") and (tGrid[4] == "1") and (tGrid[7] == "0"):
		main.set_pawn(2,get_pos_string(7))
		turnPlayed = True
	elif (tGrid[1] == "1") and (tGrid[4] == "0") and (tGrid[7] == "1"):
		main.set_pawn(2,get_pos_string(4))
		turnPlayed = True
	elif (tGrid[1] == "0") and (tGrid[4] == "1") and (tGrid[7] == "1"):
		main.set_pawn(2,get_pos_string(1))
		turnPlayed = True
		#end of mode5
	elif (tGrid[2] == "1") and (tGrid[4] == "1") and (tGrid[6] == "0"):
		main.set_pawn(2,get_pos_string(6))
		turnPlayed = True
	elif (tGrid[2] == "1") and (tGrid[4] == "0") and (tGrid[6] == "1"):
		main.set_pawn(2,get_pos_string(4))
		turnPlayed = True
	elif (tGrid[2] == "0") and (tGrid[4] == "1") and (tGrid[6] == "1"):
		main.set_pawn(2,get_pos_string(2))
		turnPlayed = True
		#end of mode6
	elif (tGrid[6] == "1") and (tGrid[7] == "1") and (tGrid[8] == "0"):
		main.set_pawn(2,get_pos_string(8))
		turnPlayed = True
	elif (tGrid[6] == "1") and (tGrid[7] == "0") and (tGrid[8] == "1"):
		main.set_pawn(2,get_pos_string(7))
		turnPlayed = True
	elif (tGrid[6] == "0") and (tGrid[7] == "1") and (tGrid[8] == "1"):
		main.set_pawn(2,get_pos_string(6))
		turnPlayed = True
		#end of mode7
	elif (tGrid[2] == "1") and (tGrid[5] == "1") and (tGrid[8] == "0"):
		main.set_pawn(2,get_pos_string(8))
		turnPlayed = True
	elif (tGrid[2] == "1") and (tGrid[5] == "0") and (tGrid[8] == "1"):
		main.set_pawn(2,get_pos_string(5))
		turnPlayed = True
	elif (tGrid[2] == "0") and (tGrid[5] == "1") and (tGrid[8] == "1"):
		main.set_pawn(2,get_pos_string(2))
		turnPlayed = True
		#end of mode8
	else:
		turnPlayed = False
	return turnPlayed

def play_offensive(tGrid):
	turnPlayed = False
	# check if user is winning and stop them if they are
	if (tGrid[0] == "2") and (tGrid[1] == "2") and (tGrid[2] == "0"):
		main.set_pawn(2,get_pos_string(2))
		turnPlayed = True
	elif (tGrid[0] == "2") and (tGrid[1] == "0") and (tGrid[2] == "2"):
		main.set_pawn(2,get_pos_string(1))
		turnPlayed = True
	elif (tGrid[0] == "0") and (tGrid[1] == "2") and (tGrid[2] == "2"):
		main.set_pawn(2,get_pos_string(0))
		turnPlayed = True
		#end of mode1
	elif (tGrid[0] == "2") and (tGrid[4] == "2") and (tGrid[8] == "0"):
		main.set_pawn(2,get_pos_string(8))
		turnPlayed = True
	elif (tGrid[0] == "2") and (tGrid[4] == "0") and (tGrid[8] == "2"):
		main.set_pawn(2,get_pos_string(4))
		turnPlayed = True
	elif (tGrid[0] == "0") and (tGrid[4] == "2") and (tGrid[8] == "2"):
		main.set_pawn(2,get_pos_string(0))
		turnPlayed = True
		#end of mode2
	elif (tGrid[0] == "2") and (tGrid[3] == "2") and (tGrid[6] == "0"):
		main.set_pawn(2,get_pos_string(6))
		turnPlayed = True
	elif (tGrid[0] == "2") and (tGrid[3] == "0") and (tGrid[6] == "2"):
		main.set_pawn(2,get_pos_string(3))
		turnPlayed = True
	elif (tGrid[0] == "0") and (tGrid[3] == "2") and (tGrid[6] == "2"):
		main.set_pawn(2,get_pos_string(0))
		turnPlayed = True
		#end of mode3
	elif (tGrid[3] == "2") and (tGrid[4] == "2") and (tGrid[5] == "0"):
		main.set_pawn(2,get_pos_string(5))
		turnPlayed = True
	elif (tGrid[3] == "2") and (tGrid[4] == "0") and (tGrid[5] == "2"):
		main.set_pawn(2,get_pos_string(4))
		turnPlayed = True
	elif (tGrid[3] == "0") and (tGrid[4] == "2") and (tGrid[5] == "2"):
		main.set_pawn(2,get_pos_string(3))
		turnPlayed = True
		#end of mode4
	elif (tGrid[1] == "2") and (tGrid[4] == "2") and (tGrid[7] == "0"):
		main.set_pawn(2,get_pos_string(7))
		turnPlayed = True
	elif (tGrid[1] == "2") and (tGrid[4] == "0") and (tGrid[7] == "2"):
		main.set_pawn(2,get_pos_string(4))
		turnPlayed = True
	elif (tGrid[1] == "0") and (tGrid[4] == "2") and (tGrid[7] == "2"):
		main.set_pawn(2,get_pos_string(1))
		turnPlayed = True
		#end of mode5
	elif (tGrid[2] == "2") and (tGrid[4] == "2") and (tGrid[6] == "0"):
		main.set_pawn(2,get_pos_string(6))
		turnPlayed = True
	elif (tGrid[2] == "2") and (tGrid[4] == "0") and (tGrid[6] == "2"):
		main.set_pawn(2,get_pos_string(4))
		turnPlayed = True
	elif (tGrid[2] == "0") and (tGrid[4] == "2") and (tGrid[6] == "2"):
		main.set_pawn(2,get_pos_string(2))
		turnPlayed = True
		#end of mode6
	elif (tGrid[6] == "2") and (tGrid[7] == "2") and (tGrid[8] == "0"):
		main.set_pawn(2,get_pos_string(8))
		turnPlayed = True
	elif (tGrid[6] == "2") and (tGrid[7] == "0") and (tGrid[8] == "2"):
		main.set_pawn(2,get_pos_string(7))
		turnPlayed = True
	elif (tGrid[6] == "0") and (tGrid[7] == "2") and (tGrid[8] == "2"):
		main.set_pawn(2,get_pos_string(6))
		turnPlayed = True
		#end of mode7
	elif (tGrid[2] == "2") and (tGrid[5] == "2") and (tGrid[8] == "0"):
		main.set_pawn(2,get_pos_string(8))
		turnPlayed = True
	elif (tGrid[2] == "2") and (tGrid[5] == "0") and (tGrid[8] == "2"):
		main.set_pawn(2,get_pos_string(5))
		turnPlayed = True
	elif (tGrid[2] == "0") and (tGrid[5] == "2") and (tGrid[8] == "2"):
		main.set_pawn(2,get_pos_string(2))
		turnPlayed = True
		#end of mode8
	else:
		turnPlayed = False
	return turnPlayed