# テキストから入力を受け取る
import io
import sys

with open("Input.txt") as TxtOpen:
    INPUT = TxtOpen.read()
sys.stdin = io.StringIO(INPUT)

# ----------------------------
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(N, M)
print(A)
print(B)
