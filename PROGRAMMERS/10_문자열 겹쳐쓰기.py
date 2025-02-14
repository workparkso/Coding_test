"""
✅문제 설명
문자열 my_string, overwrite_string과 정수 s가 주어집니다. 문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 문자열 overwrite_string으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.

제한사항
my_string와 overwrite_string은 숫자와 알파벳으로 이루어져 있습니다.
1 ≤ overwrite_string의 길이 ≤ my_string의 길이 ≤ 1,000
0 ≤ s ≤ my_string의 길이 - overwrite_string의 길이


입출력 예
my_string	    overwrite_string	s	result
"He11oWor1d"	  "lloWorl"	        2	"HelloWorld"
"Program29b8UYP"	"merS123"	    7	"ProgrammerS123"

입출력 예 설명
입출력 예 #1
예제 1번의 my_string에서 인덱스 2부터 overwrite_string의 길이만큼에 해당하는 부분은 
"11oWor1"이고 이를 "lloWorl"로 바꾼 "HelloWorld"를 return 합니다.

입출력 예 #2
예제 2번의 my_string에서 인덱스 7부터 overwrite_string의 길이만큼에 해당하는 부분은 
"29b8UYP"이고 이를 "merS123"로 바꾼 "ProgrammerS123"를 return 합니다.

✅목적: 문자열을 어떻게 겹쳐지는지 아는지 확인 목적

# solution은 파이썬 함수 이름, 
# 매개변수 즉 파라미터는 괄호 안에 있는 것들, 
# def는 파이썬에서 함수를 정의할 때 사용하는 키워드이다.
"""

# 코드 작성 

def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer

# return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):] 으로 바로 작성 가능하다.




"""
✅다른 사람 풀이

1.
def solution(my_string, over, s):
    a=list(my_string)
    b=list(over)
    a[s:s+len(b)]=b # a의 s번 인덱스부터 over의 길이만큼 부분을 b로 덮어쓰기
    return ''.join(a)
    
1-1.
예시로 a = ['H', 'e', 'l', 'l', 'a', 'b', 'c', 'W', 'o', 'r', 'l', 'd']라면, 
''.join(a)는 "HellabcWorld" 가 된다.
"""



# ✅ 리스트와 join 함수를 활용해서도 나타낼 수 있다는 것을 알게 되었다.
