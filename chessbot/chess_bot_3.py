
import chess
import chess.pgn
import random as rd
import numpy as np
import time 
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

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
    
    return val

def material_difference(board):
    return count_value_(board, chess.BLACK) - count_value_(board, chess.WHITE)



def minimax(chessboard, depth, player, alpha, beta):
    
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
            if score > best[1] :
                
                best = [move_, score]
                alpha = max(alpha, score)
                if beta <= alpha :
                    break
                #print(f'best : {best}')
        else :
            if score < best[1] :
                best = [move, score]
                beta = min(beta, score)
                if beta <= alpha :
                    break
    return best


chessboard_ = chess.Board()
#x = input('move2')

class MainWindow(QWidget):
    global turn
    turn = 0
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 1100, 1100)

        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(200, 200, 600, 600)

        # self.chessboard = chess.Board()
        self.chessboard = chessboard_
        

        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)

        legal_moves = [str(x) for x in list(chessboard_.legal_moves)]
        self.buttons = [QPushButton(str(move), self) for move in legal_moves]
        for i, button in enumerate(self.buttons) :
            button.move(50*(i%10),50 + (i//10)*50)
            
            button.clicked.connect(self.btnListener)
    
    def update(self,legal_moves) :
        
        for button in self.buttons :
            button.hide()
        # print(f' Black material : {count_value_(self.chessboard, color= chess.BLACK)}')
        # print(f' White material : {count_value_(self.chessboard, color= chess.WHITE)}')
        if self.chessboard.is_checkmate() :
            self.close()
            print('Checkmate')
        if self.chessboard.is_stalemate() :
            self.close()
            print('Stalemate')
            
        self.buttons = [QPushButton(str(move), self) for move in legal_moves]
        
        for i, button in enumerate(self.buttons) :
            button.move(50*(i%10),50 + (i//10)*30)
            
            button.show()
            
            button.clicked.connect(self.btnListener)

    


    def play_strategy(self):

        #random strategy
        # legal_moves = [str(x) for x in list(self.chessboard.legal_moves)] 
        # move = rd.choice(legal_moves)
        # self.chessboard.push(chess.Move.from_uci(move))

        #greedy strategy
        # legal_moves = [str(x) for x in list(self.chessboard.legal_moves)] 
        # try_board = self.chessboard.copy()
        # score_list = []
        # for k, move in enumerate(legal_moves) :
        #     try_board.push(chess.Move.from_uci(move))
        #     print(f' Black material : {count_value_(try_board, color= chess.BLACK)}')
        #     print(f' White material : {count_value_(try_board, color= chess.WHITE)}')
        #     score_list.append(material_difference(try_board))
        #     try_board.pop()
        # move = legal_moves[np.argmax(score_list)]
        # self.chessboard.push(chess.Move.from_uci(move))

        #minimax 

        move = minimax(self.chessboard, depth=5, player=1, alpha= -np.inf, beta = np.inf)
        move = move[0]
        self.chessboard.push(chess.Move.from_uci(move))


    #action method
    def btnListener(self):
        
        global turn
        rbt = self.sender()
        move = rbt.text()
        for button in self.buttons :
            button.deleteLater()
         
        
        if turn%2 == 0 :
            
            self.chessboard.push(chess.Move.from_uci(move))
            turn += 1
            self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
            
            self.widgetSvg.load(self.chessboardSvg) 
            legal_moves = [str(x) for x in list(self.chessboard.legal_moves)]
            self.update(legal_moves)
        
            # self.buttons = [QPushButton(str(move), self) for move in legal_moves]
            # print(self.buttons)
            # for i, button in enumerate(self.buttons) :
            #     button.move(50*(i%10),50 + (i//10)*50)
            #     button.show()
            #     print(button.text())
            #     button.clicked.connect(self.btnListener)

            
        if turn%2 == 1 :
            
            self.play_strategy()
            turn += 1


        # self.chessboard = chessboard_
            self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
            self.widgetSvg.load(self.chessboardSvg) 
            
            
            legal_moves = [str(x) for x in list(self.chessboard.legal_moves)]
            self.update(legal_moves)
            
            # self.buttons = [QPushButton(str(move), self) for move in legal_moves]
            # print(self.buttons)
            # for i, button in enumerate(self.buttons) :
            #     button.move(50*(i%10),50 + (i//10)*50)
            #     button.show()
            #     print(button.text())
            #     button.clicked.connect(self.btnListener)
        
        
        
    # def mousePressEvent(self, event):
    #     legal_moves = [str(x) for x in list(chessboard_.legal_moves)]
    #     buttons = [QPushButton(str(move), self) for move in legal_moves]
    #     for i, button in enumerate(buttons) :
    #         button.move(50*i,50)
    #         text = button.text()
    #         # move = button.clicked.connect(self.btnListener)
    #         # print(move)

        
    #     # legal_moves = [str(x) for x in list(chessboard_.legal_moves)]
    #     # print(legal_moves)
    #     moves = list(legal_moves)
    #     move = rd.choice(moves)
    #     chessboard_.push(chess.Move.from_uci(move))
    #     self.chessboard = chessboard_
    #     self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
    #     self.widgetSvg.load(self.chessboardSvg) 
        
         





    



# for k in range(2) :
    # legal_moves = [str(x) for x in list(chessboard_.legal_moves)]
    # print(legal_moves)
    # moves = list(legal_moves)
    # move = rd.choice(moves)
    # chessboard_.push(chess.Move.from_uci(move))
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
    


    
    # output = buttonbox('text', 'title', legal_moves_2, image= boardsvg)
    # chessboard.push(chess.Move.from_uci(output))

    # legal_moves = board.legal_moves
    # moves = list(legal_moves)
    # move = rd.choice(moves)
    # board.push(move)


