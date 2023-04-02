def solution(slice, n):
    if n%slice==0:
        return n//slice
    elif n%slice!=0:
        return n//slice+1