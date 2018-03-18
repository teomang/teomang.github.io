Title: Read-Only Bağlanan LVM Diskin Fsck ile Onarımı
Date: 2018-03-16 17:11
Modified: 2018-03-18 17:30
Category: linux
Tags: recovery, kurtarma
Slug: lvm-root-diskini-fsck-ile-kurtarma
Authors: orkung
Summary: Root diski read-only bağlıyken kurtarma

İşletim sistemi: CentOS 6.8

Elektrik kesintisi vb. beklenmedik olayların, sunucunun / disk bölümünde soruna
yol açarak, sadece okuma modunda (ro) diski bağladığı durumda ne yapılabileceğini
göstermeye çalışacağım.

Sunucuda dosya oluşturmayı denedim ve sorunu farkettim.

```bash
touch dosya
touch: cannot touch dosya: Read-only file system
```

ilk olarak rw olarak remount etmeyi denedim
```bash
mount -o remount,rw /
mount: cannot remount block device /dev/mapper/VolGroup-lv_root read-write, is write-protected
```
Belki düzelir umuduyla restart ettim. Fakat aşağıdaki hatalarla karşılaştım
```bash
/dev/mapper/VolGroup-lv_root contains a file system with errors, check forced.
/dev/mapper/VolGroup-lv_root Inodes that were part of a corrupted orphan linked list found.
/dev/mapper/VolGroup-lv_root: UNEXPECTED INCONSISTENCY; RUN fsck MANUALLY
```
/etc/fstab dosyasında / disk bölümü için fsck öntanımlı olarak açık durumda.
Fakat sistemin çalıştırdığı fsck'da -y flag'i kullanılmıyor, sistem 
ilk FIXED'tan sonra, disk'te halen hata mevcutsa process'i devam ettirmiyor.
Bu durumda fsck'yi aşağıdaki gibi manuel çalıştırdım.
```bash
vgchange --ignorelockingfailure -ay
lvscan --ignorelockingfailure
fsck -y /dev/mapper/VolGroup-lv_root
```
İşlem bitiminde sunucuyu reboot etmek gerekiyor, reboot sonrası disk yazma
izniyle (rw) olarak bağlandı
