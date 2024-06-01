# テキストから入力を受け取る
import argparse
import io
import sys


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, default="sample1.txt")
    return parser.parse_args()


parser = get_args()

with open(parser.input) as TxtOpen:
    INPUT = TxtOpen.read()
sys.stdin = io.StringIO(INPUT)

# ----------------------------
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(N, M)
print(A)
print(B)
