import sys
sys.stdin = open('input.txt')

T = input()

if T.islower():
    tc = T.upper()
    
else:
    tc = T.lower()

print(f"{T}(ASCII: {ord(T)}) => {tc}(ASCII: {ord(tc)})")
