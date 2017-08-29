''' 2048 game in python '''

import random

main_grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
game_over = False

# Input API #
# FROM https://stackoverflow.com/questions/22397289/finding-the-values-of-the-arrow-keys-in-python-why-are-they-triples
import sys,tty,termios
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                return "up"
        elif k=='\x1b[B':
                return "down"
        elif k=='\x1b[C':
                return "right"
        elif k=='\x1b[D':
                return "left"
        else:
                return "none"

def generate_random_case():
	tmp = random.randint(1,2)
	if tmp == 1 : return 2
	else : return 4

def potential_cases(grid):
	ret = []
	for i in range(0,4):
		for j in range(0,4):
			if grid[i][j] == 0: ret.append((i,j))
	return ret

def pop_case(grid):
	pos = potential_cases(grid)
	n = len(pos)
	if n == 0 :
		game_over = True
	else:
		x,y = pos[random.randint(0,n-1)]
		grid[x][y] = generate_random_case()
	return grid

def pop_case_init(grid):
	x = random.randint(0,3)
	y = random.randint(0,2)
	print "x = " + str(x)
	print "y = " + str(y)
	grid[x][y] = 2
	grid[x][y+1] = 2
	return grid

def print_grid(grid):
	print "-----------------"
	print "| " + str(grid[0][0]) + " | " + str(grid[1][0]) + " | " + str(grid[2][0]) + " | " + str(grid[3][0]) + " |"
	print "-----------------"
	print "| " + str(grid[0][1]) + " | " + str(grid[1][1]) + " | " + str(grid[2][1]) + " | " + str(grid[3][1]) + " |"
	print "-----------------"
	print "| " + str(grid[0][2]) + " | " + str(grid[1][2]) + " | " + str(grid[2][2]) + " | " + str(grid[3][2]) + " |"
	print "-----------------"
	print "| " + str(grid[0][3]) + " | " + str(grid[1][3]) + " | " + str(grid[2][3]) + " | " + str(grid[3][3]) + " |"
	print "-----------------"


def reset_grid(grid):
	grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def find_targets(liste):
	values = list(set(liste))
	occur = [0]*(max(values)+1)
	for i in liste: occur[i] += 1
	return [(k,occur[k]) for k in range(len(occur)) if occur[k] != 1]

def duplicates(l):
	seen = []
	for i in l:
		if i in seen : return True
		else: seen.append(i)
	return False

def play_direct(liste):
	nul = []
	non_nul = []
	non_touche = []
	j = 0
	count = 0
	for i in liste:
		if i == 0 : nul.append(i)
		else:
			non_nul.append(i)
			non_touche.append(True)
	while duplicates(non_nul) and j < len(non_nul)-1:
		print str(non_touche)
		print str(non_nul)
		print str(nul)
		if (non_nul[j] == non_nul[j+1]) and (non_touche[j] and non_touche[j + 1]):
			if not count >= 4:
				non_nul[j] *= 2
				non_touche[j] = False
				non_nul.pop(j + 1)
				non_touche.pop(j + 1)
				nul.append(0)
				j = 0
				count += 1
		j += 1
	return non_nul + nul

def play(grid):
	pop_case_init(grid)
	while game_over != True:
		print str(grid)
		print_grid(grid)
		quit = raw_input("Wanna quit ?")
		if quit == 'y': break
		if True:
			print "Choose a direction"
			user_input = get()
			if user_input == "none": continue
			elif user_input == "down":
				for i in range(0,4):
					grid[i] = list(play_direct(grid[i]))
			elif user_input == "up":
				for i in range(0,4):
					grid[i] = list(play_direct(list(reversed(grid[i]))))
			elif user_input == "right":
				for i in range(0,4):
					grid[0][i],grid[1][i],grid[2][i],grid[3][i] = play_direct([grid[0][i],grid[1][i],grid[2][i],grid[3][i]])
			elif user_input == "left":
				for i in range(0,4):
					grid[0][i],grid[1][i],grid[2][i],grid[3][i] = play_direct(list(reversed([grid[0][i],grid[1][i],grid[2][i],grid[3][i]])))
			pop_case(grid)
	return "Game over"

