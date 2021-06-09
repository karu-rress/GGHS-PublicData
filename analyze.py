import csv
from basiclib import otd
from typing import List, Dict
from collections import Counter
from matplotlib import pyplot as plt

class analyzer:

    def __init__(self, filename: str='data.csv') -> None:
        self._file = open(filename, 'r', encoding='UTF-8')
        self._data = csv.reader(self._file)
        self._header = next(self._data)
        self._data = list(self._data)

    @property
    def data(self):
        return self._data

    def show_region(self) -> None:
        regions_data: List = self.get_data_row(1)
        regions = otd.rm_duplicate(regions_data)
        counts: List = [regions_data.count(it) for it in regions]
        
        result: Dict = {}
        for i in range(len(regions)):
            result[regions[i]] = counts[i]
        result = otd.sort_dict(result, False)
        
        plt.rc('font', family='Malgun Gothic')
        plt.figure(figsize=(10, 8))
        plt.barh(*zip(*result.items()))
        plt.title('경기도 내 지역별 사교육 시설 현황')
        plt.xlabel('학원 수')
        plt.ylabel('지역')
        plt.show()
        plt.close()

    def show_type(self) -> None:
        types_data: List = []
        for i in self.data:
            tp, *_ = i[6 - 1].split('(')
            types_data.append(tp)

        types = otd.rm_duplicate(types_data) # 중복제거
        subjects = ['국어', '수학', '사회', '과학', '영어', '입시']
        types = [x for x in types 
        if subjects[0] in x
        or subjects[1] in x
        or subjects[2] in x
        or subjects[3] in x
        or subjects[4] in x
        or subjects[5] in x]
        
        numbers: List = [0, 0, 0, 0, 0, 0]
        results: Dict = {}
        
        for i in range(6):
            for type in types:
                if subjects[i] in type:
                    numbers[i] += 1
            results[subjects[i]] = numbers[i]
            
        otd.sort_dict(results, False)

        plt.rc('font', family='Malgun Gothic')
        plt.figure(figsize=(5, 4))
        plt.bar(*zip(*results.items()))
        plt.title('유형별 학원 수')
        plt.xlabel('과목')
        plt.ylabel('학원 수')
        plt.show()

    def test_func(self):
        types_data: List = []
        for i in self.data:
            tp, *_ = i[6 - 1].split('(')
            types_data.append(tp)

        types = otd.rm_duplicate(types_data) # 중복제거
        subjects = ['국어', '수학', '사회', '과학', '영어']
        types = [x for x in types 
        if subjects[0] in x
        or subjects[1] in x
        or subjects[2] in x
        or subjects[3] in x
        or subjects[4] in x]
        
        numbers: List = [0, 0, 0, 0, 0]
        results: Dict = {}
        i = 0
        while i < 5:
            for type in types:
                if subjects[i] in type:
                    numbers[i] += 1
            results[subjects[i]] = numbers[i]
            i += 1
            
        otd.sort_dict(results, False)

        plt.rc('font', family='Malgun Gothic')
        plt.figure(figsize=(8, 6))
        plt.barh(*zip(*results.items()))
        plt.title('과목별 학원 수')
        plt.show()
        
    def scatter(self):
        # 위도: latitude, 경도: longitude
        latitude = [round(float(x), 5) for x in self.get_data_row(11) if x is not '']
        longitude = [round(float(x), 5) for x in self.get_data_row(12) if x is not '']

        pos = [(round(x, 2), round(y, 2)) for (x, y) in zip(latitude, longitude)]
        cnt = dict(Counter(pos)) # {(x, y): z,}
        # list(map(list, zip(*[(1, 2), (3, 4), (5, 6)])))
        # list(map(list, zip(*cnt.keys())))
        
        sub_lat, sub_lon = zip(*list(cnt.keys()))
        sub_cnt = [round(x/1.5)+10 for x in list(cnt.values())]

        plt.rc('font', family='Malgun Gothic')
        plt.figure(figsize=(7,7)).add_subplot(111).set_aspect('equal')

        img = plt.imread("map.png")
        #fig, ax = plt.subplots()
        #ax.imshow(img, extent=[-5, 80, -5, 30])

        plt.scatter(sub_lon, sub_lat, s=sub_cnt, c=range(len(sub_cnt)), cmap='Blues')
        plt.colorbar(label='단위 면적당 학원 분포 수')
        plt.xlabel('경도(˚E)')
        plt.ylabel('위도(˚N)')
        plt.title('지역별 학원 분포')

        plt.show()

    # starts with '1'
    def get_data_row(self, row: int) -> List:
        return [lt[row - 1] for lt in self.data]

    def __del__(self):
        self._file.close()