import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import matplotlib.ticker as mticker
from babel.numbers import format_currency
sns.set(style='dark')


all_df = pd.read_csv("main_data.csv")

all_df["yr_deskripsi"] = all_df["yr_deskripsi"].astype(str)

with st.sidebar:
    genre = st.multiselect(
    label="Pilih Tahun",
    options=('2011', '2012'),
    default=('2011', '2012')
)
filtered_df = all_df[all_df["yr_deskripsi"].isin(genre)] if genre else all_df


tabel = filtered_df.groupby(["season_deskripsi", "yr_deskripsi"], as_index=False)["cnt_y"].sum()

tabel_2 = filtered_df.groupby(by="kategorijam")["cnt_y"].mean().sort_values(ascending=False)



st.header(':dizzy: Data Calculation Bike User 2011-2012 :dizzy:')
st.subheader("Performa penjualan berdasarkan musim")


fig, ax = plt.subplots(figsize=(20, 10))
colors = ["#d47861", "#bbd461"]
sns.barplot(
    data=tabel, 
    x="season_deskripsi", 
    y="cnt_y", 
    hue="yr_deskripsi", 
    errorbar=None,
    palette=colors,
    ax=ax
)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=35)

st.pyplot(fig)




st.subheader("Performa penjualan berdasarkan kategori jam")

fig, ax = plt.subplots(figsize=(20, 10))
colors_ = ["#D14624"] + ["#D3D3D3"] * (len(tabel_2) - 1)

ax.bar(x=tabel_2.index, 
       height=tabel_2.values, 
       color=colors_)

ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=35)
st.pyplot(fig)