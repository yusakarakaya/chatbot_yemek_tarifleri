#Tabanlı Yemek Tarifi Chatbotu

Bu proje, Retrieval-Augmented Generation (RAG) mimarisini kullanarak yaklaşık 3000 yemek tarifinden oluşan bir veri seti üzerinden kullanıcı sorularını yanıtlayan ve iki dev dil modelini (Google Gemini 2.5 Flash ve Meta Llama 3.3) karşılaştıran bir chatbot uygulamasıdır.

------------------------------------------------------------------------------------------------------------------------------------------

Öne Çıkan Özellikler
Çift Model Karşılaştırması: Gemini ve Llama modellerinin yanıtlarını aynı arayüzde yan yana görüntüleme.
Gelişmiş RAG Yapısı: ChromaDB ve HuggingFace Embeddings ile yüksek doğrulukta tarif getirme.
Niyet Sınıflandırma: Kullanıcı isteklerini analiz ederek doğru yanıt stratejisi belirleme.
Hızlı Arayüz: Streamlit ile optimize edilmiş kullanıcı deneyimi.

-------------------------------------------------------------------------------------------------------------------------------------------

Proje Yapısı
├── data/
│   └── yemek_tarifleri_tablosu.csv  # 3000+ Tarif İçeren Veri Seti
├── models/
│   ├── gpt_model.py                 # Llama 3.3 / Groq Entegrasyonu
│   └── gemini_model.py              # Gemini 2.5 Flash Entegrasyonu
├── app/
│   └── app.py                      # Streamlit Arayüzü ve RAG Akışı
├── .env                             # API Anahtarları (Gizli)
└── requirements.txt                 # Gerekli Kütüphaneler

-------------------------------------------------------------------------------------------------------------------------------------------

Çalışma Mantığı
Veri Hazırlığı: init_rag() fonksiyonu CSV dosyasını okur ve HuggingFace ile metinleri vektörlere dönüştürerek ChromaDB'ye kaydeder.
Retriever: Kullanıcı bir soru sorduğunda, veritabanından en alakalı tarifler çekilir.
Prompt Engineering: Çekilen tarifler, "Uzman Şef" sistem talimatlarıyla birleştirilerek modellere gönderilir.
Yanıt Üretimi: Modeller, sunulan bağlama sadık kalarak tutarlı ve gerçekçi tarifler üretir.

-------------------------------------------------------------------------------------------------------------------------------------------

Model Performansı ve Karşılaştırma
Proje kapsamında 30 soruluk özel bir test seti ile otomatik değerlendirme yapılmıştır.

Model               Precision   Recall   F1 Score  
Gemini 2.5 Flash    0.70        0.80     0.73
Llama 3.3 (Groq)    0.70        0.80     0.73

Hazırlanan tabloya göre, her iki model de (Gemini ve Llama) test verisindeki 5 farklı niyet üzerinde %80 doğruluk oranıyla birbirine tamamen özdeş bir performans sergilemiştir. Modeller standart kullanıcı taleplerini %100 doğrulukla ayrıştırarak temel sohbet yeteneklerinde kusursuz olduklarını kanıtlamışlardır. Ancak, her iki modelin de "reddetme" (rejection) niyetini tespit edemeyerek (0.00 puan), yemek dışı soruları yanlışlıkla "tarif isteği" olarak sınıflandırması, genel başarı skorlarının %70-73 bandında kalmasına neden olmuştur. Sonuç olarak; modeller genel kullanımda oldukça başarılı olsa da, kapsam dışı soruları ayırt etmekte sıkıntılar yaşamaktadır.

-------------------------------------------------------------------------------------------------------------------------------------------

Kurulum
1. Depoyu klonlayın
2. Gerekli kütüphaneleri yükleyin
3. .env dosyasını oluşturun ve API anahtarlarınızı ekleyin
4. Uygulamayı çalıştırın:
