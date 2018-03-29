# jq で JSON を組み立てる

jq はクエリで絞り込むだけが華じゃなく、テンプレート的に JSON を組み立てるのもできる。
しかし、そんなに頻繁に使う機能ではないので、オプションとか書式とかを忘れやすい。

# 生の入力を JSON に

```
$ echo -n 'a' | jq -R -c -M '{"name": .}'
{"name":"a"}
```

# 文字列を数値として JSON に

```
$ echo -n '1' | jq -R -c -M '{"num": .|tonumber}'
{"num":1}
```

## ちなみに関数はこちらに

https://stedolan.github.io/jq/manual/#Builtinoperatorsandfunctions

# JSON を JSON に

```
$ echo '{"a": "x", "b": "y"}' | jq -c -M '[.a, .b]'
["x","y"]
```
