import numpy as np
from collections import Counter

right_rule =  [[5,2],[5,0],[7,1],[5,2],[3,2]]
bottom_rule = [[6,1],[7,1],[3,2],[6,1],[3,2]]
# board = np.array([[ -1, -1, -1, -1, -1],
#                   [ -1, -1, -1, -1, -1],
#                   [ -1, -1, -1, -1, -1],
#                   [ -1, -1, -1, -1, -1],
#                   [ -1, -1, -1, -1, -1]])
board = np.array([[  3,  1,  1, -1, -1],
                  [  1,  1,  1,  1,  1],
                  [ -1,  2, -1,  3, -1],
                  [ -1, -1, -1, -1, -1],
                  [ -1, -1, -1, -1, -1]])
mask = np.full((5, 5), -1)
correct_num = []
for i in range(5):
    correct_num.append(5 - np.sum(np.equal(board[i], mask[i])))

seq_list = [[],[],[],[],[]]

def dfs(seq, num):
    if len(seq) == 5:
        if sum(seq) == right_rule[num][0] and Counter(seq)[0] == right_rule[num][1]:
            seq_list[num].append(seq)
        return
    for i in range(4):
        tmp_seq = seq[:]
        tmp_seq.append(i)
        dfs(tmp_seq, num)
    return

for i in range(5):
    dfs([], i)


def check_valid(board):
    board = np.array(board)
    m, n = board.shape
    if m < 5:
        for i in range(5):
            if Counter(board[:,i])[0] > bottom_rule[i][1]:
                return False
    elif m == 5:
        for i in range(5):
            if np.sum(board[:,i]) != bottom_rule[i][0]:
                return False
            if Counter(board[:,i])[0] != bottom_rule[i][1]:
                return False
    return True


correct_board = []
def construct_board(seq):
    global correct_board, corr, board, correct_num
    depth = len(seq)
    if depth == 5:
        if check_valid(seq):
            correct_board.append(seq)
        return
    for i in range(len(seq_list[depth])):
        tmp_board = seq[:]
        tmp_board.append(seq_list[depth][i])
        if check_valid(tmp_board) and (np.sum(np.equal(board[depth], np.array(tmp_board[depth]))) == correct_num[depth]):
            construct_board(tmp_board)
    return

construct_board([])
correct_board = np.array(correct_board)
print(correct_board)
print("\n" + str(len(correct_board)) + " answers found")

one_mask = np.full((5,5), 1)
two_mask = np.full((5,5), 2)
three_mask = np.full((5,5), 3)
zero_mask = np.zeros((5,5))

answer = np.full((5,5), True)
bomb = np.full((5,5), True)
for i in range(len(correct_board)):
    cur = correct_board[i]
    tmp_equal = (one_mask==cur) + (two_mask==cur) + (three_mask==cur)
    tmp_bomb = zero_mask==cur
    answer = np.logical_and(tmp_equal, answer)
    bomb = np.logical_and(tmp_bomb, bomb)

print('======================================')

print('- 100 percent answer')
print(answer)
print('======================================')

print('- 100 percent bomb')
print(bomb)
print('======================================')