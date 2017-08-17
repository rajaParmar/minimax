def make_grid(grid,next_move_cord,turn):
	if(turn=="max"):
		character='X'
	else:character='O'

	grid[next_move_cord[0]][next_move_cord[1]]=character

	return




def all_moves(grid):
	moves=[]

	for i in range(0,3):
		for j in range(0,3):
			if(grid=='')
				moves.append([i,j])
	return moves



def print_grid(grid):
	for i in range(0,3):
		for j in range(0,3):
			print(grid[i][j]," ",end='')
		print()





def is_leaf(grid,score):
	x='X'
	o='O'

	for i in range(0,3):#rows
		if(grid[i][0]==x==grid[i][1]==x==grid[i][2]==x):
			score=10
			return True
		if(grid[i][0]==o==grid[i][1]==o==grid[i][2]==o):
			score=-10
			return True

	for i in range(0,3):#cols
		if(grid[0][i]==x==grid[1][i]==x==grid[2][i]==x):
			score=10
			return True
		if(grid[0][i]==o==grid[1][i]==o==grid[2][i]==o):
			score= -10
			return True

	if(grid[0][0]==x==grid[1][1]==x==grid[2][2]==x):
			score= 10
			return True
	if(grid[0][0]==o==grid[1][1]==o==grid[2][2]==o):
			score= -10
			return True

	if(grid[0][2]==x==grid[1][1]==x==grid[2][0]==x):
			score= 10
			return True
	if(grid[0][2]==o==grid[1][1]==o==grid[2][0]==o):
			score= -10
			return True

	if(len(all_moves(grid))==0 or len(all_moves(grid))>=8):
		score= 0
		return True


def index_of(list,ele):
	for i in range(len(list)):
		if(list[i]==ele):
			return i

def minimax(grid,turn,move):
	score=0
	if(is_leaf(grid,score)):
		return score

	moves=all_moves(grid)
	if(turn=="max"):
		move_list=[]
		score_list=[]
		for i in moves:
			move_list.append(i)
			temp_grid=grid.copy()
			make_grid(temp_grid,i,"max")
			score_list.append(minimax(temp_grid,"min",[]))
				
	else:
		move_list=[]
		score_list=[]
		for i in moves:
			move_list.append(i)
			temp_grid=grid.copy()
			make_grid(temp_grid,i,"min")
			score_list.append(minimax(temp_grid,"max",[]))

	move=index_of(max(score_list))




grid=[['','',''],['','',''],['','','']]