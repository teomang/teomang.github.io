Title: Fstabtan Scsi Diski Başlatma
Date: 2018-08-28 18:28
Modified: 2018-08-28 18:28
Category: linux
Tags: multipahd, scsi
Slug: fstabtan-scsi-diski-baslatma
Authors: orkung
Summary: scsi disk'i fstab'tan baglamada hata alındığında

Multipath'le sunucuya gösterdiğimiz scsi disk'leri, centos 7 sunucuda fstab'dan mount ederken [link'teki](https://access.redhat.com/solutions/2042843) hatayı verdi; fstab'ta disk'lerin options'ına `_netdev` yazarak sorun çözüldü.

