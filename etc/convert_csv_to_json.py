from typing import List, Dict
from tqdm import tqdm
import csv
import json

def read_csv_file_data() -> List[Dict]:
    csv_file_path = "C:/Users/USER/book_title.csv"
    data = []  # JSON으로 변환할 데이터를 저장할 리스트

    with open(csv_file_path, "r", newline="", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in tqdm(csv_reader):
            book_id, title_author = row[0], row[1].split()
            title, author = ' '.join(title_author[:-1]), title_author[-1]
            data.append({
                "book_id": book_id,
                "Title": title,
                "author": author,
            })

    return data

# 데이터를 JSON 파일에 저장
def save_data_to_json(data: List[Dict]):
    json_file_path = "C:/Users/USER/book_title.json"

    with open(json_file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    data = read_csv_file_data()
    save_data_to_json(data)