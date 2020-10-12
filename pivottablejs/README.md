# pivottablejs: ピボットテーブル作れるhtmlを出力するパッケージ の使い方メモ

## Install
```bash
$ conda install -c conda-forge jupyter_pivottablejs
or
$ poetry add pivottablejs
```

## Usage
```bash
$ python csv2pivot_html.py -o ./ -i ./train.csv
# カレントディレクトリにtrain.csvのピボットテーブル出すtrain.html 出力。※サンプルのtrain.csvはバイクシェアリングのデータ
```

## 参考サイト
- https://towardsdatascience.com/interactive-pivot-tables-in-jupyter-notebook-fc74bad8aa67

