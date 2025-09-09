## LSTM Metin Tamamlama Modeli
Bu proje, LSTM (Long Short-Term Memory) tabanlı bir derin öğrenme modeli kullanarak, verilen bir başlangıç cümlesini otomatik olarak tamamlar. Model, eğitim verisinden cümle yapısını ve kelime ilişkilerini öğrenerek bir sonraki kelimeyi tahmin eder.

## Kullanılan Teknolojiler
Python 3.x
TensorFlow / Keras: Derin öğrenme modeli oluşturmak için kullanılır.
NumPy: Sayısal işlemler ve veri manipülasyonu için kullanılır.
Pandas: Veri setini okuma ve işleme için kullanılır.

## Kurulum
Projeyi kendi bilgisayarınızda çalıştırmak için gerekli kütüphaneleri requirements.txt dosyasından yükleyebilirsiniz.
Bash
pip install -r requirements.txt

## Veri Seti
Model, Text_LSTM.csv dosyasındaki metin verileri üzerinde eğitilir.
Text_LSTM.csv dosyası, tek bir Text sütunu içermelidir.
Her satırda, modelin öğrenmesi için bir cümle veya metin parçası bulunmalıdır.

## Nasıl Çalışır?
Modelin çalışma süreci şu adımlardan oluşur:

Veri Ön İşleme: CSV dosyasındaki metinler okunur, token'lara ayrılır ve sayılara dönüştürülür.

Sıralama ve Dolgu (Padding): Metinlerin uzunlukları eşitlenir ve model için uygun bir formata getirilir.

Model Eğitimi: Oluşturulan LSTM modeli, kelimeler arasındaki ilişkileri öğrenmek için eğitim verisi üzerinde çalıştırılır.

Tahmin: Kullanıcı tarafından girilen bir cümle, eğitilmiş model tarafından bir sonraki kelimeyi tahmin etmek için kullanılır.

## Kullanım Örneği
Modeli eğittikten sonra, LSTM.py dosyasındaki predict_next_Word fonksiyonunu kullanarak metin tamamlama yapabilirsiniz.
Python
from LSTM import predict_next_Word
# Başlangıç metnini ve kaç kelime tamamlanacağını belirtin
send_text = "Sabah yürüyüşünde"
print(predict_next_Word(send_text, 7))
# Daha Sonrasında ise modeli eğitip Sonucu Görün
Sonuç : Sabah Yürüyüşünde biraz geç kaldım çünkü otobüs çok kalabalıktı.

## Projeyi daha da geliştirmek için aşağıdaki adımlar atılabilir:
-Daha Kapsamlı Veri Seti: Modeli daha büyük ve çeşitli bir veri setiyle eğitmek, tahmin yeteneğini artırabilir.
-Daha Gelişmiş Modeller: Transformer gibi daha modern dil modellerini denemek.
-Web Arayüzü: Modelin bir web arayüzü (örneğin, Flask veya Django ile) üzerinden kullanılmasını sağlamak.

## Katkıda Bulunma
Projeye katkıda bulunmak isterseniz, lütfen bir pull request gönderin veya bir issue açarak önerilerinizi paylaşın. Tüm katkılar memnuniyetle karşılanır.

## Lisans
Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakabilirsiniz.
