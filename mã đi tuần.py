n = 8

def isSafe(x, y, board):
    if x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1:
        return True
    return False

def printSolution(board):
    print(board)

def solveKT():
    board = [[-1 for i in range(n)] for i in range(n)] #tạo ra ma trận 8x8 tương ứng với bạn cờ 8x8

    move_x = [2, 1, -1, -2, -2, -1, 1, 2] #hướng con mã di chuyển theo trục x
    move_y = [1, 2, 2, 1, -1, -2, -2, -1] #hướng con mã di chuyển theo trục y

    board[0][0] = 0 #gán vị trí đầu tiên của con mã trên ma trận

    pos = 1 #đếm số lần con mã thực hiện một bước nhảy

    if (not solveKTUtil(board, 0, 0, move_x, move_y, pos)):
        print("Solution does not exist") 
    else: 
        printSolution(board) 
    
    return board
        
def solveKTUtil(board, curr_x, curr_y, move_x, move_y, pos):
    
    #Khi con mã đi tới ô thứ n**2 thì lúc đấy hàm solveKTUtil đã giải dc nên giá trị trả về sẽ là True
    if (pos == n**2):
        return True

    #Dùng một vòng lặp để lấy ra các hướng đi cho con mã
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if(isSafe(new_x, new_y, board)):
        #Dùng hàm isSafe để kiểm tra xem con mã có nằm trong bàn cờ hay không, \
        #nếu có thì vị trí hiện tại trả về sẽ bằng pos
            board[new_x][new_y] = pos
            #Tiếp tục sử dụng đệ quy gọi lại hàm solveKTUtil cho tới khi con mã không nằm trong bàn cờ
            if solveKTUtil(board, new_x, new_y, move_x, move_y, pos+1):
                return True
            
            board[new_x][new_y] = -1
    #Nếu hàm isSafe trả về giá trị False, hàm solveKT
    return False

if __name__ == "__main__":
    board = solveKT()
