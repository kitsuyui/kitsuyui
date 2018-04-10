# docker events

Docker でコンテナが restart したり stop したときにイベントを拾う方法はないかな？
とおもっていたらそのものズバリな `docker events` というサブコマンドがあるらしい。

```
$ docker events
```

このままだとログ形式で出力される。

## JSON 形式

```
$ docker events --format '{{json .}}'
```

jq にパイプして Slack に通知、とかはコマンドラインでもできそう。

## リファレンス

https://docs.docker.com/engine/reference/commandline/events/

