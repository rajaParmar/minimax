nxy={1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}

def find_max(values):
	max=-100
	for i in values:
		if(i>max):
			max=i
	return max

def find_min(values):
	min=100
	for i in values:
		if(i<min):
			min=i
	return min


def add_to_dict(values,score,coord):
	try:
		values[score].append(coord)
	except KeyError:
		values[score]=[coord]

def board_print(board):
	for i in board:
		for j in i:
			if(j==''):
				print('@','|',end='')
			else:
				print(j,'|',end='')
		print()



def win_or_draw_or_continue(board):
	win_coord=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
	empty=['','','']
	for i in win_coord:
		if((board[nxy[i[0]][0]][nxy[i[0]][1]]==board[nxy[i[1]][0]][nxy[i[1]][1]]==board[nxy[i[2]][0]][nxy[i[2]][1]]) and ([board[nxy[i[0]][0]][nxy[i[0]][1]],board[nxy[i[1]][0]][nxy[i[1]][1]],board[nxy[i[2]][0]][nxy[i[2]][1]]]!=empty)):
			return [1,board[nxy[i[0]][0]][nxy[i[0]][1]]]
	count=0
	for i in board:
		for j in i:
			if (j==''):
				count+=1
	if(count==0):
		return 0
	return '@'

def make_fake_board(board,temp_coord,option):
	fake_board=[['','',''],['','',''],['','','']]
	for i in nxy:
		fake_board[nxy[i][0]][nxy[i][1]]=board[nxy[i][0]][nxy[i][1]]
	fake_board[temp_coord[0]][temp_coord[1]]=option
	return fake_board

def find_all_empty_space(board):
	empty_spaces=[]
	for i in nxy:
		if(board[nxy[i][0]][nxy[i][1]]==''):
			empty_spaces.append(nxy[i])
	return empty_spaces

def minimax(board,is_max,depth):
	val=win_or_draw_or_continue(board)
	if(val==0):
		return 0
	if(val==[1,'X']):
		return 10
	if(val==[1,'O']):
		return -10

	if(is_max):
		values={}
		empty_spaces=find_all_empty_space(board)
		for i in empty_spaces:
			fake_board=make_fake_board(board,i,'X')
			value=minimax(fake_board,False,[depth[0],depth[1]+1])
			add_to_dict(values,value,i)
		max=find_max(values)
		if(depth[0]==depth[1]):
			return values[max]
		else: return max 
	else:
		values={}
		empty_spaces=find_all_empty_space(board)
		for i in empty_spaces:
			fake_board=make_fake_board(board,i,'O')
			value=minimax(fake_board,True,[depth[0],depth[1]+1])
			add_to_dict(values,value,i)
		min=find_min(values)
		if(depth[0]==depth[1]):
			return values[min]
		else: return min 

board=[['','',''],['','',''],['','','']]

def game(board):

	while(win_or_draw_or_continue(board) =='@'):
		board_print(board)
		print("Enter choice:")
		choice=(int)(input())
		u_x=nxy[choice][0]
		u_y=nxy[choice][1]
		board[u_x][u_y]='O'
		options=minimax(board,True,[1,1])
		if(len(options)==0):
			print("Match Drawn!")
			break
		c_opt_x=options[0][0]
		c_opt_y=options[0][1]
		board[c_opt_x][c_opt_y]='X'
game(board)