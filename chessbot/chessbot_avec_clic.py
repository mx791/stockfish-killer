
import chess
import chess.pgn
import random as rd
import numpy as np
import time 
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

#Initialiser un plateau
chessboard_ = chess.Board()

#Détecter les promotions depuis les cases de la 7ème rangée
promotion_squares = [chess.A7, chess.B7,chess.C7,chess.D7,chess.E7,chess.F7,chess.G7,chess.H7]

# liste qui garde en mémoire les clicks de l'utilisateur
click_list = []

# Transformer les coordonnées d'un clic en une case du plateau
colonnes = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h']
lignes = np.arange(1,9)


squares = []
for colonne in colonnes :
    for ligne in lignes :
        squares.append(f'{colonne}{ligne}')


def pos_to_square(pos) :
    # print(pos)
    # print((pos[0] - 225)//69)
    pos[0] = colonnes[(pos[0] - 225)//69]
    pos[1] = 9 - ((pos[1] - 225)//69 + 1)
    return(f'{pos[0]}{pos[1]}')


# Fonction d'évaluation : valeur totale des pièces, +inf si mat

def count_value_(board, color):
    if board.is_checkmate():
        val = np.inf
        return val
    val = 0
    val += len(board.pieces(color=color, piece_type=chess.PAWN))
    val += len(board.pieces(color=color, piece_type=chess.KNIGHT))*3
    val += len(board.pieces(color=color, piece_type=chess.BISHOP))*3
    val += len(board.pieces(color=color, piece_type=chess.ROOK))*5
    val += len(board.pieces(color=color, piece_type=chess.QUEEN))*9
    
    return val + (rd.random() - 0.5)

def material_difference(board):
    return count_value_(board, chess.BLACK) - count_value_(board, chess.WHITE)

# Algo de recherche minimax avec élagage alpha-beta


def minimax(chessboard, depth, player, alpha, beta):
    best_list = []
    if player == 1 :
        best = [None, -np.inf]
    else :
        best = [None, np.inf]
    if depth == 0 :
        score = material_difference(chessboard)
        return([None,score])
    
    legal_moves = [str(x) for x in list(chessboard.legal_moves)]
    
    
        #print(move)
    for move in legal_moves :
        
        chessboard.push(chess.Move.from_uci(move))
        #print(f'depth : {depth}, move : {move} , evaluation : {material_difference(chessboard)}')
        move_ = ''.join((list(move).copy()))
        [move, score] = minimax(chessboard, depth-1, -player, alpha, beta)
        
        #print(move)
        chessboard.pop()

        if player == 1 :
            # if score == best[1] :
            #     best_list.append([move_, score])
            if score > best[1] :
                # best_list = []
                # best_list.append([move_, score])
                best = [move_, score]
                alpha = max(alpha, score)
                if beta <= alpha :
                    break
                #print(f'best : {best}')
        else :
            # if score == best[1] :
            #     best_list.append([move_, score])
            if score < best[1] :
                # best_list = []
                # best_list.append([move_, score])
                best = [move, score]
                beta = min(beta, score)
                if beta <= alpha :
                    break
    # if depth == 1 :
    #    return rd.choice(best_list)
    # else :
    #    return best
    return best


# ================Interface graphique===================    

class MainWindow(QWidget):
    # global turn
    # turn = 0
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChessBot")
        self.setGeometry(100, 100, 1100, 1100)

        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(200, 200, 600, 600)

        # self.chessboard = chess.Board()
        self.chessboard = chessboard_
        

        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)
        

    # def game_ending(self):

    #     if chessboard_.is_checkmate() :
    #         self.close()
    #         print('Checkmate')
    #     if chessboard_.is_stalemate() :
    #         self.close()
    #         print('Stalemate')

        
    def play_strategy(self): # Ici, stratégie minimax, depth = profondeur de la recherche des coups
        
        move = minimax(self.chessboard, depth= 1, player=1, alpha= -np.inf, beta = np.inf)
        move = move[0]
        print(move)
        self.chessboard.push(chess.Move.from_uci(move)) # push le nouveau move
        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8") # crée l'image du plateau
                    
        self.widgetSvg.load(self.chessboardSvg) #afficher le plateau mis à jour
        #self.game_ending(self)


    def mousePressEvent(self, event): # fonction appelée lorsqu'il y a un clic sur la fenêtre
        
        global click_list
        if event.pos().x() < 775 and event.pos().x() > 225 and event.pos().y() < 775 and event.pos().y() > 225 : # le clic doit être sur le plateau
            click_list.append(pos_to_square([event.pos().x(), event.pos().y()]))
            
            if len(click_list) == 2 : # au bout de 2 clics, on a la case de départ et d'arrivée. Si le coup est légal, il est joué et la liste des clics en mémoire est effacée
                print(click_list)
                move = f'{click_list[0]}{click_list[1]}'
                self.legal_moves = [str(x) for x in list(chessboard_.legal_moves)]
                
                if move in self.legal_moves :
                    self.chessboard.push(chess.Move.from_uci(move))
                    self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
                    
                    self.widgetSvg.load(self.chessboardSvg) 
                    #self.game_ending()

                    self.play_strategy() # l'ordi joue
                elif click_list[0][1] == '7' :
                    if self.chessboard.piece_at(promotion_squares[int(click_list[0][1])]).piece_type == 1 : # gros bordel pour les pions qui arrivent à la promotion
                        if (move + 'q') in self.legal_moves :
                            self.chessboard.push(chess.Move.from_uci(move + 'q'))
                            self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
                            
                            self.widgetSvg.load(self.chessboardSvg)


                click_list = [] # effacement des clics en mémoire

    

# ============= Exécution du programme ==================

app = QApplication([])
window = MainWindow()
window.show()
app.exec()