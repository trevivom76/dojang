# makit 문자열 변수를 활용해 아래와 같은 실행 결과가 나오도록 코드의 빈칸을 완성하세요.
# 실행 결과
# S
# W
# !

# 코드
# makit='Sieun Woojin!'
# result = ___________
#
# print(result)
# result = ___________
#
# print(result)
# result = ___________
# print(result)

# 핵심 잡기
# 문자열은 연속된 메모리 공간에 저장됩니다.
# 연속된 공간은 0번 방부터 시작합니다.
# 이렇게 0번, 1번, 2번과 같이 연속된 공간의 방 번호를 인덱스(index)라고 합니다.
# 인덱스를 사용하면 문자열을 구성하는 문자 하나하나에 접근할 수 있습니다.
# 예를 들어, a라는 변수가 'makit' 이라는 문자열을 저장하고 있다면 문자 m은 a[0]에 저장되어 있습니다.
# 0부터 순서대로 1씩 증가하므로 맨 마지막 문자 k는 a[4]에 저장되어 있겠죠?
# 문자열의 마지막 문자를 접근하기 위해서는 맨 앞에 있는 0부터 시작해 ‘전체 문자 개수-1’로 접근할 수 있습니다.
# 마지막 문자에 접근하는 다른 방법은 인덱스 숫자 자리에 -1을 적는 것입니다.
# 그러므로 문자열 'makit'에서 t를 접근하기 위해서는 a[4]도 가능하고 a[-1]도 가능합니다.

makit='Sieun Woojin!'
result = makit[0]

print(result)
result = makit[6]

print(result)
result = makit[12]
print(result)
