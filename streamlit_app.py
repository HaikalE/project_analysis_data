import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

st.title("Proyek Analisis Data: Bike Sharing Dataset")

st.write("Nama: Muhammad Haikal Rahman")
st.write("Email: muhammadhaikalrahman81@gmail.com")
st.write("Id Dicoding: haikal1231")

st.subheader("A. Pertanyaan Bisnis")
st.write("1. Apakah kecepatan angin atau kelembapan mempengaruhi keputusan masyarakat untuk menyewa sepeda?")
st.write("2. Apakah ada jam (jam) tertentu saat rental sepeda mencapai puncak atau penurunannya?")

data = pd.read_csv("Bike-sharing-dataset/day.csv")
data_2 = pd.read_csv("Bike-sharing-dataset/hour.csv")

st.subheader("B. Data Overview")

st.write("day.csv")
st.dataframe(data)

st.write("hour.csv")
st.dataframe(data_2)

st.subheader("C. Summary Statistics")

st.write("day.csv")
st.write(data.describe())

st.write("hour.csv")
st.write(data_2.describe())

st.subheader("D. Data Visualization")
st.write("Jawaban pertanyaan-1")

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.scatterplot(data=data, x='windspeed', y='cnt')
plt.title('Scatter Plot of Windspeed vs. Bike Rental Count')
plt.xlabel('Windspeed')
plt.ylabel('Bike Rental Count')

plt.subplot(1, 2, 2)
sns.scatterplot(data=data, x='hum', y='cnt')
plt.title('Scatter Plot of Humidity vs. Bike Rental Count')
plt.xlabel('Humidity')
plt.ylabel('Bike Rental Count')

plt.tight_layout()

st.pyplot(plt)

windy_days = data[data['windspeed'] >= data['windspeed'].median()]
non_windy_days = data[data['windspeed'] < data['windspeed'].median()]

t_stat, p_value = ttest_ind(windy_days['cnt'], non_windy_days['cnt'])


st.write("Jawaban pertanyaan-2")

data_2['dteday'] = pd.to_datetime(data_2['dteday'])


plt.figure(figsize=(12, 6))
sns.lineplot(x='hr', y='cnt', data=data_2, estimator='mean')
plt.title("Average Bike Rentals by Hour")
plt.xlabel("Hour of the Day")
plt.ylabel("Average Rental Count")
plt.grid(True)
st.pyplot(plt)

st.subheader("E. Conclusion")
st.markdown("##### Conclusion Pertanyaan 1")
st.write("Terdapat perbedaan signifikan dalam jumlah sewa sepeda antara hari berangin dan tidak berangin berdasarkan kecepatan angin. Nilai T-statistik negatif sebesar -6,06 dan nilai p yang sangat rendah sebesar 0,0000 menunjukkan signifikansi statistik yang kuat. Oleh karena itu, kami menolak hipotesis nol yang berarti kecepatan angin mempunyai pengaruh yang signifikan terhadap keputusan masyarakat untuk menyewa sepeda.")

data_2['dteday'] = pd.to_datetime(data_2['dteday'])



st.markdown("##### Conclusion Pertanyaan 2")
st.write("Dalam analisis ini, kita dapat menyimpulkan tentang pola peminjaman sepeda berdasarkan waktu (jam) dari dataset yang diberikan:")
st.write("Puncak Peminjaman Tertinggi (Top 5 Jam):")
st.write("1. Jam 17:00 (5:00 PM) memiliki rata-rata peminjaman tertinggi sekitar 461.")
st.write("2. Jam 18:00 (6:00 PM) menduduki peringkat kedua dengan rata-rata peminjaman sekitar 426.")
st.write("3. Jam 08:00 (8:00 AM) juga menjadi salah satu jam dengan peminjaman tinggi, rata-ratanya adalah sekitar 359.")
st.write("4. Jam 16:00 (4:00 PM) dan jam 19:00 (7:00 PM) juga memiliki rata-rata peminjaman yang signifikan.")
st.write("Peminjaman Terendah (Top 5 Jam):")
st.write("1. Jam 04:00 (4:00 AM) adalah jam dengan rata-rata peminjaman terendah, hanya sekitar 6.")
st.write("2. Jam 03:00 (3:00 AM), jam 05:00 (5:00 AM), jam 02:00 (2:00 AM), dan jam 01:00 (1:00 AM) juga termasuk jam-jam dengan peminjaman terendah.")
st.write("Jadi, berdasarkan data ini, kita dapat menyimpulkan bahwa jam-jam puncak peminjaman terjadi pada sore hingga malam hari (17:00 - 19:00) dengan jam 17:00 (5:00 PM) menjadi yang tertinggi. Sebaliknya, jam-jam dengan peminjaman terendah terjadi pada dini hari (01:00 - 05:00) dengan jam 04:00 (4:00 AM) menjadi yang terendah. Informasi ini dapat berguna untuk mengelola stok sepeda dan perencanaan operasional sistem penyewaan sepeda.")

