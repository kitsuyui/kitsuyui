# System Restart Required 

と言われたときに、一体何が reboot を要求してるのか知りたいことがある。
たいていセキュリティパッチを当てるとそうなる

# ファイル

/var/run/reboot-required.pkgs

にある。でも大量にパッケージがあるとき、重複して表示するのでわかりにくい

## なのでユニークにする

こういう感じ

```
$ cat /var/run/reboot-required.pkgs | sort -n | uniq
dbus
libc6
libssl1.0.0
linux-base
linux-image-4.4.0-57-generic
linux-image-4.4.0-59-generic
linux-image-4.4.0-62-generic
```
