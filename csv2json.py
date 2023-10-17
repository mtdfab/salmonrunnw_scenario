import csv
import json

if __name__ == '__main__': 
    # CSVファイルの読み込み
    with open('database.csv', 'r', encoding='utf_8_sig') as f:
        d_reader = csv.DictReader(f)
        d_list = [row for row in d_reader]
    
    # datatablesで読めるようにdataで括る
    data = {'data':d_list}

    # JSONファイルへの書き込み
    with open('database.json', 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)