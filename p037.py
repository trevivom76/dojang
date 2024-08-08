# m, j, w, s 입력에 따라 각각 makit, james, woojin, sieun을 출력하고 m, j, w, s 이외의 문자가 입력되면 howard를 출력하는 코드를 작성하세요.
#
# 실행 결과
# s
# sieun
# 핵심 잡기
# 파이썬은 다른 언어보다 쉽게 코드를 작성할 수 있다는 장점이 있습니다.
# 파이썬 코드를 쉽게 작성해준다는 말에는 문자열 처리를 쉽게 하는 것도 포함됩니다.
# 문자열을 작은따옴표(' ') 또는 큰따옴표(" ") 사이에 감싸서 저장하고
# == 연산자를 활용하면 문자열이 서로 같은지 쉽게 비교할 수 있습니다.

# 사용자로부터 입력을 받는다
str_input = input().strip()

# 입력된 값에 따라 조건을 체크하고 출력한다
if str_input == 'm':
    print('makit')
elif str_input == 'j':
    print('james')
elif str_input == 'w':
    print('woojin')
elif str_input == 's':
    print('sieun')
else:
    print('howard')
