# ブラウザのネイティブ代入を別のものに置き換える

```js
const getPrototype = (obj) => {
  if (obj === document) {
    return Document.prototype;
  }
  return obj.constructor.prototype;
}

const redefinePropertyWithOriginal = (target, key, proxyTo) => {
  const proto = getPrototype(target);
  const original = Object.getOwnPropertyDescriptor(proto, key);
  const get = original.get.bind(target);
  const set = original.set.bind(target);
  Object.defineProperty(target, key, proxyTo({get, set}));
}
```

## 例: document.cookie への代入をコンソールにログ出力したい。

document.cookie を操作する 3rd party のライブラリを使っているときに重宝する。
引数や this にたいして console.dir を実行すれば、それらのライブラリが何をやっているのかを確認できる。他のあらゆる中間の処理も加えることができる。

```js
redefinePropertyWithOriginal(document, 'cookie', (original) => {
  return {
    get() {
      console.dir(this);
      console.dir(arguments);
      return original.get(...arguments);
    },
    set() {
      console.dir(this);
      console.dir(arguments);
      return original.set(...arguments);
    }
  }
});
```
