# Docker for Mac で発生するシステム時刻のズレと、それを解消する方法

```console
$ docker run --rm --privileged alpine hwclock -s
```

Docker for Mac で Docker ホストの内部時計がずれていたときに治すコマンドです。

なぜか自分の Mac の Docker ホストの内部時計だけが 15 分ずれていたときに使いました。

`hwclock -s` は本来、システム時刻をハードウェア時刻に合わせるためのコマンドです。

# どこから情報を得たか

https://github.com/docker/for-mac/issues/2076
https://github.com/docker/for-mac/issues/1260

このあたりの issue に載っていました。
報告によっては 1 日につき 30 秒くらいずつずれている模様です。
