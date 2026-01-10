#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 读取文件
with open('九、数据挖掘案例-南方电网时序预测.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 替换路径
old_pattern1 = '.\assets\'
new_pattern1 = 'images/九、数据挖掘案例-南方电网时序预测.md/'

old_pattern2 = 'assets\'
new_pattern2 = 'images/九、数据挖掘案例-南方电网时序预测.md/'

content = content.replace(old_pattern1, new_pattern1)
# 注意：要先替换带点的，避免assets\被重复替换
content = content.replace(old_pattern2, new_pattern2)

# 写回文件
with open('九、数据挖掘案例-南方电网时序预测.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("替换完成")
print(f"替换次数1: {content.count(new_pattern1)}")
print(f"替换次数2: {content.count(new_pattern2)}")
