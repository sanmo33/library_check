# library_check

こんにちは。ICU関係者の皆さん。

Macユーザー向けにICU図書館に新しい書籍が入ったら通知でお知らせをしてくれるプログラムを書いてみました。
library_check.pyを実行すると、ICU図書館に新しい書籍が入っていれば「New Books Arrive!」と通知されるプログラムです。

同一ディレクトリ(フォルダ)内にlibrary_check.pyとcheck.txtを存在させるようにしてください。

プログラムを書いていない人のmacbookには

・python3

・feedparser

の二点がインストールされていないかもしれません。

python3は https://www.python.org/downloads/ こちらから入手できまる。
feedparserはterminalで [pip3 install feedparser]と打ち込めば入手できます。

「python3 インストール」や「feedparser インストール」などと検索すればわかりやすいインストール方法が出てきますのでそちらを参考にしてください。

crontabやAutomatorなどを利用すると毎日決まった時間に通知を受け取ることも可能です。

もしなにかございましたらTwitter @mosanul までご連絡ください。よろしくおねがいします。
