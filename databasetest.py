import streamlit as st
import sqlite3

# Streamlit uygulamasını başlat
st.title("Şərh əlavə et")

# SQLite veritabanına bağlan
conn = sqlite3.connect('test3.db')
cursor = conn.cursor()

# Tabloyu oluştur
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_table (
        name TEXT,
        comment TEXT
    )
''')
conn.commit()

# Veritabanındaki verileri göster
user = cursor.execute("SELECT * FROM users").fetchall()

# Veritabanına yeni kullanıcı eklemek için giriş alanları

name = st.text_input("Ad:")
comment = st.text_area("Şərh:")

# Yeni kullanıcıyı eklemek için buton
if st.button("Daxil et"):
    cursor.execute("INSERT INTO users (name, comment) VALUES (?, ?)", (name, comment))
    conn.commit()
    st.success("Şərhiniz uğurla qeydə alındı!")

# Veritabanı bağlantısını kapat
conn.close()
