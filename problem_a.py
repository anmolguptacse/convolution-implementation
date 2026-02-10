# problem_a.py
import random
import sys

def problem_a():
    # Fix seed for all file have same random value 
    random.seed(42)
    # if we are ruuning on same file then we can use random.random()
    #instead of fixing random values 
    # we can change seed value from 42 to random value but make 
    #sure it is same for both files other wise output will not match
    # it is use for proving implementation correctness

    
    # paramaetr declaration
    N, C, H, W = 8, 4, 28, 28
    R, S, M = 5, 5, 16
    stride = 2
    
    # dimension of output
    E = (H - R) // stride + 1
    F = (W - S) // stride + 1
    
    # Average pooling
    pool_size = 2
    pool_stride = 2
    E_pool = (E - pool_size) // pool_stride + 1
    F_pool = (F - pool_size) // pool_stride + 1
    


    def random_signed():
    # Generate number between 0 and 1
        value = random.random()  # 0 <= value < 1
    
    # Randomly choose positive/negative sign
        if random.random() < 0.5:
            return -value  # Negative
        else:
            return value   # Positive





    
    I = [[[[random_signed() for _ in range(W)] for _ in range(H)] for _ in range(C)] for _ in range(N)]
    Wgt = [[[[random_signed() for _ in range(S)] for _ in range(R)] for _ in range(C)] for _ in range(M)]
    B = [0.0 for _ in range(M)]
    
    # navie approch 7 loop
    O_conv = [[[[0.0 for _ in range(F)] for _ in range(E)] for _ in range(M)] for _ in range(N)]
    
    for n in range(N):
        for m in range(M):
            for x in range(E):
                for y in range(F):
                    val = B[m]
                    for i in range(R):
                        for j in range(S):
                            for k in range(C):
                                input_x = x * stride + i
                                input_y = y * stride + j
                                val += I[n][k][input_x][input_y] * Wgt[m][k][i][j]
                    O_conv[n][m][x][y] = val
    
    # Average pooling
    O_final = [[[[0.0 for _ in range(F_pool)] for _ in range(E_pool)] for _ in range(M)] for _ in range(N)]
    
    for n in range(N):
        for m in range(M):
            for x in range(E_pool):
                for y in range(F_pool):
                    total = 0.0
                    for i in range(pool_size):
                        for j in range(pool_size):
                            conv_x = x * pool_stride + i
                            conv_y = y * pool_stride + j
                            total += O_conv[n][m][conv_x][conv_y]
                    O_final[n][m][x][y] = total / (pool_size * pool_size)
    
    return O_final

if __name__ == "__main__":
    result = problem_a()
    checksum = 0.0
    N, M = 8, 16
    E_pool, F_pool = 6, 6
    for n in range(N):
        for m in range(M):
            for x in range(E_pool):
                for y in range(F_pool):
                    checksum += result[n][m][x][y]
    print(f"Problem a  checksum: {checksum:.6f}")