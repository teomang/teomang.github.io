Title: Docker compose isimlendirme
Date: 2018-09-13 15:34
Modified: 2018-09-13 21:20
Category: linux
Tags: docker, docker-compose
Slug: Docker-compose-isimlendirme
Authors: orkung
Summary: compose'da konteyner ve servis isimlendirme

* compose `links`'te `service` parametresini kabul ediyor. `container_name`
  parametresine hata veriyor.
* ps ciktisinda container_name'i donduruyor.

asagidaki compose file ile test ettim;

```yaml
version: '3'
services:

  service-1:
    container_name: konteyner-1
    image: busybox
    command: tail -f /etc/hosts

  service-2:
    container_name: konteyner-2
    image: busybox
    command: tail -f /etc/hosts
    links:
      - service-1:xyz
```
