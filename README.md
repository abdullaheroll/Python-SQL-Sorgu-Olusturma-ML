# Python Makine Öğrenimi ile SQL Sorgu 

## Giriş
Bu rapor, Python programlama dilini kullanarak metin verilerini işleme, doğal dil işleme (NLP) tekniklerini uygulama ve makine öğrenimi yöntemleri ile veri analizi yapma sürecini içeren "Python Makine Öğrenimi ile SQL Sorgu Oluşturma" projesinin ayrıntılı bir incelemesini sunmaktadır.

## Amaç
Bu projenin amacı, kullanıcı tarafından girilen metin tabanlı veriyi alarak, bu metni veri kümesindeki metinlere benzerlik temelinde analiz ederek en uygun SQL sorgusunu oluşturmayı amaçlamaktadır.

## Kullanılan Teknikler ve Kütüphaneler
1) Veri Okuma ve İşleme: Veri kümesi, pandas kütüphanesi kullanılarak okunmuş ve işlenmiştir.
2) Metin Temizleme: Metin verileri düzenlenmiş ve gereksiz karakterler temizlenmiştir.
3) TF-IDF Dönüştürme: Metin verileri TF-IDF vektörlerine dönüştürülerek sayısal temsiller elde edilmiştir.
4) Cosine Benzerliği: TF-IDF vektörlerinin cosine benzerliği kullanılarak metinler arasındaki benzerlik ölçülmüş ve en uygun sorgu tespit edilmiştir.

## Adımlar
1) Veri kümesi okunarak giriş ve çıkış verileri elde edilmiştir.
2) TF-IDF vektörleri oluşturularak metinler sayısal temsillere dönüştürülmüştür.
3) Cosine benzerliği kullanılarak metinler arasındaki benzerlik ölçülmüştür.
4) Kullanıcıdan alınan metin, TF-IDF vektörleri ile benzerlik hesaplanarak en uygun sorgu tespit edilmiştir.

## Sonuçlar
Projede kullanılan yöntemler ve kodlar, metin tabanlı girdilerin veri kümesindeki metinlere ne kadar benzediğini ölçerek en yakın SQL sorgusunu bulmada etkili bir yaklaşım sağladı. Ancak, benzerlik temelli yöntemlerin doğrulukları, veri kümesinin büyüklüğüne ve kalitesine bağlı olarak değişebilir.

## Sonuç ve Öneriler
Bu projede, metin tabanlı verileri işleme, TF-IDF dönüşümü ve cosine benzerliği kullanarak SQL sorgusu oluşturma amacıyla başarılı bir model geliştirildi. Ancak, daha geniş ve çeşitli bir veri kümesi ile test edilerek ve farklı NLP yöntemleri ile karşılaştırılarak modelin performansının daha ayrıntılı bir şekilde değerlendirilmesi önerilir.

## İlişkili Projeler

İşte bazı ilgili projeler

[Ml.Net İle Duygu Analizi](https://github.com/abdullaheroll/Ml.Net-TR-Duygu-Analizi)
[Ml.Net İle Spam Analizi](https://github.com/abdullaheroll/Ml.Net-TR-Spam-Analizi)

## Veri setinin alındığı yer:

- [Kagle](https://www.kaggle.com/datasets/mrtbeyz/trke-sosyal-medya-paylam-veri-seti)

  ## Ekran Görüntüleri

![Uygulama Ekran Görüntüsü](https://raw.githubusercontent.com/abdullaheroll/Sorgu-Olusturma-ML/main/program.png)
