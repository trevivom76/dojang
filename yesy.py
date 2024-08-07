T = int(input())
delta_x = [-1, 1, 0, 0, -1, -1, 1, 1]
delta_y = [0, 0, -1, 1, -1, 1, -1, 1]

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [list(input().strip()) for _ in range(N)]
    new_arr = [['' for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == '*':
            new_arr[i][j] = '*'
        else:
            cnt = 0
            for k in range(8):
                ci = i + delta_x[k]
                cj = j + delta_y[k]
                if 0 <= ci < N and 0 <= cj < M and arr[ci][cj] == '*':
                    cnt += 1
            new_arr[i][j] = str(cnt)

print(f'#{tc}')
for row in new_arr:
    print(''.join(row))