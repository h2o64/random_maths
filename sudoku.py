# Convention numpy :
'''
[[1,2,3],[4,5,6],[7,8,9]]
           ===
    		| 1 2 3 |
    		| 4 5 6 |
    		| 7 8 9 |
'''

solution_ex = [
	[[1,8,9],[3,6,4],[7,5,2]],
	[[2,9,3],[5,4,6],[8,7,1]],
	[[6,2,5],[4,3,8],[9,1,7]],
	[[7,6,5],[1,8,2],[3,9,4]],
	[[5,1,7],[2,3,8],[9,4,6]],
	[[8,7,9],[6,2,1],[4,5,3]],
	[[2,4,3],[7,9,5],[6,8,1]],
	[[4,6,8],[1,7,9],[5,3,2]],
	[[3,1,4],[9,5,7],[8,2,6]]
]

def duplicates(l):
	seen = []
	for i in l:
		if i in seen : return True
		else: seen.append(i)
	return False

def calc_det(mat):
	ret = 0
	ret += 1*mat[0][0]*(mat[1][1]*mat[2][2]-mat[1][2]*mat[2][1])
	ret += -1*mat[0][1]*(mat[0][1]*mat[2][2]-mat[0][2]*mat[2][1])
	ret += 1*mat[0][2]*(mat[0][1]*mat[1][2]-mat[0][2]*mat[1][1])
	return ret

def is_list_correct(liste):
	return (len(liste) == 9) and not duplicates(liste)

def print_sud(sud):
	sud_str = []
	tmp_str = ''
	for i in range(9):
		tmp = str(sud[i][0][0]) + " " + str(sud[i][0][1]) + " " + str(sud[i][0][2]) + " \n"
		tmp += str(sud[i][1][0]) + " " + str(sud[i][1][1]) + " " + str(sud[i][1][2]) + " \n"
		tmp += str(sud[i][2][0]) + " " + str(sud[i][2][1]) + " " + str(sud[i][2][2]) + " \n"
		sud_str.append(tmp)
	for j in range(3):
		print sud_str[j+0]
	for j in range(3):
		print sud_str[j+3]
	for j in range(3):
		print sud_str[j+6]


'''
def is_sud_correct(sud):
	liste1 = [sud[0][0][0],sud[0][1][0],sud[0][2][0],sud[1][0][0]

	for i in range(9)
		for j in range(3)
'''
