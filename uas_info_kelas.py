import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from streamlit_option_menu import option_menu

@st.cache_data
#Load Data CSV
def load_data(url) :
    df = pd.read_csv(url)
    return df

def Data_Mining(df_data_Aotizhongxin, df_data_Changping, df_data_Dingling):
    #mengambil data dari kota Aotizhongxin
    st.header("Data Kota Aotizhongxin")
    st.write(df_data_Aotizhongxin.head())
    #mengambil data dari kota Changping
    st.header("Data Kota Changping")
    st.write(df_data_Changping.head())
    #mengambil data dari kota Dingling
    st.header("Data Kota Dingling")
    st.write(df_data_Dingling.head())

    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    #Cleaning data Aotizhongxin
    st.header("Cleaning Data")
    st.subheader("Nilai yang Hilang")
    st.write("Kota Aotizhongxin")
    missing_values = df_data_Aotizhongxin.isnull().sum()
    st.write(missing_values)

    #Cleaning data Changping
    st.write("Kota Changping")
    missing_values = df_data_Changping.isnull().sum()
    st.write(missing_values)

    #Cleaning data Dingling
    st.write("Kota Dingling")
    missing_values = df_data_Dingling.isnull().sum()
    st.write(missing_values)

    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    # Menampilkan data yang dihapus karena duplikasi
    st.header("Data yang Dihapus karena Duplikasi")
    duplicates_data=df_data_Aotizhongxin[df_data_Aotizhongxin.duplicated()]
    st.write(duplicates_data)

    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    # Menampilkan data setelah menghapus duplikasi
    st.header("Setelah Menghapus Duplikasi Data Kota Aotizhongxin")
    df_data_Aotizhongxin.drop_duplicates(inplace=True)
    st.write(df_data_Aotizhongxin.head())

    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    # Eksplorasi Data
    st.header("Eksplorasi Data")
    st.subheader("Air Quality Kategori Hari di Kota Aotizhongxin")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=df_data_Aotizhongxin, x='day', ax=ax)
    ax.tick_params(axis='x', rotation=90)
    st.pyplot(fig)

    # Analisis Penjelasan
    st.header("Analisis Penjelasan")
    st.subheader("Statistik Temperature")
    st.write(df_data_Aotizhongxin['TEMP'].describe())
    with st.expander("Penjelasan Statistik :") :
        st.write("Untuk temperature menunjukkan terdapat 35.044 hitungan dalam dataset. Rata-rata temperature adalah sekitar 13,5°C dengan standar sebesar 11,3°C, menunjukkan variasi dalam temperature. Temperature minimum adalah -16,8°C, sementara temperature maksimumnya mencapai 40,5°C. Kuartil pertama (25 %) memiliki temperature di bawah 3,1°C, sedangkan kuartil ketiga (75%) memiliki temperature di bawah 23,3°C. Median temperature, yang membagi dataset menjadi dua bagian yang sama besar, adalah 14,5°C.")


