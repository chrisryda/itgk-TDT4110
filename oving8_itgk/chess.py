from enum import Enum

class White(Enum):
    def __str__(self) -> str:
        return "White " + self.name
    
    WHITE = 0
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6

class Black(Enum):
    def __str__(self) -> str:
        return self.name
    
    BLACK = 0
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6

print_dict = {
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

translation_dict = {
    "a" : 0, "b" : 1, "c" : 2, "d" : 3,
    "e" : 4, "f" : 5, "g" : 6, "h": 7
}

def make_board() -> list:
    board = []
    board.append([Black.ROOK, Black.KNIGHT, Black.BISHOP, Black.QUEEN, Black.KING, Black.BISHOP, Black.KNIGHT, Black.ROOK])
    board.append([Black.PAWN, Black.PAWN, Black.PAWN, Black.PAWN, Black.PAWN, Black.PAWN, Black.PAWN, Black.PAWN])
    row = []
    for _ in range(8*4):
        row.append(None)
        if len(row) == 8:
            board.append(row)
            row = []
    board.append([White.PAWN, White.PAWN, White.PAWN, White.PAWN, White.PAWN, White.PAWN, White.PAWN, White.PAWN])
    board.append([White.ROOK, White.KNIGHT, White.BISHOP, White.QUEEN, White.KING, White.BISHOP, White.KNIGHT, White.ROOK])
    
    return board

def print_board(board : list):
    print("    a   b   c   d   e   f   g   h")
    for i in range(8, 0, -1):
        print("  ---------------------------------")
        print(f"{i} ", end="") 
        for p in board[(8-i)]:
            print(("|"+ f" {print_dict[p]} " + ""), end="")
        print("|" + f" {i}")
    print("  ---------------------------------")
    print("    a   b   c   d   e   f   g   h")
    return

def is_valid_input(s : str) -> bool:
    moves = s.split(" ")
    if (len(moves) != 2):
        return False
    for m in moves:
        if (len(m) != 2 or m[0] not in translation_dict or int(m[1]) < 1 or int(m[1]) > 8):
            return False
    return True

def is_valid_move(board : list, from_s : str, to_s : str, piece):
    return NotImplementedError

def translate(s : str) -> (int, int):
    x = 8 - int(s[1])
    y = translation_dict[s[0]]
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

def chess():
    b = make_board()
    print_board(b)
    print("\n\n")
    players = [White.WHITE, Black.BLACK]
    p = 0
    contd = True
    while contd:
        p = p%2
        move = input(f"{players[p]}'s move: ")
        if not is_valid_input(move):
            print("Invalid input\n")
            continue
        # TODO: check valid move
        move_from, move_to = move.split(" ")[0], move.split(" ")[1]
        print(f"Move from {move_from}, move to {move_to}") 
        print("\n\n")
        p += 1
    
chess()
