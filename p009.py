# 정수와 실수를 각각 변수 a, b에 입력받아 두 숫자의 합과 평균을 구하는 코드를 작성하세요.
#
# 핵심 잡기
# 입력받은 결과는 문자열이므로 숫자로 사용하려면 자료형 변환을 해야 합니다. 정수는 int() 함수를, 실수는 float() 함수를 사용하면 됩니다.
# 키보드로 75.6을 입력받아 변수 a에 숫자 75.6으로 저장하려면 실수 자료형 float로 변환해야 합니다.
# a = float(input())

# input
# 3
# 2.5

# output
# a와 b의 합은 5.5
# a와 b의 평균값은 2.75

a = float(input())
b = float(input())
total = a + b
average = (a + b) / 2
print(f"a와 b의 합은 {total}")
print(f"a와 b의 평균값은 {average}")