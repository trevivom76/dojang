# 다음과 같이 1보다 같거나 큰 수를 입력받고
# 1부터 입력받은 수까지의 합을 구하는 코드를 while 반복문을 사용해 코드를 작성하세요.
#
# 실행 결과
# # 입력
# 10
# # 출력
# 1부터 10 까지 모두 더한 합은 55
# 핵심 잡기
# while 반복문을 수행하면서 반복할 때마다 변경되는 변숫값을 더해가면서 문제를 해결할 수 있습니다.
# while 반복문에 사용되는 변숫값은while 반복문 시작 전에 초기화해야 합니다.
# while 반복문을 수행하면서 변숫값이 직접 증가 또는 감소를 해야 합니다.
# print("# 입력")
# n = int(input())
# sum = 0
# i = 1
#
# while n >= i:
#     sum += i
#     i += 1
#
# print("# 출력")
# print(f'1부터 {n} 까지 모두 더한 합은 {sum}')

# 입력 받기
n = int(input())

# 합계와 반복 변수 초기화
total_sum = 0
i = 1

# 1부터 n까지의 합을 계산
while i <= n:
    total_sum += i
    i += 1

# 결과 출력
print(f'1부터 {n} 까지 모두 더한 합은 {total_sum}')
