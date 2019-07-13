import random
num =[6,7,8]
s = random.choice(num)
i = random.choice(num)
class rpg:
    def __init__(self, name, s , i):
        self.name = name
        self.s=s
        self.i=i
        
    def select(self, s, i):
        if s>i:
            self.s = s
            self.i = i
            self.job = "전사"
        if s<i:
            self.s = s
            self.i = i
            self.job = "법사"
        if s==i:
            self.s = s
            self.i = i
            self.job = "궁수"
            
        
        
name = input("캐릭터의 이름을 입력하세요 : ")
rpg1 = rpg(name, s, i)
rpg1.select(s,i)
print("캐릭터의 이름 :",rpg1.name)
print("캐릭터 정보 : 힘(",rpg1.s,")",", 지력(",rpg1.i,")")
print("캐릭터 직업 :",rpg1.job)
