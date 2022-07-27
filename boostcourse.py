#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Q1 가위바위보 게임 만들기
import random

def rcp(user):
    computer = random.randint(0,2)
    rcp_dic = { 0 : "가위", 1 : "바위", 2 : "보"}
    print("컴퓨터: " + rcp_dic[computer])
    
    if (user == 0 and computer == 0) or (user == 1 and computer == 1) or (user == 2 and computer == 2):
        print("비겼습니다!")
    elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
        print("나의 승리!")
    elif (user == 0 and computer == 1) or (user == 1 and computer == 2) or (user == 2 and computer == 0):
        print("컴퓨터 승리!")
    else:
        print("잘못 입력하셨습니다.")
    


user = input("가위 바위 보를 입력하세요 (0.가위, 1.바위, 2.보)")

if user == '가위' or user == '0':
    print("나: 가위")
    user = 0
elif user == '바위' or user == '1':
    print("나: 바위")
    user = 1
elif user == '보' or user == '2':
    print("나: 보")
    user = 2

rcp(user)


# In[12]:


#Q2 연봉 계산기
monthly_payment = int(input("월급을 입력하세요"))
yearly_payment = monthly_payment * 12

if yearly_payment <= 1200:
    at_yearly_payment = yearly_payment * 0.94
elif yearly_payment <= 4600:
    at_yearly_payment = yearly_payment * 0.85
elif yearly_payment <= 8800:
    at_yearly_payment = yearly_payment * 0.76
elif yearly_payment <= 15000:
    at_yearly_payment = yearly_payment * 0.65
elif yearly_payment <= 30000:
    at_yearly_payment = yearly_payment * 0.62   
elif yearly_payment <= 50000:
    at_yearly_payment = yearly_payment * 0.60
else:
    at_yearly_payment = yearly_payment * 0.58
    
print("세전 연봉: %d만원" %yearly_payment)
print("세후 연봉: %d만원"%at_yearly_payment)


# In[16]:


#Q3 학점변환기
name = input("이름을 입력해주세요")
score = int(input("점수를 입력해주세요"))

if score >= 95 and score <= 100:
    grade = "A+"
elif score >= 90 and score < 95:
    grade = "A"
elif score >= 85 and score < 90:
    grade = "B+"
elif score >= 80 and score < 85:
    grade = "B"
elif score >= 75 and score < 80:
    grade = "C+"
elif score >= 70 and score < 75:
    grade = "C"
elif score >= 65 and score < 70:
    grade = "D+"
elif score >= 60 and score < 65:
    grade = "D"
elif score < 60:
    grade = "F"
else:
    print("잘못 입력하셨습니다.")
    
print()
print("학생이름: %s" %name)
print("점수: %d" %score)
print("학점: %s" %grade)


# In[21]:


#Q4 버스요금계산기
age = int(input("나이를 입력하세요"))
pay_method = input("지불 유형을 입력해주세요 1.현금, 2.카드")

if pay_method == '1':
    pay_method = "현금"
elif pay_method == '2':
    pay_method = "카드"
    

if age < 8 or age >= 75:
    pay = 0
elif age < 14:
    pay = 450
elif age < 20:
    if pay_method == "현금":
        pay = 1000
    elif pay_method == "카드":
        pay = 720
    else:
        print("잘 못 입력하셨습니다.")
elif age < 75:
    if pay_method == "현금":
        pay = 1300
    elif pay_method == "카드":
        pay = 1200
    else:
        print("잘 못 입력하셨습니다.")
else:
    print("잘 못 입력하셨습니다.")
    

print("\n나이: %d세" %age)
print("지불유형: %s" %pay_method)
print("버스요금: %d" %pay)


# In[ ]:




