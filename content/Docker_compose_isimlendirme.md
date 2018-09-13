Title: Docker compose isimlendirme
Date: 2018-09-13 15:34
Modified: 2018-09-13 15:24
Category: linux
Tags: docker, docker-compose
Slug: Docker-compose-isimlendirme
Authors: orkung
Summary: compose'da konteyner ve servis isimlendirme

asagidaki gibi bir compose file olusturdum;
compose link'lemede servis parametresini kabul ediyor. container_name
kullanildiginda hata veriyor.

```yaml
version: '3'
services:

  server-1:
    container_name: konteyner-1
    image: busybox
    command: tail -f /etc/hosts

  server-2:
    container_name: konteyner-2
    image: busybox
    command: tail -f /etc/hosts
    links:
      - server-1:xyz
```

ps ciktisinda ise container_name ile donus yapiyor.
