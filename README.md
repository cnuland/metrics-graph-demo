# metrics-graph-demo


### cpu-usage
pod:container_cpu_usage:sum{namespace="metrics-blog", pod="metrics-demo-base-64868ddd-xwhzt", prometheus="openshift-monitoring/k8s"}

### average
pod:container_cpu_usage:sum:avg_over_time_1week{namespace="metrics-blog", pod="metrics-demo-base-64868ddd-xwhzt", prometheus="openshift-monitoring/k8s"}

### zscore
```
(
pod:container_cpu_usage:sum{namespace="metrics-blog", pod="metrics-demo-base-64868ddd-xwhzt", prometheus="openshift-monitoring/k8s"} -
pod:container_cpu_usage:sum:avg_over_time_1week{namespace="metrics-blog", pod="metrics-demo-base-64868ddd-xwhzt", prometheus="openshift-monitoring/k8s"}
) / pod:container_cpu_usage:sum:stddev_over_time_1week{namespace="metrics-blog", pod="metrics-demo-base-64868ddd-xwhzt", prometheus="openshift-monitoring/k8s"}
```
