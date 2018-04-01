# SSH Dynamic Forward

```
$ ssh -N -D 1080 proxy_server
```

# curl with --socks5 option

```
$ curl --socks5 127.0.0.1:1080 http://httpbin.org/ip
```

# ~/.curlrc

```
socks5 = "127.0.0.1:1080"
```

# ~/.proxy.pac

```
// https://en.wikipedia.org/wiki/Proxy_auto-config
function FindProxyForURL (url, host) {
  // DIRECT means pass-through when fail.
  return "SOCKS5 127.0.0.1:1080; DIRECT";
  // return "SOCKS5 127.0.0.1:1080;";
}
```
