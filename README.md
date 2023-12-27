# mypkg
ROS2で使えるパッケージであり、talker,listenerの二つのノードを使用し、メッセージの送受信を行う。

## 起動する手順
端末1でtalker.pyを立ち上げる。
```
端末1 $ ros2 run demo_nodes_py talker
```

## 使い方

```
$ seq 5 | ./plus
$ 15

```

## OS
* Windows
* MacOS
* Linux

## Pythonのバージョン
* Python3

## 必要なソフトウェア
* Python
  * テスト済み: 3.7~3.10

## テストの結果
![test](https://github.com/taisei0515/robosys202x/actions/workflows/test.yml/badge.svg)

## 権利関係

* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージは，3条項BSDライセンスの下、ryuichiueda/robosys2023由来のコード（© 2022 Ryuichi Ueda）を利用しています．
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
* [ryuichiueda/my_slides robosys_2022/lesson10.md](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022/lesson10.md)
* © 2023 taisei0515
