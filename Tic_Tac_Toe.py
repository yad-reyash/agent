def calculate_heuristic(board, player):
    """
    Calculates e(p) = (Lines open for player) - (Lines open for opponent)
    """
    # Determine who the opponent is
    opponent = 'O' if player == 'X' else 'X'
    
    # 1. Identify all 8 possible winning lines (3 rows, 3 cols, 2 diagonals)
    winning_lines = []
    
    # Rows
    for row in board:
        winning_lines.append(row)
        
    # Columns
    for col in range(3):
        current_col = [board[row][col] for row in range(3)]
        winning_lines.append(current_col)
        
    # Diagonals
    diag1 = [board[i][i] for i in range(3)]       # Top-left to bottom-right
    diag2 = [board[i][2-i] for i in range(3)]     # Top-right to bottom-left
    winning_lines.append(diag1)
    winning_lines.append(diag2)
    
    # 2. Count open lines
    player_open_count = 0
    opponent_open_count = 0
    
    for line in winning_lines:
        # Check if line is open for Player (contains NO Opponent pieces)
        if opponent not in line:
            player_open_count += 1
            
        # Check if line is open for Opponent (contains NO Player pieces)
        if player not in line:
            opponent_open_count += 1
            
    # 3. Calculate Heuristic
    heuristic_value = player_open_count - opponent_open_count
    
    # --- Print details for demonstration ---
    print(f"Player ({player}) open lines: {player_open_count}")
    print(f"Opponent ({opponent}) open lines: {opponent_open_count}")
    
    return heuristic_value

# ==========================================
# Main Execution / Test Case
# ==========================================

# Representing the board: '-' is empty
# Example State:
#  X | - | - 
# ---+---+---
#  - | O | - 
# ---+---+---
#  X | - | - 

current_board = [
    ['X', '-', '-'],
    ['-', 'O', '-'],
    ['X', '-', '-']
]

# We want to calculate heuristic for player 'X'
current_player = 'X'

print("Current Board State:")
for row in current_board:
    print(row)
print("-" * 20)

h_val = calculate_heuristic(current_board, current_player)

print("-" * 20)
print(f"Heuristic Value e(p) = {h_val}")