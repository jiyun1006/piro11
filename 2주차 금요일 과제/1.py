import time

class suspect:
    def __init__(self,p,e,m,v,l):
        self.ps_mosup = p  #평소 모습, 피해자에 대한 진술
        self.event = e #최근 사건
        self.body_check = m #몸 수색시 특이점
        self.visit_purpose = v #방문 목적
        self.last = l
class police:
    def __init__(self,s):
        self.susang = s #수상하거나 특이한점

def display(line):
    for i in line:
        print(i,end="")
        time.sleep(0.01)
    print()
    print()

def check_(a):
    print('-----------------') 	
    print('무엇을 조사하시겠습니까?') 
    print('1. 대상의 평소모습을 알아보고\n   피해자에 대한 진술을 조사하자.')
    print('2. 살해 추정 동기를 알아보자')
    print('3. 몸수색을 해보자') 
    print('4. 방문목적을 알아보자') 
    print('-----------------')
    while True:
        cho3 = input(" ")
        if cho3=='1' or cho3=='2' or cho3=='3' or cho3=='4':
            break
        print('정확한 숫자를 입력하세요')
        print()


    print()
    if  int(cho3)==1:
        display(a.ps_mosup)
    elif  int(cho3)==2:
        display(a.event)
    elif  int(cho3)==3:
        display(a.body_check)
    elif  int(cho3)==4:
        display(a.visit_purpose)
    time.sleep(1.5)


이즈미 = suspect('평소모습: 평소 바지 밑단을 접고 다니는 것 같군. \n피해자에 대한 진술: "사장님은 평소 직원 및 주위 사람과의 관계가 별로 좋지 않았습니다." ',
              "이즈미: 저는 사장의 지시로 받은 투자가 큰 손실이 나서 고소당할 예정입니다..",
              "이즈미의 바지 자락에서 렌즈 한알이 발견됨!",
              "이즈미: 저는 사장님과의 업무 협의를 위해 방문했었습니다.",
"이즈미: 저는 죽이지 않았어요. 애초에 제가 갔던 시간 이후에도 사장님이 살아있다는 것을 알 수 있잖아요!")
치히로 = suspect('평소모습: 평소 보라색 립스틱을 바르고 다니는걸로 보이는 군, \n피해자에 대한 진술: "엄마는 평소 눈이 안좋아 렌즈를 착용했어요. 안경은 불편하다면서 말이죠"',
              "치히로: 저는 남편을 위해 엄마에게 돈을 받으려다가 크게 싸웠었습니다..",
              "치히로의 핸드백에서 보라색 립스틱이 발견됨!",
              "치히로: 저는 엄마가 불러서 이 곳에 왔었어요. 잔소리를 하려고 불렀던 모양이에요",
"치히로: 제가 엄마로 변장해서 경비원을 맞이한건 맞아요. 근데 제가 죽이지는 않았어요!")
오카 = suspect('평소모습: 대머리라서 머리카락이 없군, \n피해자에 대한 진술: "사장은 성격은 고약해도 사업 수완이 매우 뛰어났습니다."',
             "오카: 사장이 저의 횡령 사실을 알아내서 저는 이에 대해 사장과 교섭하려 했습니다..",
             "본인의 횡령 사실을 증명하는 보고서 봉투가 발견됨!(본래 소유자는 사장인것 같다)",
             "오카: 저는 사업에 대한 협상을 위해 방문했었습니다.",
             "오카: 나는 그저 신고를 했을 뿐이야. 이 보고서가 발견되면 내가 의심받을 것 같아서 가지고 나온 것 뿐이야.!")
경찰  = police("경비원: 아 그러고 보니 사모님은 9시에 확인했을 때 보라색 립스틱을 바른 상태였습니다! 팩을 한 채로  립스틱을 바른 것이 특이해서 기억이 납니다.")

경찰2 = police("경찰: 시체는 잠옷을 입고 마스크를 쓴 채 죽어있었습니다. 사인은 질식사. 그나저나 마스크 팩을 굉장히 깔끔하게 붙였었네요, 저는 잘 못하겠던데.")
미란이 = police("란: 그러고 보니 피해자는 입을 벌리고 죽었는데 마스크에 주름이 하나도 없어.. 뭔가 이상하지 않아?")



