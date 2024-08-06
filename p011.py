# makit문자열 변수를 활용해 아래와 같은 실행 결과가 나오도록 코드의 빈칸을 완성하세요.
#
# 코드
# makit = 'Sieun Woojin!'
# ____________
# print(result)
# ____________
# print(result)
# _____________
# print(result)

# 핵심 잡기
# 문자열에서 부분 문자열을 뽑아낼 수 있습니다.
# 문자열 a = 'makit code lab'에서 문자열 일부인 code를 뽑아내려면 [c의 인덱스 번호:e의 다음 인덱스 번호]를 적으면 됩니다.
# 예를 들어 a[6:10]라고 하면 부분 문자열 code가 됩니다.
# 처음 인덱스 번호와 마지막 인덱스 번호는 생략할 수도 있습니다.
# 예를 들어 처음부터 시작해서 makit만을 뽑아낸다면 a[0:5]도 가능하지만, a[:5]라고 해도 결과는 같습니다.
# 마찬가지로 lab은 a[11:]가 됩니다 .
# 11번째 인덱스 문자부터 문자열 끝까지의 부분 문자열을 뽑아냅니다.
# a[:]는 무엇을 의미할까요?
# 처음부터 끝까지 문자열을 의미하므로 a 문자열 그 자체가 됩니다.

# 예
# 결과
# eun Woo
# Sieun
# Woojin!


makit = 'Sieun Woojin!'
result = makit[2:9]
print(result)
result = makit[0:5]
print(result)
result = makit[6:13]
print(result)