"""
✅문제 설명
영어 알파벳으로 이루어진 문자열 str이 주어집니다. 
각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

제한사항
1 ≤ str의 길이 ≤ 20
str은 알파벳으로 이루어진 문자열입니다.
입출력 예
입력 #1

aBcDeFg
출력 #1

AbCdEfG

✅목적: 대문자와 소문자를 바꾸는 방법을 아는지 확인 목적

.isupper() : 문자열이 모두 대문자로 이루어져 있으면 True를 반환
.islower() : 문자열이 모두 소문자로 이루어져 있으면 True를 반환
"""

# 코드 작성(빈문자열 생성해서 보다 효율적인 코드 작성)
str = input()
str2 = ''

for i in str:
    if i.isupper() == True:
        str2 += i.lower()
    elif i.islower() == True:
        str2 += i.upper()

print(str2)


"""
✅다른 사람 풀이

1.
print(input().swapcase())

.swapcase()는 문자열의 모든 대소문자를 서로 바꾸는 메서드이다. 
즉, 문자열에 포함된 대문자는 소문자로, 소문자는 대문자로 변경한다.

2.
print(''.join(x.upper() if x == x.lower() else x.lower() for x in input()))
for x in input()은 입력된 문자열의 각 문자를 순차적으로 처리한다.
x == x.lower()는 해당 문자가 소문자인지 확인 후,
만약 x가 소문자라면, x.upper()로 대문자로 변환한다.
만약 x가 대문자라면, x.lower()로 소문자로 변환한다.
''.join(...)은 각 문자 변환 결과를 하나의 문자열로 합친다.

"""


# ✅ 바로 대문자 소문자 바꾸는 함수가 있을까? 보다는 어떤 과정을 거칠 수 있는지를 판단하자.
