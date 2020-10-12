"""
pivottablejsでピボットテーブル作れるhtmlを出力する
列数行数大きすぎると重くて使えないが。。。（300列あるとなんもでなくなる）

Usage:
    $ conda activate tfgpu
    $ python csv2pivot_html.py -o ./ -i ./train.csv
"""
import os
import pathlib
import argparse
import pandas as pd
from pivottablejs import pivot_ui
from IPython.display import HTML

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "-o", "--output_dir", type=str, default="./", help="output dir path.",
    )
    ap.add_argument(
        "-i", "--input_csv", type=str, help="input csv path.",
    )
    args = vars(ap.parse_args())

    os.makedirs(args["output_dir"], exist_ok=True)
    df = pd.read_csv(args["input_csv"])
    outfile_path = f'{args["output_dir"]}/{pathlib.Path(args["input_csv"]).stem}.html'

    # pivot html出力
    pivot_ui(df, outfile_path=outfile_path)
    HTML(outfile_path)
