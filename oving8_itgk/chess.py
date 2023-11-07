from enum import Enum

class White(Enum):
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6

class Black(Enum):
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6

def make_board() -> list:
    board = []
    row = [Black.ROOK, Black.KNIGHT, Black.BISHOP, Black.QUEEN, Black.KING, Black.BISHOP, Black.KNIGHT, Black.ROOK]
    board.append(row)
    
    row = []
    for _ in range(8):
        row.append(Black.PAWN)
    board.append(row)
    
    row = []
    for _ in range(8*4):
        row.append(None)
        if len(row) == 8:
            board.append(row)
            row = []
    
    row = []
    for _ in range(8):
        row.append(White.PAWN)
    board.append(row)
    row = [White.ROOK, White.KNIGHT, White.BISHOP, White.QUEEN, White.KING, White.BISHOP, White.KNIGHT, White.ROOK]
    board.append(row)
    
    return board

def print_board(board : list):
    d = {
        Black.PAWN : "♙",
        Black.ROOK : "♖", 
        Black.KNIGHT : "♘",
        Black.BISHOP : "♗",
        Black.QUEEN : "♕",
        Black.KING : "♔",
        
        White.PAWN : "♟",
        White.ROOK : "♜", 
        White.KNIGHT : "♞",
        White.BISHOP : "♝",
        White.QUEEN : "♛",
        White.KING : "♚",
        
        None : " "
    }
    print("    a   b   c   d   e   f   g   h")
    for i in range(8, 0, -1):
        print("  ---------------------------------")
        print(f"{i} ", end="") 
        for num in board[(8-i)]:
            print(("|"+ f" {d[num]} " + ""), end="")
        print("|" + f" {i}")
    print("  ---------------------------------")
    print("    a   b   c   d   e   f   g   h")
    
    return

def translate(s : str) -> (int, int):
    d = {
        "a" : 0, "b" : 1, "c" : 2, "d" : 3,
        "e" : 4, "f" : 5, "g" : 6, "h": 7
    }
    if len(s) != 2 or int(s[1]) > 8 or int(s[1]) < 1 or s[0] not in d:
        raise ValueError("Invalid coordinates")
    x = 8 - int(s[1])
    y = d[s[0]]
    return x, y

    
def get_piece(board : list, s : str):
    x, y = translate(s)
    return board[x][y]

def move_piece(board : list, from_s : str, to_s : str):
    from_x, from_y = translate(from_s)
    to_x, to_y = translate(to_s)
    board[to_x][to_y] = board[from_x][from_y]
    board[from_x][from_y] = None

    return 

b = make_board()
print_board(b)
move_piece(b, "a1", "a3")
print_board(b)

# print(get_piece(b, "c4"))

#TODO: Lage Chess-klasse?
