Title: Pelican'la blog'luyorum
Date: 2018-02-23 10:06
Modified: 2018-03-17 00:40
Category: misc
Tags: misc
Slug: ilk-yazi
Authors: orkung
Summary: kısaca neden pelican

Uzun zamandır blog yazısı yazmak isteyip yazmamamın faturasını jekyll'e kestim,
her ne kadar kendisi çok iyi bir blog framework'u olsa da, yeni aldığım
makinaya ruby, gems, rvm, bundle kurmak ve bilumum konfigürasyonuyla
uğraşmaktansa python'a 5 tane bileşen kurarak daha rahat blog yazacağıma kanaat getirdim. Her defasında
gem'lerde yaşadığım çakışmalar, kramdown'u unutup tekrar dokümana bakmalar
artık geride kaldı. 

Pelican için gerekli pip paketleri;

* markdown 
* pelican
* ghp-import
* disqus-python {mecburi değil, [disqus yorum uygulamasını](https://disqus.com) ekleyebilmek için}

kurulum için [bu yazıdan](https://rsip22.github.io/blog/create-a-blog-with-pelican-and-github-pages.html) faydalandım.

Eklenti ve temalar icin;
* https://github.com/getpelican/pelican-plugins.git
* https://github.com/gunchu/nikhil-theme.git

Neden blog tutuyorum sorusunu da biraz açmak istiyorum; insanoğlununun bir şeyi
anlamasını sağlayan iki önemli etmeni barındırıyor blog tutmak;

* Hayali de olsa, bir konuyu başka birisine anlatmak, onu daha iyi anlamayı sağlar.
* Bir blog yazısı, bir wiki yazısından, bir sözlük kaydından farklı olarak,
  konunun hikayeleştirilmesine gereksinir. Bir konuda ihtiyaç doğmuş ve
  yaratıcı bir şekilde onunla uğraşılmış, sonucunda bir deneyim oluşmuşsa bundan
  bir blog yazısı çıkar. Dolayısıyla diğer metinlerden farklı olarak, blog metni,
  tecrübe aktarımını sağlaması bakımından, değer üretir, bu sebepten biriciktir.
