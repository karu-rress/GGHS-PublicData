import csv
from basiclib import otd
from typing import List, Dict
from matplotlib import pyplot as plt


class analyzer:

    def __init__(self, filename: str='data.csv') -> None:
        self._file = open(filename, 'r', encoding = 'UTF-8')
        self._data = csv.reader(self._file)
        self._header = next(self._data)
        self._data = list(self._data)

    
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
        plt.show()

    def show_type(self) -> None:
        types_data: List = self.get_data_row(6)
        types = otd.rm_duplicate(types_data) # 중복제거
        counts: List = [types_data.count(it) for it in types]
        
        result: Dict = {}
        for i in range(len(types)):
            result[types[i]] = counts[i]
        result = otd.sort_dict(result, False)
        
        plt.rc('font', family='Malgun Gothic')
        plt.figure(figsize=(10, 8))
        plt.barh(*zip(*result.items()))
        plt.title('종류별 사교육 분포도')
        plt.show()

    def test_func(self):
        types_data: List = []
        for i in self._data:
            tp, *_ = i[3 - 1].split('(')
            types_data.append(tp)

        types = otd.rm_duplicate(types_data) # 중복제거
        print(types)
        
    # starts with '1'
    def get_data_row(self, row: int) -> List:
        return [lt[row - 1] for lt in self._data]

    def __del__(self):
        self._file.close()