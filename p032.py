# 다음과 같이 정수 두 개를 x, y로 입력받아 x가 y보다 크면 'makit'을, 작거나 같으면 'woojin'을 출력하는 코드를 작성하세요.
#
# 실행 결과
# 첫 번째 정수를 입력하세요:7
# 두 번째 정수를 입력하세요:10
# woojin
# 핵심 잡기
# 성적에 따라 학점이 여러가지로 나뉘듯이, 코드를 작성하다가 여러 가지로 나누어서 일을 진행해야 할 때는 조건문 if를 사용해 갈림길을 만들 수 있습니다.
# 두 가지 갈림길로 만들기 위해서 if~else 조건문을 사용해보세요.
# 파이썬은 들여쓰기에 민감한 프로그래밍 언어입니다.
# 즉 들여쓰기가 올바로 되어 있지 않으면 오류가 발생합니다.
# if와 else는 들여쓰기가 같아야 합니다.

######
# x, y = list(map(int, input().split()))
# print('첫 번째 정수를 입력하세요 :' , x)
# print('두 번째 정수를 입력하세요 :' , y)
# if x > y:
#     print('makit')
# else:
#     print('woojin')

x = int(input("첫 번째 정수를 입력하세요:"))
y = int(input("두 번째 정수를 입력하세요:"))
if x > y:
    print('makit')
else:
    print('woojin')

