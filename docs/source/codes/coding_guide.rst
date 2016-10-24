CafePy Coding Guidance In Japanses
===================================


1. ファイルを読み込む時はutils/cafepy_base.pyのreadを使え。
-------------------------------------------------------------------------

このモジュールはファイル名の拡張子からファイルの種類を判断し、適切なAPIを通じてデータを返す。 多くのcore/*.pyはcafepy_baseを継承しているので、 :code:`self.read('filename')` で呼び出すことが出来る。また、 :code:`self.sfx` にファイルの拡張子が代入されるので、それを参照してプログラムの分岐を考えれば良い。

使い方は

.. code:: python

   import cafepy_base
   data = cafepy_base.read('filename')
   """
   return data
   """


2. testディレクトリ内でテストを実行するときは :code:`py.test` を使え。
----------------------------------------------------

pythonで実行すると、相対パスをパスを解決することができない。

   
3. テストを書くときはtest_base.CafePyTestBaseを継承せよ。
-----------------------------------------------------------

このクラスは :code:`unittest.TestCase` を継承している。そのため、使い方はそれを継承している時と変わらない。しかし、コンストラクタとしてtest/data/へのパスの設定と :code:`self.data_path` へのtest/dataの設定を行っているので、テストケースを書くときのパス設定を減らしてくれる。
