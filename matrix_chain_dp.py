#!/usr/bin/env python3
"""Matrix chain multiplication — optimal parenthesization via DP."""
import sys
def matrix_chain(dims):
    n = len(dims) - 1
    dp = [[0]*n for _ in range(n)]
    split = [[0]*n for _ in range(n)]
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1; dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + dims[i]*dims[k+1]*dims[j+1]
                if cost < dp[i][j]: dp[i][j] = cost; split[i][j] = k
    def parens(i, j):
        if i == j: return f"A{i+1}"
        return f"({parens(i, split[i][j])} × {parens(split[i][j]+1, j)})"
    return dp[0][n-1], parens(0, n-1)
if __name__ == "__main__":
    dims = [30, 35, 15, 5, 10, 20, 25]
    cost, order = matrix_chain(dims)
    print(f"Dimensions: {dims}")
    print(f"Optimal cost: {cost} multiplications")
    print(f"Order: {order}")
