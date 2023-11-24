# はじめに

pythonを用いた計測器制御の方法を最近知りました。
有名な計測器制御ソフト（LabV*EWなど）と比べて、汎用性・自由度が高いことに感動を覚えています。
具体的なサンプルプログラムなどは後日まとめるとして、ここでは使用頻度の高いpyvisaのコマンドを列挙します。
自分用の備忘録なのであしからず。

参考ページ: PyVISA
<https://pyvisa.readthedocs.io/en/latest/>

# 環境

python3.7.7
Windows10

# 環境構築

ここではPythonはインストール済と想定しています。

### NI-VISAのインストール

通信を行うために必要なもの。National Instrumentsが無償提供するものが一般的。自分の使用するPCのOSにあったものをインストールする。他にもPyVISAでは、他社提供のVISAでも動く。
（Keysight VISA, R&S VISA, tekVISA、など）

### PyVISAのインストール

pip（pip3）から入れる。

```
pip install pyvisa
```

これで環境構築は完了。
非常に簡単。

## サンプルコード

```python
import pyvisa

rm = pyvisa.ResourceManager()
visa_list = rm.list_resources()
usb_1 = visa_list[0]
inst_1 = rm.open_resource(usb1)

inst_1.write('*IDN?')
out = inst_1.read()

# queryを用いてももちろんOK
# out = inst_1.query('*IDN?')

print(out)
# (計測器の情報）
```

以下より、このコードの説明をする。

python上でimport、インスタンスの生成を行う。

```python
import pyvisa

# インスタンス生成、おまじないのようなもの
rm = pyvisa.ResourceManager()
# PCに接続された計測器のVISAリソース名の取得
visa_list = rm.list_resources()
```

ここで、```rm```は任意。また、```rm.list_resources()```はlistでVISAリソース名が返ってくる。ここでは機器1つがUSBポートに接続されていると仮定。VISAリソース名の取得を行う。

```python
# VISAリソース名
usb_1 = visa_list[0]
```

VISAリソース名を使って、計測器を指定。

```python
# 計測器の指定
inst_1 = rm.open_resource(usb1)
```

### VISA書き込み

```python
inst_1.write('*IDN?')
```

```'*IDN?'``` は計測器の機種情報を聞くためのコマンド。多くの機器で採用されている。

### VISA読み込み

```python
inst_1.read()
```

先程送ったクエリに対する返答を読むことができる。
今回、'IDN?'を送っているので、機種情報が返ってくる。

### VISAクエリ

```python
inst_1.query('*IDN?')
```

クエリを送り、返り値を受け取るまで一度に行ってくれるスグレモノ。上2つを1行で書くことができるため、簡素化することができる。
なお、クエリのないコマンドを送るとエラーが出るため注意。

### 複数コマンドの一度送信

```python
inst_1.write('*rst, *IDN?')
```

複数のコマンドを一度に送信することもできる。機器の設定コマンドなど、何行も書くとプログラムが煩雑になる。これを使うといくぶんかスッキリする。
ただ、一度に多くのコマンドを送りすぎると、通信が追いつかなくなるため、時間を置くなど様子見は必要。

ここまでで紹介したVISA通信用コマンドと、ループ等のプログラミング基礎骨格、計算などを組み合わせ、制御プログラムを構築する。
なお、VISAを経由し計測器に送るSCPI通信用のコマンドは、各種計測器の取説を参照すること。

# 最後に

ここではPythonを使って計測器を制御する方法について説明しました。
計測器との接続方法は、USBケーブル、NI社のUSB-GPIBケーブルを使うと良いと思います。
GPIBケーブルは少々高額だし、最近の計測器は基本的にUSB端子がついてるので、USBケーブルでの接続をおすすめします。

# 関連記事
<https://qiita.com/YujiMatsu/items/8e0437b33555647b0fc4>
