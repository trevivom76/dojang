# 다음과 같이 숫자를 입력받아 1까지 카운트다운하고
# 마지막에 “발사!”라고 출력하는 코드를 for 반복문을 사용해 작성하세요.
# 실행 결과
# 카운트다운 몇 초 전인가요?10
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 발사!
# 핵심 잡기
# for 반복문 range를 사용해 반복문에서 사용하는 변수의 값이 하나씩 줄어들도록 코드를 작성하세요.
# for i in range(n, m, step):에서 step의 값이 음수라면
# 숫자 n부터 숫자 m+1까지 step만큼 줄어들면서 i에 값이 할당됩니다.
# for i in range(5, 0, -1):에서 i는 5부터 하나씩 줄어들어서 1까지 가능합니다.
# 즉 i는 차례대로  5, 4, 3, 2, 1이 되면서 반복문을 5번 수행합니다.
# for i in range(7, 2, -2):에서 i는 7부터 2씩 줄어들면서 3까지 가능합니다 .
# 즉i는 차례대로 7, 5, 3이 되면서 반복문은 3번 수행됩니다.

i = int(input("카운트다운 몇 초 전인가요?"))

while i >= 1:
    print(i)
    i -= 1

print("발사!")