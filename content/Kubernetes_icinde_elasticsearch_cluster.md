Title: Kubernetes icinde elasticsearch cluster
Date: 2019-01-31 14:34
Modified: 2019-01-31 14:34
Category: kisisel
Tags: 
Slug: K8s ile elasticsearch cluster
Authors: orkung
Summary: Kubernetes içinde elasticsearch cluster yapılandırma

K8s ortami olarak GKE kullaniyorum, Elasticsearch surumu oss-6.4.2
Elastic node'lari icin tanimlar;

All nodes know about all the other nodes in the cluster and can forward client
requests to the appropriate node. Besides that, each node serves one or more
purpose:

* `Master-eligible node`: A node that has `node.master set to true (default)`,
  which makes it eligible to be elected as the master node, which controls the
  cluster.
* `Data node`: A node that has `node.data set to true (default)`. Data nodes hold
  data and perform data related operations such as CRUD, search, and
  aggregations. 
*  Ingest node A node that has `node.ingest set to true (default)`. Ingest nodes
   are able to apply an ingest pipeline to a document in order to transform
   and enrich the document before indexing. With a heavy ingest load, it makes
   sense to use dedicated ingest nodes and to mark the master and data nodes as
   `node.ingest: false`
*  Tribe node A tribe node, configured via the `tribe.*` settings, is a special
   type of coordinating only node that can connect to multiple clusters and
   perform search and other operations across all connected clusters. 

Client only nodes are used as load balancers for indexing and searching.
if you set `node.client: true` it implicitly sets `node.master` and `node.data` to false.

# https://discuss.elastic.co/t/node-types-in-an-elasticsearch-cluster/25488/12


