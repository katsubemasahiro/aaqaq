import streamlit as st
import pandas as pd
import numpy as np

# サンプル数を増やす
np.random.seed(0)  # 乱数生成のシードを固定
x = np.random.rand(100) * 10  # 0から10までのランダムな値を100個生成
y = 2 * x + 1 + np.random.randn(100)  # xの値に依存したyの値を生成 (ノイズあり)

# サンプルデータを作成
data = pd.DataFrame({
    'x': x,
    'y': y
})

st.title('Scatter Chartaaaa')
# 散布図を表示
st.scatter_chart(data, x='x', y='y')
st.area_chart(data, x='x', y=['y1', 'y2'])