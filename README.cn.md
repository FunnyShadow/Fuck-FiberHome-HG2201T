# Fuck You FiberHome HG2201T !
优雅的操翻你的烽火 HG2201T 路由器

## 这是什么?

这个脚本可以帮助你优雅的操翻 FiberHome HG2201T，只需要一条命令便可以得到它的所有底细 :D

## 我该怎么使用它?

1. 整点薯条
2. 随便打开一个能运行 Python 脚本的终端 (CMD 或者 Bash, 随你便)
3. 运行
```bash
git clone https://github.com/FunnyShadow/Fuck-FiberHome-HG2201T.git
python install -r requirements.txt
python decode.py
```

> 有些时候, 那些脑子有问题的厂商总喜欢偷偷改掉 `baseinfoSet.cgi` 的存储位置, 并认为这可以阻挠我们操翻它们, 不过我们完全不用担心这个问题, 你可以使用下面这条命令来指定一个新的 URL
```bash
python decode.py -u <你的 baseinfoSet.cgi 文件 URL>
```

## 如果我想在我的项目里面引用它呢?

如果你不认为这段 shitcode 非常的烂, 你可以随意使用它

## 开源许可

本项目按照 Apache 2.0 开源协议进行开源
