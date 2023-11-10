# comments.py

import sqlite3
import streamlit as st

def show_comments():
    # Veritabanı bağlantısı
    conn = sqlite3.connect('test3.db')
    cursor = conn.cursor()

    # Yorumları göster
    st.header("Yorumlar")
    comments = cursor.execute("SELECT * FROM user_table").fetchall()

    for comment in comments:
        st.write(f"**{comment[1]}** diyor: {comment[2]}")

    # Veritabanı bağlantısını kapat
    conn.close()
