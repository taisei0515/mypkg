# mypkg
ROS2で使えるパッケージであり、talker,listenerの二つのノードを使用し、メッセージの送受信を行い、talkerが行っているcountupをlistenerが読み取る。

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

## talker
トピックに継続的にメッセージを送信する。

## listener
talkerからのトピックからメッセージを受け取り、反映する。

## メッセージの型
talkerからlistenerに流れるデータの方は16ビットの符号付き整数である。

## Pythonのバージョン
* Python3

## 必要なソフトウェア
* Python
  * テスト済み: 3.7~3.10
* ROS2 (Humble Hawksbill)

## ROS2のUbuntu対応バージョン
Humble HawksbillではUbuntu 22.04が推奨されています。

## テストの結果
![test](https://github.com/taisei0515/mypkg/actions/workflows/test.yml/badge.svg)

## テスト環境
* Ubuntu(22.04)

## 権利関係
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
  * [ryuichiueda/my_slides robosys_2022/lesson8.md](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022/lesson8.md)
* © 2023 taisei0515
