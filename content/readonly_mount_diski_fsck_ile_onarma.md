Title: Read-Only Bağlanan LVM Diskin Fsck ile Onarımı
Date: 2018-03-16 17:11
Modified: 2018-03-16 17:11
Category: linux
Tags: recovery, kurtarma
Slug: lvm-root-diskini-fsck-ile-kurtarma
Authors: orkung
Summary: Root diski read-only bağlıyken kurtarma

İşletim sistemi: CentOS 6.8

Elektrik kesintisi vb. beklenmedik olayların, sunucunun / diskinde soruna yol
açarak yazma iznine engel olduğu aşağıdaki durumda ne yapılabileceğini
göstermeye çalışacağım.
Sunucuda dosya oluşturmayı denedim böylece sorun olduğunu farkettim.

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
fstab'ta / partition'u için fsck default aktif. Fakat burada -y flag'i
kullanılmıyor, sistem fsck'yı deniyor, ilk FİXED'tan sonra, disk'te halen 
hata mevcutsa process'i durduruyor. Bu durumda fsck'yi aşağıdaki gibi 
manuel çalıştırdım.
```bash
vgchange --ignorelockingfailure -ay
lvscan --ignorelockingfailure
fsck -y /dev/mapper/VolGroup-lv_root
```
İşlem bitiminde sunucuyu reboot etmek gerekiyor, reboot sonrası disk rw
olarak bağlandı