print('코난 추리 게임: 얼굴 팩 살인사건')
time.sleep(2)
print(' 어느 늦은 금요일 저녁 코난은 가족들과 함께 저녁 식사를 한 후 식당에서 나오던 참이었다. 그의 주머니에서 전화기의 울음 소리가 요란하게 들렸다.')
time.sleep(4)
print('살인 사건 발생이다!!! 세기의 명탐정 코난.....오늘 불금은 글렀구나....\n')
time.sleep(4)
print('살인 현장 도착...\n')
time.sleep(4)
print('사망 추정시각: 21시 10분\n')
time.sleep(4)
print('현장에는 경찰과 용의자 세 명 이즈미, 치히로, 오카가 있었다. 그리고 마스크 팩을 한채로 싸늘하게 입을 벌리고 죽어있는 시체…')
time.sleep(4)
print('피해자는 화장품 회사를 경영하는 걸출한 사업가이다. 입가에는 매력진 주름을 가지고 있다.')
time.sleep(4)
print('그리고 경찰의 조사에 의하면 용의자와 피해자의 관계는 다음과 같다.\n')
time.sleep(4)
print('이즈미는 피해자 회사의 직원 중 한 명이다.\n치히로는 피해자의 자녀 중 둘째 딸이다.\n오카는 피해자와 애증의 사업 파트너 관계다.\n')
time.sleep(4)
print('코난의 표정은 일그러졌다. 하지만 이내 아무렇지 않다는 듯이 사건을 조사하기 시작했다.\n')
time.sleep(4)
print('그는 현관 CCTV를 먼저 살펴 보았다. CCTV에는 세 명의 용의자의 모습 그리고 경비원 두 명의 모습이 찍혔다.\n')
time.sleep(4)
print('2019/07/12 20:03:06 이즈미가 초인종을 누르자 집안의 한 여성이 문을 열어준다\n')
time.sleep(4)
print('2019/07/12 20:40:37 이즈미가 현관문을 열고 급하게 나간다.\n')
time.sleep(4)
print('2019/07/12 20:51:14 치히로가 현관문의 열쇠를 꽂는다. 문이 열린다.\n')
time.sleep(4)
print('2019/07/12 21:00:32 경비원들과 집안에서 나온 마스크 팩을  한 여성이 얘기를 나눈다. 그리고 마당 앞을 기웃거리는 고양이를 가리킨다.\n')
time.sleep(4)
print('고양이 때문에 침입 센서가 작동했던 모양인듯 하다.\n')
time.sleep(4)
print('2019/07/12 21:09:56 치히로가 집 밖을 나선다.\n')
time.sleep(4)
print('경비원과 얘기를 나누는 동안 딸은 집 안에 있었다는 건가?\n')
time.sleep(4)
print('2019/07/12 21:22:16 오카가 집을 들어간다.\n')
time.sleep(4)
print('2019/07/12 21:23:46 오카가 손에 서류 봉투를 들고 두리번 거리며 나온다.\n')
time.sleep(4)
print('우리의 명탐정 코난...뭔가 석연찮은 듯한 표정을 짓는다.\n')
time.sleep(4)
print('당신은 혼란에 빠진 코난을 도와줄 수 있습니다.\n')
time.sleep(4)



while True:
    print('------------------------------')
    print('1. 조사를 한다.')
    print('2. 범인을 지목한다.')
    print('------------------------------')
    
    while True:
        cho = input(" ")
        if cho=='1' or cho=='2':
            break
        print('정확한 숫자를 입력하세요')
        print()



    if  int(cho)==1:
        print()
        print('---------------------')
        print('누구와 이야기해볼까?')
        print('1. 경비원')
        print('2. 이즈미')
        print('3. 치히로')
        print('4. 오카')
        print('5. 경찰')
        print('6. 미란이')
        print('---------------------')

        while True:
            cho2 = input(" ")
            if cho2=='1' or cho2=='2' or cho2=='3' or cho2=='4' or cho2=='5' or cho2=='6':
                break
            print('정확한 숫자를 입력하세요')
        print()


        
        if int(cho2)==1:
            display(경찰.susang)
            time.sleep(1.5)
        elif  int(cho2)==2:
            check_(이즈미)
        elif  int(cho2) == 3:
            check_(치히로)
        elif  int(cho2) == 4:
            check_(오카)
        elif int(cho2) == 5:
            display(경찰2.susang)
        elif int(cho2)==6:
            display(미란이.susang)	
    
    elif cho=="선택" or cho=='2':

        print()	
        print('---------------------')
        print('범인을 지목하세요')
        print('1. 이즈미')
        print('2. 치히로')
        print('3. 오카')
        print('---------------------')

        while True:
            con = input("")
            if con=='1' or con=='2' or con=='3' :
                break
            print('정확한 숫자를 입력하세요')
            print()

        print('마지막 최후변론을 들어보자.')
        if con=='1':
            display(이즈미.last)
            l_cho = input('정말 이사람이 범인이 맞을까? : 1.Yes, 2.No\n')
            print('---------------------')
            if int(l_cho) == 1:
                print('범인을 찾았다.')
                break
            else:
                print('다시 생각해보자')
                continue
	
        if con=='2':
            display(치히로.last)
            l_cho = input('정말 이사람이 범인이 맞을까? : 1.Yes, 2.No\n')
            if int(l_cho) == 1:
                print('범인 찾는것을 실패다. 다 죽었다..이런!')
                break;
            else:
                print('다시 생각해보자')
                continue
        if con=='3':
            display(오카.last)
            l_cho = input('정말 이사람이 범인이 맞을까? : 1.Yes, 2.No\n')
            if int(l_cho) == 1:
                print('범인 찾는것을 실패했다. 다 죽었다..이런!')
                break
            else:
                print('다시 생각해보자')
                continue
        
        
