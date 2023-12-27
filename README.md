# mypkg
ROS2で使えるパッケージであり、talker,listenerの二つのノードを使用し、メッセージの送受信を行い、talkerが行っているcountupをlistenerが読み取る。

## ダウンロード方法
mypkgフォルダーに入っているファイルをコピーし、新規ファイルに貼り付けてください。

## 起動する手順
端末1でtalkerを立ち上げる。
```
端末1 $ ros2 run mypkg talker
```
何も表示されないのでこのまま別の端末でROS2を使い、サブスクライバを持つlistenerを立ち上げる。
```
端末2 $ ros2 run mypkg listener
...
data: 46
---
data: 47
---
data: 48
---
...
```
このようにtalker側の/countupからメッセージをもらってlistenerで表示させている。

## メッセージの型
talkerからlistenerに流れるデータの方は16ビットの符号付き整数である。

## OS
* Windows
* MacOS
* Linux

## Pythonのバージョン
* Python3

## 必要なソフトウェア
* Python
  * テスト済み: 3.7~3.10
* ROS2

## テストの結果
![test](https://github.com/taisei0515/mypkg/actions/workflows/test.yml/badge.svg)

## 権利関係

* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージは，3条項BSDライセンスの下、ryuichiueda/robosys2023由来のコード（© 2022 Ryuichi Ueda）を利用しています．
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
* [ryuichiueda/my_slides robosys_2022/lesson10.md](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022/lesson10.md)
* © 2023 taisei0515
