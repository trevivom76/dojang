# 문제 014: 문자열 바꾸기
# makit 문자열에 핸드폰 번호가 다음과 같이 저장되어 있습니다.
# ‘-‘를 ‘.’으로 변경해 다음과 같이 실행 결과가 나오도록 코드의 빈칸을 완성한 코드를 작성하세요.
#
# 실행 결과
# 010.1234.5678

phone = '010-1234-5678'
new_phone = phone.replace('-','.')
print(new_phone)