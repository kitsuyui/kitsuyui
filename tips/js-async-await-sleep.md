# JavaScript の async/await で sleep

```javascript
const sleep = (time) =>
  new Promise((resolve, reject) =>
    setTimeout(resolve, time));

(() => {
  (async () => {
    console.log('Hello, World!');
    await sleep(1000);
    console.log('foo');
    await sleep(2000);
    console.log('bar');
  })()
})();
```
