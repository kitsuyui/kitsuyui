# Python で functional な書き方をしてみる練習

[map, reduce もいいけど transduce もね](https://qiita.com/41semicolon/items/666a3ff1c226828ecdb2) を読んだ元同僚から、「Python ではどう書くの？」と質問を受けたのでチャレンジしたら、思いのほか熱中してしまった。

## やったこと

functional.py を作った。

## テスト

functional.py の中で test* の名称になっているものは全てテストコード。

docker build . でテストできるようにしている。

## ポリシー

- なるべく可変長引数が外部に出ないようにラップし、完全ではないものの 1 引数にした。 なるべく全てを関数にした。

- tranceduce を使って map と filter を作った。

- curry と uncurry はプリミティブなやり方では定義不可能なので safe_eval を定義してマクロによる定義という体裁にした。
(もちろん [inspect を使えば定義可能](http://code.activestate.com/recipes/577928-indefinite-currying-decorator-with-greedy-call-and/) )

- 用語はよくある関数型プログラミングから名前などは借用したつもりだが、用法は間違っているかもしれない。