def Pertanyaan_Bisnis(df_data_Aotizhongxin, df_data_Changping, df_data_Dingling) :
    # Data tahun 2015
    data_2015 = df_data_Aotizhongxin[df_data_Aotizhongxin['year'] == 2015]

    # Pertanyaan 1
    st.header("Pertanyaan 1 : Berapa rata-rata suhu dari tahun ke tahun ?")

    # Mengatur ukuran dan gaya plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x="year", y="TEMP",data=df_data_Aotizhongxin,color='tomato', ax=ax)
    # Menambahkan judul dan label sumbu
    ax.set_title('Perubahan Rata Rata Suhu Dari Tahun Ke Tahun')
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Suhu Terendah (°C)')
    # Menampilkan grafik
    st.pyplot(fig)

    with st.expander("Informasi Suhu Tertinggi dan Terendah"):
        max_temp = df_data_Aotizhongxin['TEMP'].max()
        min_temp = df_data_Aotizhongxin['TEMP'].min()
        st.markdown(f"Suhu tertinggi pada tahun 2013 : **{max_temp} °C**")
        st.markdown(f"Suhu terendah pada tahun 2017 : **{min_temp} °C**")

    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    # Pertanyaan 2
    st.header("Pertanyaan 2 : Bagaimana rata-rata suhu terendah per Bulan ?")

    # Mengatur ukuran dan gaya plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x="month", y="TEMP",data=df_data_Aotizhongxin, color='red', ax=ax)
    # Menambahkan judul dan label sumbu
    ax.set_title('Perubahan Suhu setiap bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Suhu (°C)')
    # Menampilkan grafik
    st.pyplot(fig)

    with st.expander("Rata-Rata Suhu Terendah per Bulan"):
        mean_temp = df_data_Aotizhongxin.groupby('month')['TEMP'].mean().round(1)
        for month, temp in mean_temp.items():
            st.markdown(f"**Bulan {month} :** {temp} °C")

    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    # Pertanyaan 3
    st.header("Pertanyaan 3 : Bagaimana intensitas hujan tertinggi dan terendah dari tahun ke tahun ?")

    # Mengatur ukuran dan gaya plot
    fig, ax = plt.subplots(figsize=(10, 6))
    # Menggambar grafik batang intensitas hujan tertinggi dari tahun ke tahun
    sns.barplot(x="year", y="RAIN", data=df_data_Aotizhongxin.groupby('year')['RAIN'].max().reset_index(), color='yellowgreen', ax=ax)
    # Menambahkan judul dan label sumbu
    ax.set_title('Intensitas Hujan Tertinggi per-Tahun Stasiun Aotizhongxin')
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Intensitas Hujan Tertinggi (mm/hari)')
    # Menampilkan grid
    ax.grid(True)
    # Menampilkan grafik
    st.pyplot(fig)

    # Mengatur ukuran dan gaya plot
    fig, ax = plt.subplots(figsize=(10, 6))
    # Mengatur data intensitas hujan terendah per tahun
    sns.barplot(x="year", y="RAIN", data=df_data_Aotizhongxin, color='yellowgreen', ax=ax)
    # Menambahkan judul dan label sumbu
    ax.set_title('Intensitas Hujan Terendah per-Tahun Stasiun Aotizhongxin')
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Intensitas Hujan (mm/hari)')
    # Menampilkan grafik
    st.pyplot(fig)

    with st.expander("Informasi Intensitas Hujan Tertinggi dan Terendah"):
        max_rain = df_data_Aotizhongxin.groupby('year')['RAIN'].max()
        min_rain = df_data_Aotizhongxin.groupby('year')['RAIN'].min()
        st.markdown("Intensitas Hujan Tertinggi per Tahun :")
        for year, rain in max_rain.items():
            st.markdown(f"**Tahun {year}:** {rain} mm/hari")
        st.markdown("Intensitas Hujan Terendah per Tahun :")
        for year, rain in min_rain.items():
            st.markdown(f"**Tahun {year}:** {rain} mm/hari")


    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    # Pertanyaan 4
    st.header("Pertanyaan 4 : Bagaimana rata-rata Intensitas hujan Terendah per Bulan pada tahun 2015 di Stasiun Aotizhongxin ?")

    # Mengatur ukuran dan gaya plot
    fig, ax = plt.subplots(figsize=(10, 6))
    # Mengatur data intensitas hujan terendah per tahun
    sns.lineplot(x="month", y="RAIN", data=data_2015, marker='o', color='Green', ax=ax)
    # Menambahkan judul dan label sumbu
    ax.set_title('Intensitas Hujan terendah per bulan Stasiun Aotizhongxin pada tahun 2015')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Intensitas Hujan (mm/hari)')
    # Menampilkan grid
    ax.grid(True)
    # Menampilkan grafik
    st.pyplot(fig)

    with st.expander("Informasi Rata-rata Intensitas Hujan Terendah per Bulan Tahun 2015"):
        mean_rain_2015 = data_2015.groupby('month')['RAIN'].mean().round(1)
        for month, rain in mean_rain_2015.items():
            st.markdown(f"**Bulan {month}:** {rain} mm/hari")


    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    # Pertanyaan 5
    st.header("Pertanyaan 5 : Bagaimana rata-rata Tingkat NO2 per Tahun dan per Bulan ?")

    # Mengatur ukuran dan gaya plot
    fig, ax = plt.subplots(figsize=(10, 6))
    # Menggambar grafik bar
    sns.barplot(x="year", y="NO2", data=df_data_Aotizhongxin, ax=ax)
    # Menambahkan judul dan label sumbu
    ax.set_title("Perubahan Tingkat NO2 per Tahun Pada Stasiun Aotizhongxin")
    ax.set_xlabel("Tahun")
    ax.set_ylabel("Tingkat NO2")
    # Menampilkan grafik
    st.pyplot(fig)

    # Mengatur ukuran dan gaya plot
    fig, ax = plt.subplots(figsize=(10, 6))
    # Menggambar grafik bar
    sns.barplot(x="month", y="NO2", data=df_data_Aotizhongxin, ax=ax)
    # Menambahkan judul dan label sumbu
    ax.set_title("Perubahan Tingkat NO2 per Bulan Pada Stasiun Aotizhongxin")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Tingkat NO2")
    # Menampilkan grafik
    st.pyplot(fig)

    with st.expander("Informasi Rata-rata Tingkat NO2"):
        # Rata-rata tingkat NO2 per tahun
        mean_no2_yearly = df_data_Aotizhongxin.groupby('year')['NO2'].mean().round(1)
        st.markdown("### Rata-rata Tingkat NO2 per Tahun:")
        for year, no2 in mean_no2_yearly.items():
            st.markdown(f"**Tahun {year}:** {no2} ppb")
        # Rata-rata tingkat NO2 per bulan
        mean_no2_monthly = df_data_Aotizhongxin.groupby('month')['NO2'].mean().round(1)
        st.markdown("### Rata-rata Tingkat NO2 per Bulan:")
        for month, no2 in mean_no2_monthly.items():
            st.markdown(f"**Bulan {month}:** {no2} ppb")

    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    # Pertanyaan 6
    st.header("Pertanyaan 6 : Bagaimana rata-rata Perubahan Tingkat CO per Tahun Pada tiap Bulannya ?")

    # 2013
    data_2013 = df_data_Aotizhongxin[df_data_Aotizhongxin['year'] == 2013]
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x="month", y="CO", data=data_2013, marker='o', color='blue', ax=ax)
    plt.title('Tingkat CO Ditahun 2013')
    plt.xlabel('Bulan')
    plt.ylabel('Tingkat CO')
    plt.grid(True)
    st.pyplot(fig)

    # 2014
    data_2014 = df_data_Aotizhongxin[df_data_Aotizhongxin['year'] == 2014]
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x="month", y="CO", data=data_2014, marker='o', color='yellow', ax=ax)
    plt.title('Tingkat CO Ditahun 2014')
    plt.xlabel('Bulan')
    plt.ylabel('Tingkat CO')
    plt.grid(True)
    st.pyplot(fig)

    # 2015
    data_2015 = df_data_Aotizhongxin[df_data_Aotizhongxin['year'] == 2015]
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x="month", y="CO", data=data_2015, marker='o', color='green', ax=ax)
    plt.title('Tingkat CO Ditahun 2015')
    plt.xlabel('Bulan')
    plt.ylabel('Tingkat CO')
    plt.grid(True)
    st.pyplot(fig)

    # 2016
    data_2016 = df_data_Aotizhongxin[df_data_Aotizhongxin['year'] == 2016]
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x="month", y="CO", data=data_2016, marker='o', color='cyan', ax=ax)
    plt.title('Tingkat CO Ditahun 2016')
    plt.xlabel('Bulan')
    plt.ylabel('Tingkat CO')
    plt.grid(True)
    st.pyplot(fig)

    # 2017
    data_2017 = df_data_Aotizhongxin[df_data_Aotizhongxin['year'] == 2017]
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x="month", y="CO", data=data_2017, marker='o', color='cyan', ax=ax)
    plt.title('Tingkat CO Ditahun 2017')
    plt.xlabel('Bulan')
    plt.ylabel('Tingkat CO')
    plt.grid(True)
    st.pyplot(fig)

    with st.expander("Informasi Rata-rata Perubahan Tingkat CO per Tahun"):
        for year in range(2013, 2018):
            data_year = df_data_Aotizhongxin[df_data_Aotizhongxin['year'] == year]
            monthly_avg_CO = data_year.groupby('month')['CO'].mean().round(1)
            st.markdown(f"### Tahun {year} : ")
            for month, avg_CO in monthly_avg_CO.items():
                st.write(f"Bulan {month} : {avg_CO} ppm")


    st.write('<hr>', unsafe_allow_html=True) #hr Garis Pemisah

    with st.expander("Conclusion") :
        st.markdown("- Conclusion pertanyaan 1 : Suhu Tertinggi Terjadi di 2013 dan Terendah di 2017")
        st.markdown("- conclution pertanyaan 2 : Rata Rata Suhu Terendah Terjadi dibulan Januari")
        st.markdown("- conclution pertanyaan 3 : Intensitas Hujan Tertinggi per-Tahun Stasiun Aotizhongxin Terjadi di 2013")
        st.markdown("- conclution pertanyaan 4 : Intensitas Hujan Terendah per-Tahun Stasiun Aotizhongxin Terjadi di 2017")
        st.markdown("- conclution pertanyaan 5 : Perubahan Tingkat NO2 yang Signifikan Terjadi pada 2016-2017 dan Tertinggi pada Bulan 10 & 12")
        st.markdown("- conclution pertanyaan 6 : Peningkatan Tertinggi Terjadi di 2015 dan Penurun Terendah Terjadi di 2015")



