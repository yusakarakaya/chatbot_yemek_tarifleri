# RAG Tabanlı Yemek Tarifi Chatbotu

Bu proje, Gemini 2.5 ve Llama 3.3 modellerini niyet sınıflandırma ve 
yemek tarifi verme başarısı üzerinden karşılaştırır. Bu chatbotla yaklaşık
3000 yemek tarifi olan veri setiyle sorgulama yapar.

1
.env dosyasının içine Gemini ve Llama aldığım API'leri yerleştirdim. 

retriever ile vektör veritabanından (ChromaDB) en alakalı tarifleri bulup getiren araç.


ChatGoogleGenerativeAI ile Google'ın Gemini modelini projeye bağlar. temperature=0.3 ayarı, modelin çok uydurma yapmadan tutarlı ve gerçekçi cevaplar vermesini sağlar.

2
gemini_model.py dosyası içinde gemini sorgulama işlemini gösterdim.

3
gpt_model.py dosyası içinde gpt model sorgulama işlemlerini gösterdim.

Bu fonksiyon, Meta'nın Llama 3.3 modelinin Groq altyapısı üzerinden yüksek performansla çalışmasını sağlayan işlem hattıdır. 

Süreç, retriever aracılığıyla veritabanından soruyla en alakalı yemek tariflerinin çekilip düzenlenmesiyle başlar; bu veriler kullanıcının sorusuyla birlikte "uzman şef" talimatlarına (prompt) enjekte edilir.

Llama modeli, kendisine sunulan bu özel bağlamı analiz ederek veritabanındaki gerçek bilgilere sadık, akıcı ve şef üslubuna uygun bir yanıt üretir; son aşamada ise bu yanıt temiz bir metin olarak kullanıcıya sunulur.

4
app.py dosyası ilk olarak init_rag() fonksiyonuyla yemek_tarifleri_tablosu.csv dosyasını okur. 

HuggingFace Embeddings ile yemek tariflerini bilgisayarın anlayacağı sayısal verilere dönüştürür.

ChromaDB ile bu sayısal verileri bir "vektör veritabanı"na kaydeder. Kullanıcı bir soru 
sorduğunda, veritabanından en alakalı 3 tarifi bulup getirir.

System Prompt ile kullanıcı istekleri doğrultusunda sorgu oluşturur.

Kod, modellerin iç mantığını gemini_model.py ve gpt_model.py dosyalarından çeker.

Streamlit arayüzü uygulamanın kullanıcıyla buluştuğu yerdir. Sayfayı ikiye bölerek Google Gemini ve Meta Llama'nın cevaplarını yan yana gösterir.


MODEL PERFORMANSI KARŞILAŞTIRMASI

Model               Precision     Recall     F1 Score
Gemini 2.5 Flash    0.70,         0.80       0.73
Llama 3.3 (Groq).   0.70          0.80       0.73

Hazırlanan tabloya göre, her iki model de (Gemini ve Llama) test verisindeki 5 farklı niyet üzerinde %80 doğruluk oranıyla birbirine tamamen özdeş bir performans sergilemiştir. Modeller standart kullanıcı taleplerini %100 doğrulukla ayrıştırarak temel sohbet yeteneklerinde kusursuz olduklarını kanıtlamışlardır. Ancak, her iki modelin de "reddetme" (rejection) niyetini tespit edemeyerek (0.00 puan), yemek dışı soruları yanlışlıkla "tarif isteği" olarak sınıflandırması, genel başarı skorlarının %70-73 bandında kalmasına neden olmuştur. Sonuç olarak; modeller genel kullanımda oldukça başarılı olsa da, kapsam dışı soruları ayırt etmekte sıkıntılar yaşamaktadır.

*** bu model karşılaştırması 30 soruluk bi veri seti hazırladım yazdığım otomatik test scripti ile her iki modele soru sorarak aldığım cevapları karşılkaştırdım.
