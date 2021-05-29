from typing import List, Dict
import csv
import matplotlib.pyplot as plt

class Analyzer:
    def __init__(self):
        self.file = open('data.csv', 'r',encoding = 'UTF-8')
        self.data = csv.reader(self.file)
        self.header = next(self.data)

        # 전체리스트.count => regionsSet
        self.result: List = [] # 데이터 저장용 리스트

    
    def showRegion(self):
        # regionsList: csv에서 지역만을 담음
        regionsList: List = []
        for i in self.data:
            regionsList.append(i[0])

        regionsSet = list(set(regionsList)) # 중복제거
        counts: List = []
        for i in regionsSet:
            counts.append(regionsList.count(i))
        
        dataDict: Dict = {}
        for i in range(len(regionsSet)):
            # print(regionsSet[i], self.counts[i])
            dataDict[regionsSet[i]] = counts[i]

        dataDict = {k: v for k, v in sorted(dataDict.items(), key = lambda item:-item[1])} # 내림차순

        plt.rc('font', family = 'Malgun Gothic')
        plt.figure(figsize = (10, 5))
        plt.barh(*zip(*dataDict.items()))
        plt.show()

    def showType(self):
        pass

    def work(self):
        

        # dict 를 reverse로 재정렬할 것.
        for key, val in dict.items():
            print(key, val, '개')

    def __del__(self):
        self.file.close()

ui = Analyzer()
ui.showRegion()