#load Dataset
df_data_Aotizhongxin = load_data("https://raw.githubusercontent.com/JohnLemon10/AnalisisAirQuality/main/PRSA_Data_Aotizhongxin_20130301-20170228.csv")
df_data_Changping = load_data("https://raw.githubusercontent.com/JohnLemon10/AnalisisAirQuality/main/PRSA_Data_Changping_20130301-20170228.csv")
df_data_Dingling = load_data("https://raw.githubusercontent.com/JohnLemon10/AnalisisAirQuality/main/PRSA_Data_Dingling_20130301-20170228.csv")



# Side Bar
with st.sidebar :
    selected = option_menu('Menu',['About Us','Dashboard'],
    icons =["easel2", "graph-up"],
    menu_icon="cast",
    default_index=1)
    
if (selected == 'Dashboard') :
    st.header(f"Dashboard Analisis Air Quality")
    tab1,tab2 = st.tabs(["Data Mining", "Pertanyaan Bisnis"])
    with tab1 :
        Data_Mining(df_data_Aotizhongxin, df_data_Changping, df_data_Dingling)
    with tab2 :
        Pertanyaan_Bisnis(df_data_Aotizhongxin, df_data_Changping, df_data_Dingling)

elif (selected == 'About Us') :
    st.header("Kelompok info kelas")
    # Tampilkan anggota kelompok
    st.markdown(" **Anggota**:")
    st.markdown("  - 10122358 - Muhammad Irfan Dava Nugraha")
    st.markdown("  - 10122360 - Ghamir Diah Kharismasya")
    st.markdown("  - 10122370 - M Nata Jayndra Permana")
    st.markdown("  - 10122372 - Danendra Muzhaffar")
    st.markdown("  - 10122387 - Teguh Darmawansyah")