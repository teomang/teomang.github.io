Title: Kubernetes Persistence Volume Claimde Hata
Date: 2019-01-31 15:17
Modified: 2019-03-25 16:35
Category: it
Tags: k8s,pvc
Slug: K8ste-persistence-volume-claim-olustururken-hata 
Authors: orkung
Summary: Gluster endpoint'ine mount etme

kubectl create ile pvc resource'u yarattığımda;
```
 MountVolume.NewMounter initialization failed for volume "" :
endpoints "" not found
```

Başka bir tane daha pvc resource'unu recreate etmeyi deneyip aynı hatayı
aldığımı görünce problemin glusterfs'ten kaynaklandığını düşündüm. [Redhat'ın
dokümanına](https://docs.openshift.com/container-platform/3.9/install_config/storage_examples/gluster_example.html) bakmaya başladım. 
adım adım giderken, endpoints'in olmadığını farkettim.
        
```
kubectl get endpoints --all-namespaces
```

daha önce oluşturulmuş  glusterfs-endpoints.yaml dosyasından endpoint'i
yarattım. Problem çözüldü.
