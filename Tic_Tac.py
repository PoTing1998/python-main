counter = 0
row1 = ['', '', '']  
row2 = ['', '', '']  #4 , 5 , 6 =>row index 0 , 1 , 2
#4 , 5 , 6 =>row index 0 , 1 , 2
#1 , 2 ,0-1  =  0, 1 ,-1
row3 = ['', '', '']  

def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3) 

def user_choice():
    choice = input("Please enter your number (1-9): ")
    while not choice.isdigit() or (int(choice) not in range(1, 10)):
        if not choice.isdigit():
            print("Sorry ,Invalid input. Please enter a number.")
        else:
            print("Sorry, that number is not in the range 1-9.")
        choice = input("Please enter a valid number (1-9): ")
    return int(choice)
#user_choices()
# display = display(row1, row2, row3) 

def getCurrentSymbol():
    global counter
    symbol_list = ['X', 'O']
    counter += 1
    return symbol_list [ counter % 2]
def update_board(index):
    if index in range (1 , 4):
        row1[index - 1] = getCurrentSymbol()
    elif index in range (4, 7):
        row2[index % 3 - 1 ] = getCurrentSymbol()
    else:
        row3[index % 3 - 1 ] = getCurrentSymbol()


def start_game():
    while True:
        display(row1, row2, row3)
        choices= user_choice()

        update_board(choices)
def check_winning():
    player_1_wins =False
    player_2_wins = False
    
start_game()


display(row1, row2, row3)
# class TicTacToeTurnManager:
#     def __init__(self):
#         self.turn = 1  # 從第 1 次輸入開始
#     def next_turn(self):
#         """返回當前回合應該輸入的符號，並增加回合數。"""
#         if self.turn > 9:
#             return "Game Over"  # 超過 9 次輸入則結束

#         symbol = "X" if self.turn % 2 != 0 else "O"
#         self.turn += 1  # 更新回合數
#         return symbol

# # 測試
# manager = TicTacToeTurnManager()
# for _ in range(10):  # 測試 10 次
#     print(manager.next_turn())
