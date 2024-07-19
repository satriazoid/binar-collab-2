import sqlite3
import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

# Fungsi untuk membersihkan teks
def clean_text(text):
    cleaned_text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    return cleaned_text

# Mengambil data dari database
def fetch_data():
    conn = sqlite3.connect('data.db')
    df = pd.read_sql_query("SELECT * FROM texts", conn)
    conn.close()
    return df

# Membersihkan teks dalam data frame
def clean_texts(df):
    df['cleaned_text'] = df['text'].apply(clean_text)
    return df

# Menghitung frekuensi kata
def word_frequency(texts):
    words = ' '.join(texts).split()
    word_counts = Counter(words)
    return word_counts

# Membuat visualisasi frekuensi kata
def plot_word_frequency(word_counts):
    word_df = pd.DataFrame(word_counts.items(), columns=['word', 'frequency'])
    word_df = word_df.sort_values(by='frequency', ascending=False).head(20)  # ambil 20 kata teratas

    plt.figure(figsize=(12, 8))
    sns.barplot(data=word_df, x='frequency', y='word')
    plt.title('Top 20 Words by Frequency')
    plt.xlabel('Frequency')
    plt.ylabel('Word')
    plt.show()

# Langkah-langkah analisis
df = fetch_data()
df = clean_texts(df)
word_counts = word_frequency(df['cleaned_text'])
plot_word_frequency(word_counts)
