# 大纲

## 1. 实现的功能

```
cli
  hello
    --count 3 abc
  cal
    sum 1 2 3
    min 12 3 4
```

## 2. 原生脚本

cli1

<!--
- sys.argv
- hello
- cal
- parse
- handle
-->

## 3. 使用 click

[Click](https://click.palletsprojects.com/en/6.x/)

### 从原生脚本到 click

<!--
- 安装 click
- cli2
- 复制 hello, cal
- 添加装饰器
- 解释装饰器
https://www.python.org/dev/peps/pep-0318/#motivation
日志，鉴权
-->

## 4. 单元测试

- cli1 测试

- cli2 测试
<!-- 把 ! 改成 . -->

## 5. 打包

setup.py

[Setuptools Integration](https://click.palletsprojects.com/en/6.x/setuptools/#setuptools-integration)

`pip install --editable .`

## 6. 命令补全

[Bash Complete](https://click.palletsprojects.com/en/6.x/bashcomplete/)

`_CLI2_COMPLETE=source cli2 > cli2-complete.sh`

`. /vagrant/cli2-complete.sh`

### 原理

readline complete

[Programmable Completion](https://www.gnu.org/software/bash/manual/html_node/Programmable-Completion.html)

## 7. shell 中的 getopt, getopts

## 8. 总结

使用 click
