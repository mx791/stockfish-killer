import matplotlib.pyplot as plt
import chess.pgn
import numpy as np 
import chess

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


out_dir = "F:\\Dataset\\chess\\"

def load_n_game_from(pgn, n, name):
    count = 0

    X, Y = [], []
    Y_ = []

    for i in range(n):
        game = chess.pgn.read_game(pgn)
        if game.headers["Result"] == "1/2-1/2":
            continue
        winner = 0
        y_ = 0
        if game.headers["Result"] == "1-0":
            y_ = 1 
        if game.headers["Result"] == "0-1":
            y_ = 2

        vectY = np.zeros(3)
        vectY[y_] = 1
        board = game.board()

        for move in game.mainline_moves():
            board.push(move)
            count += 1
            if count % 7 == 0:
                vect = get_vect(board)
                X.append(vect)
                Y.append(y_)
                Y_.append(vectY)
        
        if i%1000 == 0:
            print(i, len(X))


    np.save(open(out_dir + "X_" + str(name), "wb"), np.array(X))
    np.save(open(out_dir + "Y_" + str(name), "wb"), np.array(Y_))


pgn = open("../../data/lichess_elite_2020-06.pgn")
load_n_game_from(pgn, 300000, 1)

pgn = open("../../data/lichess_elite_2020-08.pgn")
load_n_game_from(pgn, 300000, 2)

pgn = open("../../data/lichess_elite_2020-12.pgn")
load_n_game_from(pgn, 300000, 3)

pgn = open("../../data/lichess_elite_2021-06.pgn")
load_n_game_from(pgn, 300000, 4)