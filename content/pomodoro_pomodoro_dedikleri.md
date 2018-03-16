Title: Pomodoro nun Pratik Kullanımı
Date: 2018-03-14 17:14
Modified: 2018-03-17 00:42
Category: araçlar
Tags: pomodoro
Slug: pomodoro-crontab
Authors: orkung
Summary: Pomodoro en kolay nasıl hayata dahil edilir

Pomodoro disipliniyle çalışmak için ( 25 dk. çalış, 5 dk. mola ver ),
terminal'den çalışan bir app aradım, python/zsh/nodejs app'larını denedim,
hiçbirisi istediğim verimlilikte değildi, sonunda kendim hazırladım, son derece
de basit oldu, crontab'ı şöyle düzenledim;

```
*/30 * * * *      /usr/bin/notify-send "Work"
25 * * * *      /usr/bin/notify-send "Break"
55 * * * *      /usr/bin/notify-send "Break"
```

Her yarım saatte bir `Work`, saati her 25 ve 55 geçtiğinde ise `Break` gönderiyor.
böylece pomodoro döngüsü sağlanıyor.

Kısacası, eğer hızlıca yapılabilir geliyorsa, önce yapılmısına bakmak yerine,
kendin yaptığında daha verimli oluyormuş.
