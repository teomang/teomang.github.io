Title: San Disklerin Centos7'ye Tanıtılması
Date: 2018-08-29 13:52
Modified: 2018-08-29 13:52
Category: linux
Tags: server,san
Slug: san-disklerin-centos7ye-tanitilmasi
Authors: orkung
Summary: Centos7'ye San disk bağlama

* Sunucularda iscsi initiatorname'ler oluşturulup storage admin'e iletilir:
```
yum install iscsi-initiator-utils
cat /etc/iscsi/initiatorname.iscsi
```

* Storage admin SAN'e hangi ip'lerden erisilecegini iletir, ip'ler ilgili
  interface'lere eklenir. İscsi initiator target ip’ler ping'lendiğinde `no
  route to host` alınıyorsa interface/ip adresi eşleşmesi değiştirilir.
```
TYPE=Ethernet
PROXY_METHOD=none
BOOTPROTO=static
DEFROUTE=no
NAME=<>
UUID=<>
DEVICE=<>
ONBOOT=yes
IPADDR=<>
NETMASK=255.255.255.0
USERCTL=no
ZONE=public
```

* Iscsi initiator target ip’leri discover edilir. Dönen targetname'ler eklenir:
```
iscsiadm -m discovery -t sendtargets --portal <IP>
iscsiadm --mode node --targetname <name> --portal <ip> \
-o update -n node.startup -v automatic
```

* Multipath ile birden çokmuş gibi görünen disk ortamı işletim sistemine tek
  disk olarak gösterilir.
```
yum -y install device-mapper-multipath
syst/emctl enable multipathd
cat /etc/multipath/wwids
cp /usr/share/doc/device-mapper-multipath-0.4.9/multipath.conf /etc/multipath.conf 
vi  /etc/multipath.conf
defaults {
    user_friendly_names yes
    find_multipaths yes
}
blacklist {
    devnode "^sd[abc]"
}
multipaths {
        multipath {
                uid 0
                gid 0
                wwid ""
                mode 0600
        }
        multipath {
                uid 0
                gid 0
                wwid ""
                mode 0600
        }
}
systemctl start multipathd
```

* Firewall kurallari eklenir
```
firewall-cmd --permanent --add-port=3260/tcp
firewall-cmd --permanent --add-service iscsi-target
firewall-cmd --reload
```

* Disk'ler formatlanir, mount edilir, fstab guncellenir.
```
mkfs.xfs -f /dev/mapper/mpatha
mkfs.xfs -f /dev/mapper/mpathb
mount /dev/mapper/mpatha <dizin>
mount /dev/mapper/mpathb <dizin>
/dev/mapper/mpathb       <dizin> xfs     _netdev 0 0
```
