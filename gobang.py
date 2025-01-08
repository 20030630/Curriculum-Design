import os

# 棋盘大小
BOARD_SIZE = 15

# 棋盘初始化
def init_board_yxl():
    return [["." for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# 打印棋盘
def print_board_yxl(board):
    os.system("cls" if os.name == "nt" else "clear")
    print("   " + "".join([f"{i:2}" for i in range(BOARD_SIZE)]))  # 无空格
    for i, row in enumerate(board):
        print(f"{i:2} " + " ".join(row))

# 检查是否胜利
def check_winner_yxl(board, x, y, player):
    directions = [
        (1, 0),  # 横向
        (0, 1),  # 纵向
        (1, 1),  # 主对角线
        (1, -1), # 副对角线
    ]

    def count_consecutive_yxl(dx, dy):
        count = 0
        nx, ny = x + dx, y + dy
        while 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[nx][ny] == player:
            count += 1
            nx += dx
            ny += dy
        return count

    for dx, dy in directions:
        total_count = 1 + count_consecutive_yxl(dx, dy) + count_consecutive_yxl(-dx, -dy)
        if total_count >= 5:
            return True
    return False

# 检查棋盘是否已满
def is_draw_yxl(board):
    for row in board:
        if "." in row:
            return False
    return True

# 玩家输入
def get_player_move_yxl(player):
    while True:
        try:
            move = input(f"玩家 {player} 的回合，请输入坐标（格式：x y）：")
            x, y = map(int, move.split())
            if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
                return x, y
            else:
                print("输入超出棋盘范围，请重新输入！")
        except ValueError:
            print("输入格式错误，请按 'x y' 格式输入！")

# 游戏主循环
def play_game_yxl():
    board = init_board_yxl()
    current_player = "X"

    print_board_yxl(board)
    while True:
        x, y = get_player_move_yxl(current_player)

        # 检查是否为空位
        if board[x][y] != ".":
            print("该位置已被占用，请选择其他位置！")
            continue

        # 落子
        board[x][y] = current_player
        print_board_yxl(board)

        # 检查是否胜利
        if check_winner_yxl(board, x, y, current_player):
            print(f"🎉 玩家 {current_player} 获胜！")
            break

        # 检查是否平局
        if is_draw_yxl(board):
            print("棋盘已满，游戏平局！")
            break

        # 切换玩家
        current_player = "O" if current_player == "X" else "X"

# 显示欢迎界面
def display_welcome_yxl():
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 40)
    print("🎮 欢迎来到五子棋游戏 🎮")
    print("=" * 40)
    print("规则说明：")
    print("1. 玩家 X 和玩家 O 轮流下棋。")
    print("2. 第一个在任意方向（横、竖或斜）连成 5 子的玩家获胜。")
    print("3. 输入坐标格式为 'x y'，例如 '7 8' 表示在第 7 行第 8 列下棋。")
    print("=" * 40)
    input("按 Enter 开始游戏...")

# 主函数
if __name__ == "__main__":
    display_welcome_yxl()
    play_game_yxl()
