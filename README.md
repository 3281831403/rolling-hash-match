# 滚动哈希：多项式、子串与碰撞校验

特征串扫描漏报、长文本越扫越慢：多项式哈希没有取模，滚动窗口没有减掉旧字符，哈希命中没有校验原文，出现次数把重叠也算错，空模式崩，批量扫描只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
scan/__init__.py
scan/rolling_hash.py
tests/test_rolling_hash.py
```

## 当前状态

`scan/rolling_hash.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_rolling_hash.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 多项式哈希取模
2. 滚动窗口减旧字符
3. 命中后校验原文
4. 重叠出现计数
5. 空模式兜底
6. 批量扫描统一提交

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `scan/rolling_hash.py`
后 15 条用例应全部通过。
