# 문제 016: and, or 그리고 not 연산자
# 다음 코드를 수행한 결과를 적어 보세요.
#
# 코드
a = 20
b = 30
print(a > 40 and b > 40)
print(a > 20 and b > 20)
print(a < 30 and b > 30)
print(a > 10 and b > 10)
print(20 > 40 or 30 > 40)
print(20 > 20 or 30 > 20)
print(20 < 30 or 30 > 30)
print(20 > 10 or 20 > 10)
print(a != b)
print(not(a != b))
# 핵심 잡기
# and 연산자는 A and B와 같이 표현하고 A와 B 모두 True인 경우에만 A and B 전체 결과가 True가 되고, 나머지 결과는 모두 False입니다.
# or 연산자는 A or B와 같이 표현하고 A와 B 둘 중에 하나 이상 True이면A or B 전체 결과가 True가 되고, 나머지 결과는 모두 False입니다.
# not 연산자는 not(True)는 False가 되고 not(False)는 True로 참과 거짓을 반대로 변경해주는 연산자입니다.
# 여러 개의 True와 False의 관계를 통해 최종적으로 True와 False의 결과를 얻는 연산자 and, or, not을 논리 연산자(logical operator)라고 합니다 .