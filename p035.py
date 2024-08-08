# 다음과 같이 0 이외의 정수 한 개를 입력받아, 음수 또는 양수, 짝수 또는 홀수로 구분해 출력하는 코드를 작성하세요. and와 or 연산자를 사용할 수 있으면 사용하세요.
# 실행 결과
# -14
# 음수이고 짝수
# 핵심 잡기
# 조건문의 조건식이 여러 가지일 때 and와 or 연산자를 조합해서 사용합니다. 예를 들어 나이가 10살 이상이고 몸무게가 70kg이상인 사람을 조건식으로 나타내면 if age >= 10 and weight >= 70:으로 표현할 수 있습니다.
# if 조건문이 3개 이상이면 if~elif~else 조건식을 사용합니다. 물론 마지막 else는 앞에 모든 조건식이 만족하지 않았을 때 사용하는 것이므로 조건식이 없습니다. 마찬가지로 if와 elif는 조건을 체크해야 하므로 모두 조건식이 존재합니다.
# and와 or연산자를 사용해 다중 조건을 한 줄에 입력하여 검사해도 되지만, 중첩 if문을 사용해서 코드를 작성해도 됩니다. 예를 들어 아래 두 코드는 같은 의미입니다.
# if age >= 10 and weight >= 70:
# if age >= 10: # age가 70 이상이고
#     if weight >= 70: # weight가 70 이상일 때0

n = int(input())

if n < 0 and n % 2 == 1:
    print('음수이고 홀수')
elif n < 0 and n % 2 == 0:
    print('음수이고 짝수')
elif n > 0 and n % 2 == 1:
    print('양수이고 홀수')
elif n > 0 and n % 2 == 0:
    print('양수이고 짝수')
else:
    print('0')


