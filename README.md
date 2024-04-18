# AtCoder用コンテナ

最初はログインする
```bash
acc login
```

ログインできているか確認
```bash
acc session
```

online-judge-toolsへのログイン
```bash
oj login https://beta.atcoder.jp/
```

config
```bash
cd `acc config-dir`
mkdir python
cd python
touch template.json
touch main.py
code template.json
```
configの中身
```
 {
 "task":{
   "program": ["main.py"],
   "submit": "main.py"
     }
 }
```
config設定
```bash
acc config default-template python
```
コンテストの全データを読み出すように設定
```
acc config default-task-choice all
```
aliasを設定
~.bashrcに以下を追加
```bash
# PyPy3でのテスト実施
alias test='oj t -c "pypy3 main.py" -d ./tests/'
# Pythonでのテスト実施
alias test_python='oj t -c "python3 main.py" -d ./tests/'

# PyPy3での解答提出
alias sb='acc s main.py -- --guess-python-interpreter pypy'
# Pythonでの解答提出
alias sb_python='acc s main.py'
```


# コンテスト
```bash
acc new abc???
```

```bash
cd abc???
cd a
```
各フォルダのmain.pyを編集する。

submissionはフォルダ内で設定したaliasをたたくとよい。
```bash
sb
```