from pathlib import Path
import pandas as pd

# N225_master_path = Path("./master/N225_master.csv")
# N225_new_path = Path("./new_data/N225.csv")

master_list = list(Path("./master").glob("*.csv"))
new_list = list(Path("./new_data").glob("*.csv"))


def updata_master(master_path: Path | str, new_path: Path | str):
    master = pd.read_csv(master_path)
    new = pd.read_csv(new_path)
    columns = [
        "日付",
        "始値",
        "高値",
        "安値",
        "終値",
        "5日平均",
        "25日平均",
        "75日平均",
        "VWAP",
        "出来高",
        "出来高_5日平均",
        "出来高_25日平均",
    ]
    master.columns = columns
    new.columns = columns

    # 重複データの削除 & indexの振り直し
    master = pd.concat([new, master]).drop_duplicates().reset_index(drop=True)
    master = master.to_csv(master_path, index=False)
    print(f"{master_path.name} is updated.")


# 同じ名前のファイル同士で更新
for master_path in master_list:
    new_path = Path("./new_data") / master_path.name
    if new_path.exists():
        updata_master(master_path, new_path)
