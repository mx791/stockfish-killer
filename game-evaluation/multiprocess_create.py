import matplotlib.pyplot as plt
import chess.pgn
import numpy as np 
import chess
from multiprocessing import Process


def get_base_vect(size):
    arr = [0 for i in range(size)]
    return np.array(arr)

def get_vect(board):
    pieces = [chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN, chess.KING]
    colors = [chess.WHITE, chess.BLACK]
    vect = get_base_vect(len(pieces)*2*64)
    for i in range(len(colors)):
        for e in range(len(pieces)):
            lst = board.pieces(color=colors[i], piece_type=pieces[e])
            for position in lst:
                vect[position*len(pieces)*2 + i*len(pieces) + e] = 1
    return vect


X, Y = [], []
Y_ = []

count = 0

def process(game):
    if game.headers["Result"] == "1/2-1/2":
        return

    y = np.zeros((1))
    if game.headers["Result"] == "1-0":
        y[0] = 1.0

    board = game.board()

    for move in game.mainline_moves():
        board.push(move)
        count += 1
        if count%4 == 0:
            vect = get_vect(board)
            X.append(vect)
            Y.append(y)

if __name__ == '__main__':
    pgn = open("../../data/lichess_elite_2020-06.pgn")

    for i in range(1):
        threads = []
        for e in range(2):
            game = chess.pgn.read_game(pgn)
            print(game)
            p = Process(target=process, args=(game))
            p.start()
            threads.append(p)
        
        for t in threads:
            t.join()
        
        if i%10 == 0:
            print(i, len(X))

    print(len(X))