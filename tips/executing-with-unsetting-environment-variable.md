# 環境変数を消しつつ実行する 2 つの方法とその違い

`FOO` 環境変数を消した環境で `some-command` を実行したいとする。
ただしカレントシェルの方の変数を消してはならないとする。

つまり

```console
$ unset FOO
$ some-command
```

は認められない

## サブシェルを使う

```console
$ (unset FOO; some-command)
```

こうするとサブシェル内だけで FOO を消せる

## `env -u` を使う

```console
$ env -u FOO some-command
```

こうすると、やはり FOO を消しつつ `some-command` を実行できる

## 違い

後者の方は `exec` できるが

```
$ exec env -u FOO some-command
```


前者の方はできない

```console
$ exec ( unset FOO ; some-command )
-bash: syntax error near unexpected token `unset'
```

しかし大抵の場合は `exec` したいケースでは、 2 行にわけて

```console
$ unset FOO
$ exec some-command
```

と書けるので問題にならない。

問題になるのは `PATH` のような環境変数を消しながら実行したい場合。
カレントシェルの `PATH` を保ちつつ `some-command` を実行する場合。
自分の知るかぎり後者でしかできない。
