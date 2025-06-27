
# Repository Evaluation

- Python files present: Yes (10/10)
- readme.md present: Yes (10/10)
- researchs folder with at least 2 .md files: Yes (20/20)
- researchs folder with at least 1 .pdf file: Yes (10/10)
- requirements.txt present: Yes (10/10)
- Python code quality and logic: 0/40

## Code Review (in Turkish)
Detaylı Kod Değerlendirme Raporu:

OKUNABILIRLIK (13/15 puan):
+ Fonksiyon isimleri açıklayıcı ve anlaşılır
+ Ana menü ve alt menüler iyi organize edilmiş
+ Temel kullanıcı yönergeleri mevcut
- Fonksiyonların başında docstring eksik
- Bazı karmaşık işlemlerde (özellikle şifreleme algoritmaları) açıklayıcı yorumlar eksik
+ Değişken isimlendirmeleri tutarlı ve anlamlı

YAPI (8/10 puan):
+ Her şifreleme yöntemi için ayrı fonksiyonlar oluşturulmuş
+ Modüler yapı kullanılmış
+ Ana menü ve alt menüler mantıklı bir hiyerarşide
- Bazı fonksiyonlar çok uzun ve tek sorumluluğu aşıyor
- Hata yönetimi için ayrı bir modül/sınıf kullanılmamış

MANTIK (14/15 puan):
+ Şifreleme algoritmaları doğru implementasyon
+ Güvenli kriptografi kütüphaneleri kullanılmış
+ Giriş kontrolü ve hata yönetimi mevcut
+ AES, RSA gibi modern kriptografi yöntemleri uygun şekilde kullanılmış
- RSA anahtar çiftleri program kapatıldığında kayboluyor, kalıcı depolama eksik

TOPLAM PUAN: 35/40

GÜÇLÜ YÖNLER:
1. Kapsamlı bir kriptografi araç seti sunuyor
2. Kullanıcı dostu arayüz
3. Güvenli kriptografi kütüphanelerinin kullanımı
4. İyi hata yönetimi

GELİŞTİRİLEBİLECEK YÖNLER:
1. Fonksiyon dokümantasyonları eklenebilir
2. Kod tekrarını azaltmak için bazı ortak işlevler ayrılabilir
3. Anahtar yönetimi için kalıcı depolama eklenebilir
4. Sınıf tabanlı bir yapıya geçilebilir

Sonuç olarak, kod profesyonel ve işlevsel bir kriptografi araç seti sunuyor. Küçük iyileştirmelerle daha da geliştirilebilir.

Total Score: 60/100
