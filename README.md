# mypkg
千葉工業大学のロボットシステム学の講義内で扱ったレポジトリです。

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
中止する場合はctrl+C

* 一度に二つのノードを立ち上げる場合
```
$ ros2 launch mypkg talk_listen.launch.py
```
実行結果は次の通りになる。
```
[INFO] [launch]: All log files can be found below /home/raisu/.ros/log/2024-01-13-14-29-53-665808-DESKTOP-AKKN6N4-294
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [296]
[INFO] [listener-2]: process started with pid [298]
[listener-2] [INFO] [1705123795.385050900] [listener]: Listen: 0
[listener-2] [INFO] [1705123795.805992900] [listener]: Listen: 1
[listener-2] [INFO] [1705123796.306473000] [listener]: Listen: 2
[listener-2] [INFO] [1705123796.805138700] [listener]: Listen: 3
[listener-2] [INFO] [1705123797.305697000] [listener]: Listen: 4
[listener-2] [INFO] [1705123797.805182600] [listener]: Listen: 5
[listener-2] [INFO] [1705123798.307108300] [listener]: Listen: 6
[listener-2] [INFO] [1705123798.804587300] [listener]: Listen: 7
[listener-2] [INFO] [1705123799.304705800] [listener]: Listen: 8
[listener-2] [INFO] [1705123799.804512500] [listener]: Listen: 9
[listener-2] [INFO] [1705123800.304073000] [listener]: Listen: 10
[listener-2] [INFO] [1705123800.805816800] [listener]: Listen: 11
[listener-2] [INFO] [1705123801.304898100] [listener]: Listen: 12
[listener-2] [INFO] [1705123801.804237900] [listener]: Listen: 13
[listener-2] [INFO] [1705123802.305331000] [listener]: Listen: 14
[listener-2] [INFO] [1705123802.804934500] [listener]: Listen: 15
[listener-2] [INFO] [1705123803.304293100] [listener]: Listen: 16
[listener-2] [INFO] [1705123803.804467800] [listener]: Listen: 17
[listener-2] [INFO] [1705123804.304669400] [listener]: Listen: 18
```
中止する場合はctrl+C

## talker
パブリッシャを持つノード。トピックに継続的にメッセージを送信する。

## listener
サブスクライバを持つノード。talkerからのトピックからメッセージを受け取り、反映する。

## talk_listen.launch.py
talkerとlistener二つのノードを一度に立ち上げる。

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
