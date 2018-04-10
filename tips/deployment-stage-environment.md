# production とか staging とか development とか

production 環境とか staging 環境とか development 環境とか、
そういったものを入れる変数を何にしようかと迷った。

XXXXX=production というような環境変数の XXXXX は何か。

単に environment と呼ぶと、普通の環境変数などと紛らわしい。

https://en.wikipedia.org/wiki/Deployment_environment

を読む限りだと

- tier
- environment
- stage

あたりの用語が適当なようだ。

一方で "staging stage" などと言うのも変な感じがする。
英語力の問題かもしれない。

ニュアンス的に environment とは、 deployment の各 stage ごとにあるもので、
environment は stage に付随して発生する差異だと思う。

tier は stage をもっと順序性と直列性を意識して呼ぶ呼び方なのかな？

## 結局自分の中では何が正解か

結論として

DEPLOYMENT_STAGE=production のような用法が自然かな？とおもっている。

