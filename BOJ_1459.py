x, y , w, s = map(int, input().split())

move = (x + y) * w #평행이동

#홀 짝 에 따른 이동
if(x + y) % 2 == 0:
    move2 = max(x,y) * s
else:
    move2 = (max(x,y) - 1) * s + w
#대각선 + 평행 이동
move3 =  (min(x,y) * s) + ((max(x,y) - min(x,y)) * w)

result = min(min(move, move2), move3)

print(result)