Title: Osx'te bozulan virtualenv dizin yollarini duzeltme
Date: 2019-03-21 21:17
Category: it
Tags: osx,python
Slug: Osxte-bozulan-virtualenv-dizin-yollarini-duzeltme
Authors: orkung
Summary: virtualenv'deki projeye erişilemediğinde...

Nicedir günlüğe yazı eklemedim, bir bakayım diye virtualenv içindeki pelican
projesine girmek istediğimde buna benzer bir karşılaştım.

```
dyld: Library not loaded: @executable_path/../.Python
  Referenced from: /Users/[user]/.virtualenvs/pelican/bin/python
  Reason: image not found
Trace/BPT trap: 5
```

önce google'ladım tabi, bir sürü şey çıktı karşıma, bir kısmını denedim,
başarılı olamadım, sonra kendi kendime, şu yolu izleyerek çözdüm.

Problem, virtualenv'i oluştururken kullandığım python sürümünü
kaldırmam/unlink yapmamdan kaynaklanmış, bunu şöyle anladım;

```
ls -l ~/.virtualenvs/pelican/lib/python3.7
stat.py -> /usr/local/Cellar/python/3.7.1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/stat.py
```

sistemimde `/usr/local/Cellar/python/3.7.1/` yoktu. En kolay çözüm geri
getirmek olur deyip google'ladım ve sonucunda bu komutları çalıştırınca
düzeldi

```
brew unlink python
git config http.postBuffer 524288000
brew install https://raw.githubusercontent.com/Homebrew/homebrew-core/db004f83243963caf8be2ebdb4d0e660d7f7cb4e/Formula/python.rb
```

