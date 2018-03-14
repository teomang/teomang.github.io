Title: Linux Swap Alanı Yönetimi
Date: 2018-03-14 17:10
Modified: 2018-03-14 17:10
Category: linux
Tags: swap
Slug: linux swap
Authors: orkung
Summary: Swap alanı kullanımı

### Swap alanı ne işe yarar, gerekli mi?
Linux fiziksel RAM'i page adındaki yığınlara bölerek kullanır. Swap işlemi, bu
page'lerin diske kopyalanması ve page'lerin boşaltılması işlemine denir. 

### Swap işlemi 2 sebepten ötürü gereklidir
- Sistem fiziksel ram miktarından fazlasına ihtiyaç duyduğunda, kernel RAM'deki
  az kullanılan page'leri swap alanına yazar ve ihtiyaç olan hafızayı
  uygulamaya tahsis eder.

- Uygulamalar ayağa kalkarken yüksek miktarda page'e ihtiyaç duyar, ancak bu
  alanlara sonrasında ihtiyaç duymaz. Sistem bunları swap'a atar.

### Swap Türleri

#### Disk Swap
- Disk bölümü (Partition)

```bash
# Fdisk ile
fdisk /dev/hdb
Command: a
Partition number (1-4): 1
#And I make the second partition of type swap:
Command: t
Partition number (1-4): 2
Hex code: 82
#Changed system type of partition 2 to 82 (Linux swap)      
Command: p
```
- Dosya

```bash
fallocate -l 1G /mnt/1GB.swap
dd if=/dev/zero of=/mnt/1GB.swap bs=1024 count=1048576
mkswap /mnt/1GB.swap
swapon /mnt/1GB.swap
vi /etc/fstab 
/mnt/1GB.swap  none  swap  sw 0  0
# Check that the swap file was created.
swapon -s
```

#### Ram swap
- zRam: Cpu cache'inde kullanilmayan alan buyukse tercih edilebilir. 
Kaynak: https://wiki.voidlinux.eu/Zram
