# comments.py

import sqlite3
import streamlit as st

def show_comments():
    # Veritabanı bağlantısı
    conn = sqlite3.connect('test3.db')
    cursor = conn.cursor()

    # Yorumları göster
    st.header("Yorumlar")
    comments = cursor.execute("SELECT * FROM comments").fetchall()

    for comment in comments:
        st.write(f"**{comment[1]}** diyor: {comment[2]}")

    # Veritabanı bağlantısını kapat
    conn.close()




# app.py

import streamlit as st
from comments import show_comments

# Ana uygulama
def main():
    st.title("Streamlit ile Veritabanına Bağlanma")

    # Yeni yorumları ekleme bölümü (daha önceki örneklerde olduğu gibi)
    # ...

    # Yorumları gösterme bölümü
    show_comments()

# Uygulamayı başlat
if __name__ == "__main__":
    main()
