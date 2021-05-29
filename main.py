from typing import List, Dict
import csv
import matplotlib.pyplot as plt

class Analyzer:
    def __init__(self):
        self.file = open('data.csv', 'r',encoding = 'UTF-8')
        self.data = csv.reader(self.file)
        self.header = next(self.data)

        self.regionsList: List = []
        for i in self.data:
            self.regionsList.append(i[0])
        self.regions = list(set(self.regionsList))

        # 리스트를 선회하면서 0번, 1번, .... n번 인덱스 참조
        self.counts: List = [] # int0

        # 전체리스트.count => self.regions

        self.result: List = [] # 데이터 저장용 리스트

    def work(self):
        
        for i in self.regions:
            self.counts.append(self.regionsList.count(i))
        
        dict: Dict = {}
        for i in range(1, 31):
            # print(self.regions[i], self.counts[i])
            dict[self.regions[i]]=self.counts[i]

        dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}
        # dict 를 reverse로 재정렬할 것.
        for key, val in dict.items():
            print(key, val, '개')

    def __del__(self):
        self.file.close()

ui = Analyzer()
ui.work()