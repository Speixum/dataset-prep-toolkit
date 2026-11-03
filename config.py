# -*- coding: utf-8 -*-
"""路径配置 —— 换成你自己机器上的路径即可。

三个路径的含义：
  LABELME_DIR  Labelme 导出的多边形标注（每张图一个 .json）
  DATA587_DIR  已转换好的训练/测试数据（Train/Test 下各有 JPEGImages 与 BlackWhite）
"""
import os

# 数据根目录（按需修改）
DATASET_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

# Labelme 多边形标注目录
LABELME_DIR = os.path.join(DATASET_ROOT, "labelme_json")

# 已转换好的数据集目录（Train / Test）
DATA587_DIR = os.path.join(DATASET_ROOT, "data_587")

# 类别合并规则：原始多类 -> 统一成 1 类
# 依据：小类样本量过低（最小类仅 21 个多边形），单独成类学不动且拉低整体指标
MERGED_CLASS_NAME = "defect"
