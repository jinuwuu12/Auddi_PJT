
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
from auddi_scrap.items import dcinsideScrapItem, bobaeCommunityItem

class AuddiScrapPipeline:
    def process_item(self, item, spider):
        return item
    
class ExcelExportPipeline:
    def open_spider(self, spider):
        self.items = []

    def close_spider(self, spider):
        df = pd.DataFrame(self.items)
        df.sort_values(by='date', ascending= False, inplace=True)
        file_path = r"C:/Users/PC/Desktop/크롤링 데이터/google_stock_prices.xlsx"
        df.to_excel(file_path, index= False)
    
    def process_item(self, item, spider):
        self.items.append(item)
        return item
    
class kukminScrapPipeline:
    def content_item(self, item, spider):
        return item
    
import pandas as pd

class dcinsidePipeline:
    def __init__(self):
        # items 리스트를 초기화
        self.items = []

    def open_spider(self, spider):
        """스파이더가 시작될 때 호출되고, items 리스트를 초기화합니다."""
        self.items = []

    def close_spider(self, spider):
        """스파이더가 종료될 때 호출되고, 수집된 아이템을 엑셀 파일로 저장합니다."""
        # 수집된 아이템 리스트를 데이터프레임으로 변환
        df = pd.DataFrame(self.items)
        
        # 파일 경로 설정 (원하는 경로로 변경 가능)
        file_path = r"C:/Users/PC/Desktop/크롤링 데이터/dcinsideBoard.xlsx"
        
        # 엑셀 파일로 저장
        df.to_excel(file_path, index=False)
        print(f"데이터가 엑셀 파일로 저장되었습니다: {file_path}")

    def process_item(self, item, spider):
        """각 아이템을 items 리스트에 추가하고, 다음 파이프라인으로 전달합니다."""
        # 딕셔너리 형태로 변환 후 리스트에 추가
        self.items.append(dict(item))
        return item

    
class bobaePipeline:
    def __init__(self):
        # items 리스트를 초기화
        self.items = []

    def open_spider(self, spider):
        """스파이더가 시작될 때 호출되고, items 리스트를 초기화합니다."""
        self.items = []

    def close_spider(self, spider):
        """스파이더가 종료될 때 호출되고, 수집된 아이템을 엑셀 파일로 저장합니다."""
        # 수집된 아이템 리스트를 데이터프레임으로 변환
        df = pd.DataFrame(self.items)
        
        # 파일 경로 설정 (원하는 경로로 변경 가능)
        file_path = r"C:/Users/PC/Desktop/크롤링 데이터/보배외제차.xlsx"
        
        # 엑셀 파일로 저장
        df.to_excel(file_path, index=False)
        print(f"데이터가 엑셀 파일로 저장되었습니다: {file_path}")

    def process_item(self, item, spider):
        """각 아이템을 items 리스트에 추가하고, 다음 파이프라인으로 전달합니다."""
        # 딕셔너리 형태로 변환 후 리스트에 추가
        self.items.append(dict(item))
        return item