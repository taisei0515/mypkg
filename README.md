# mypkg
ROS2で使えるパッケージであり、talker,listenerの二つのノードを使用し、メッセージの送受信を行う。

## インストール方法
このパッケージを使用するためにROS2をインストールします。
### ROS1がすでにインストールされている場合
初めに別の環境を準備してください。
```
$ vi ~/.bashrc
```
と入力し、.bashrcに関係する記述を#を付けてコメントアウトしてください。
### ROS2のインストール方法
```
$ git clone https://github.com/ryuichiueda/ros2_setup_scripts
```
```
$ cd ros2_setup_scripts
```
```
$ ./setup.bash
```
ここまでできたら動作確認をします。
```
$ source ~/.bashrc
```
これでROS2のインストールは完了です。

## ダウンロード方法
```i
$ chmod +x plus
```

## 起動する手順
* 数列が入ったファイルを用意してください。(例)seq 5
* seq 5は1~5の数列を作ります。

## 簡単な使い方

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
