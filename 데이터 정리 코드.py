
import csv

results_dic1 = {} #시간대별 사고 구역으로 그릴꺼
results_dic2 = {}

#지방코드 판단해주는 함수
def defineRegionCode(n):
    if n == "서울":
        return "KR-11"

    elif n == "부산":
        return "KR-26"

    elif n == "대구":
        return "KR-27"

    elif n == "대전":
        return "KR-30"

    elif n == "광주":
        return "KR-29"

    elif n == "인천":
        return "KR-28"

    elif n == "울산":
        return "KR-31"

    elif n == "충북":
        return "KR-43"

    elif n == "충남":
        return "KR-44"

    elif n == "강원":
        return "KR-42"

    elif n == "경기":
        return "KR-41"

    elif n == "경북":
        return "KR-47"

    elif n == "경남":
        return "KR-48"

    elif n == "전북":
        return "KR-45"

    elif n == "전남":
        return "KR-46"

    elif n == "제주":
        return "KR-49"

    elif n == "세종":
        return "KR-50"

#각 시간대별 지역에서 일어난 사고수를 사전에 저장
def insertResultDic1(dic, line):
    time = int(line[1][11:13])//4 #4시간 단위로 나눈다
    province = line[9]
    #lng = line[24]
    #lat = line[25]
    if not time in dic:
        dic[time] = {}
    if not province in dic[time]:
        dic[time][province] = 1
    else:
        dic[time][province] += 1

#각 시간대별 사건이 일어난 위도 경도를 사전에 저장
def insertResultDic2(dic, line):
    time = int(line[1][11:13])//4
    province = line[9]
    lng = line[24]
    lat = line[25]
    tmp = [lat,lng,0,0]
    if not time in dic:
        dic[time] = [tmp]
    else:
        dic[time].append(tmp)

f = open('C:/Users/lg/Desktop/데이터사각화지도/도로교통공단_전국_사망교통사고정보(2018)_20190910 (1).csv', 'r')
rdr = csv.reader(f)

cnt = 0
for line in rdr:
    if(cnt == 0):
        cnt+=1
        continue
    #print(line[1][11:13], line[9], line[24], line[25])
    insertResultDic1(results_dic1, line)
    insertResultDic2(results_dic2, line)
    cnt += 1


for i in range(0,6):
    print(i)
    for key, value in results_dic1[i].items():
        print("['%s', %d]"%(defineRegionCode(key), value))

for i in range(0,6):
    print(i)
    print(results_dic2[i])
    print(' ')
    print(' ')
    print(' ')
    print(' ')

f.close()

