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

## 3. 使用 click

### 从原生脚本到 click

### 使用 click 的好处

### click 的设计

装饰器设计模式

## 4. 单元测试

cli1 测试

cli2 测试

## 5. 打包

setup.py

`pip install --editable .`

## 6. 命令补全

https://click.palletsprojects.com/en/6.x/bashcomplete/

`_CLI2_COMPLETE=source cli2 > cli2-complete.sh`

`. /vagrant/cli2-complete.sh`

### 原理

readline complete
