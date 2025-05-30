import streamlit as st
import pandas as pd

# 讀取 Excel 檔案
df = pd.read_excel("完整49項目整理.xlsx")

st.title("🌟 梅爾達大自然占卜")
st.write("點擊按鈕，隨機抽出一張牌")

if st.button("抽一張牌"):
    row = df.sample().iloc[0]  # 隨機選一列
    st.subheader(f" 抽到的牌：{row['主題']}")
    st.write(f"**連結**：{row['連結']}")
    st.write(f"**大局**：{row['大局']}")
    st.write(f"**個體**：{row['個體']}")
