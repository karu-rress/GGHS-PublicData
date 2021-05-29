import csv
from basiclib import otd
from typing import List, Dict
from matplotlib import pyplot as plt


class analyzer:

    def __init__(self, filename: str='data.csv') -> None:
        self.file = open(filename, 'r', encoding = 'UTF-8')
        self.data = csv.reader(self.file)
        self.header = next(self.data)
        self.result: List = [] # 데이터 저장용 리스트
        plt.rc('font', family='Malgun Gothic')
    
    def show_region(self) -> None:
        regions_data: List = []
        for i in self.data:
            regions_data.append(i[0])

        regions = otd.rm_duplicate(regions_data)
        counts: List = []
        for i in regions:
            counts.append(regions_data.count(i))
        
        dataDict: Dict = {}
        for i in range(len(regions)):
            dataDict[regions[i]] = counts[i]
        dataDict = otd.sort_dict(dataDict, False)
        
        plt.figure(figsize=(10, 8))
        plt.barh(*zip(*dataDict.items()))
        plt.title('경기도 내 지역별 사교육 시설 현황')
        plt.show()

    def show_type(self) -> None:
        typesList: List = []
        for i in self.data:
            typesList.append(i[5])

        typesSet = otd.rm_duplicate(typesList) # 중복제거
        counts: List = []
        for i in range(len(typesSet)):
            pass

    def __del__(self):
        self.file.close()