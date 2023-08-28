import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import re
from colorama import Fore, Back, Style, init
import os


# Renkleri başlat
init(autoreset=True)

# Ekran genişliği ve yüksekliği
screen_width = os.get_terminal_size().columns
screen_height = os.get_terminal_size().lines

# Metin
title = "Python Makine Öğrenimi Sql Sorgu Oluşturma"
author = "GitHub: @abdullaheroll"

# Metni renklendirme
colored_title = Fore.GREEN + title
colored_author = Fore.YELLOW + author

# Metni tam ortalamak için hesaplamalar
title_padding = (screen_width - len(title)) // 2
author_padding = (screen_width - len(author)) // 2

# Metni tam ortaya yerleştirme
centered_title = " " * title_padding + colored_title
centered_author = " " * author_padding + colored_author

# Başlık ve yazarı yazdırma
print("*" * screen_width)
print(centered_title)
print(centered_author)
print("*" * screen_width)


# Veri setini oku
data = pd.read_csv('turkish_query_answ_sql.csv')

# Veri kümesindeki input ve query alanları
inputs = data['Input']
queries = data['Query']

# TF-IDF vektörlerini oluştur
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(inputs)

# Modeli eğit
cosine_sim = cosine_similarity(tfidf_matrix)

# Modeli kaydet
joblib.dump(cosine_sim, 'cosine_similarity_model.pkl')

# Kaydedilen modeli yükle
cosine_sim = joblib.load('cosine_similarity_model.pkl')

# Kullanıcıdan metin tabanlı input al
user_input = input("Metin Giriniz: ")

# Veriyi temizleme fonksiyonu
def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    return text

    # Temizlenmiş kullanıcı girdisi
clean_user_input = preprocess_text(user_input)

# En benzer sorguyu bul
max_similarity = -1
best_query = None

# Kullanıcı girdisini vektöre dönüştür
user_input_vector = vectorizer.transform([clean_user_input])

for i, input_text in enumerate(inputs):
    similarity = cosine_similarity(user_input_vector, tfidf_matrix[i])[0][0]
    if similarity > max_similarity:
        max_similarity = similarity
        best_query = queries[i]

if max_similarity > 0:
    print("Eşleşen sorgu:", best_query)
else:
    print("Eşleşen sorgu bulunamadı.")
