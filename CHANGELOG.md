## 2.0.0 - 2018-05-30
+ replaced `sched` backend with `threading.Timer`-like implementation, saving us from needing to respawn when a job's rate is changed.
+ jobs can now be permanently stopped by calling `job.terminate()`

### Backwards-Incompatible Changes
+ `job.stop()` no longer takes an optional `timeout` argument

## 1.0.1 - 2018-05-24
+ Corrected an assumption about the number of events that could be queued at once.

## 1.0.0 - 2018-05-22
+ Initial release
