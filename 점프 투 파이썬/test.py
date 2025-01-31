# 1+1 프로그램 
import sys


print(1+1)

"""
Hello Python 출력하기
"""

print("Hello Python")

for a in [1,2,3,4,5]:
    print(a)


# 1부터 10까지의 합
sum = 0
for i in range(1, 11):
    sum += i
    print(sum)
print("1부터 10까지의 합:", sum)


# 1부터 10까지의 곱하기
mul = 1
for i in range(1, 11):
    mul *= i
    print(mul)
print("1부터 10까지의 곱:", mul)

print("----------------------")

a = "Python"
print(a*2)

print("----------------------")

# 숫자형 
a = 3
b = 4
print(a+b)
print(a*b)
print(a/b)
print(a%b)
print(b%a)

print("----------------------")

# 1에서 10까지의 합
sum = 0
for i in range(1, 11):
    sum += i
    print(sum)

print("1에서 10까지의 합:", sum)

print("----------------------")
# 리스트 자료형
a = [1, 2, 3, 4, 5]
print(a)
print(a[0])
print(a[1])

for i in a:
    print(i)    

print("----------------------")    
# 딕셔널리 자료형 = java map
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a)
print(a['name'])

for i in a:
    print(i, a[i])
    
print("----------------------")
# boolean 자료형
a = True
b = False
print(a)
print(b)
print(a and b)
print(a or b)
print(not a)
print(not b)

print("----------------------")
# if and for 문 
marks = [90, 25, 67, 45, 80]   # 학생들의 시험 점수 리스트
number = 0   # 학생에게 붙여 줄 번호

for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)
        
# ranege 함수
a = range(0,10)
print(a)
for i in a:
    print(i)
        
# for와 range를 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')

# function 작성 
def add(a, b):
    return a+b

print(add(3, 4))

print("----------------------")
# 사용자 입출력 input
"""
a = input("Enter:")
print(a)
"""

print("----------------------")
# 파일 입출력 , 현재 폴더에
f = open("test.txt", "w")
f.write("Hello Python")
f.close()

print("----------------------")
# 파일 입출력 , 지정 폴더에
f = open("D:/test_python_file.txt", "w")
f.write("Hello Python")
f.close()

print("----------------------")
# 파일 입출력 , for 문 사용 입력
f = open("D:/test_python_file.txt", "w")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

print("----------------------")
# 파일 읽기 , 첫번째 라인
f = open("D:/test_python_file.txt", "r")
line = f.readline()
print(line)
f.close()

print("----------------------")
# 파일 읽기 , 전체내용
f = open("D:/test_python_file.txt", "r")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

print("----------------------")    
# readlines 함수 사용
f = open("D:/test_python_file.txt", "r")
lines = f.readlines()
for line in lines:
    line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)
f.close()

print("----------------------")
# read 함수 사용
f = open("D:/test_python_file.txt", "r")
data = f.read()
print(data)
f.close()

print("----------------------")
# 파일에 새로운 내용 추가하기
f = open("D:/test_python_file.txt", "a")
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

print("----------------------")
# with문과 함께 사용하기
# with 문을 사용하면 with 블록(with 문에 속해 있는 문장)을 벗어나는 순간, 열린 파일 객체 f가 자동으로 닫힌다
with open("D:/test_python_file.txt", "a") as f:
    f.write("Life is too short, you need python")
    
print("----- 04-4 프로그램 입출력 -----")    
args = sys.argv[1:]
for i in args:
    print(i)