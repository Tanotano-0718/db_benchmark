# データベース性能評価ソフト

## 概要

- SQLの絞り込み性能を検証するため検索の実行時間表示を半自動化するソフトを作成する

## 環境

- Python3.10
- Windows 10
- xampp v3.3.0

## 機能

- main.pyより実行
- 性能評価用データはTPC-Hを用いた
- ウィンドウは入力と出力のタブで分かれていて、出力タブを押すたびに更新される
- 入力タブにはsqlを入力し、実行ボタンで実行
- 出力タブにはsql 実行時間　実行日時のリストが表示される
- 任意のSELECT文を入力すると実行時間が出るようになる
- wxPythonを用いたGUIアプリケーション

## 感想

- 最低限の機能しかつけていないのでsqlの構文エラーに対する処理も未完成
- 実行を押したときに何も表示されないので要修正

## 出展

- タブの実現
  - teratail <https://teratail.com/questions/288368?link=qa_related_sp>
- wxpython
  - <https://docs.wxpython.org/index.html>
- mysql × python
  - Dragon Arrow mysql-connector-python でMySQL操作の効率化 <https://www.dragonarrow.work/articles/248>
