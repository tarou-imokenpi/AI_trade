import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


# 前処理
def preprocess(X: pd.DataFrame):
    X.drop(columns=["日付"], inplace=True)
    X.replace("--", np.nan, inplace=True)  # "--"をnp.nanに変換
    X.replace(",", "", regex=True, inplace=True)  # ","を削除
    X.dropna(inplace=True)  # 欠損値を削除
    X = X.astype(np.float32)  # 型変換
    return X


X = pd.read_csv("./master/N225_master.csv")
X.drop(columns=["VWAP"], inplace=True)  # VWAP日経平均にはないので削除

X = preprocess(X)

# 説明変数と目的変数に分割
y = X["終値"]
X.drop(columns=["終値"], inplace=True)

# 学習データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# モデルの学習
# todo LSMT
# model = LinearRegression()
model = RandomForestRegressor()

model.fit(X_train, y_train)

# モデルの評価
score = model.score(X_test, y_test)
print(f"score: {score}")
