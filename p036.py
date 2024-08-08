# 다음 실행 결과와 같이 코딩 과목의 시험 점수를 0점 이상~100점 이하의 값으로 입력받아 학점을 출력하는 코드를 작성하세요. 코딩 점수에 따른 학점은 아래와 같습니다.
#
# 90점 이상 : A학점
# 80점 이상 ~ 90점 미만 : B학점
# 70점 이상 ~ 80점 미만 : C학점
# 60점 이상 ~ 70점 미만 : D학점
# 60점 미만 : F학점
# 실행 결과
# 코딩 점수를 입력하세요:89
# B학점
# 핵심 잡기
# 코딩 점수에 따라 여러 가지로 나뉘어야 하므로
# if~elif~else 조건문을 사용하면 됩니다.
# if 조건문이 위에서부터 순서대로 조건식을 만족하는지 체크하고,
# 만족하지 않을 때는 다음 조건식을 체크합니다.
# 만약 조건문을 만족했다면 그에 따른 명령어를 실행하고 전체 조건문은 완료됩니다.
# 90점 이상이면 A학점이고, 80점 이상 90점 미만이면 B학점을 얻습니다.
# 그렇다면 조건문 순서에 따라
# 효율적인 코드를 작성하려면 어떻게 해야 할지 생각해 보세요.

n = int(input("코딩 점수를 입력하세요:"))
if n > 90:
    print('A학점')
elif 80 <= n < 90:
    print('B학점')
elif 70 <= n < 80:
    print('C학점')
elif 60 <= n < 70:
    print('D학점')
else:
    n < 60
    print('F학점')