# 工业大数据产业创新平台/工业大数据创新竞赛/风机叶片结冰预测大赛

*网址：http://www.industrial-bigdata.com/*

该竞赛为2017年的一个工业大数据应用比赛， 围绕真实采集的风机数据，分为两个比赛题目。本仓库主要关注题目一：风机叶片结冰预测大赛。

由于官网已不再提供完整数据，互联网上也找不到资源，我们特地与对方联系获取了所需的比赛数据，添加到了本仓库的release中。

本仓库部分代码借鉴了[另一个GitHub仓库](https://github.com/BreezeDoo/Industrial_big_data_contest)

### 脚本说明：

1. console.py——控制台，作为函数调用的总端口
2. labelGen.py——从原始数据中生成结冰标签信息
3. feature_selector_process.ipynb——用feature_selector库**尝试**预筛选数据的Jupyter Notebook草稿本
4. Script.ipynb—观察特征关系的草稿本
5. plot.py—两特征作图观察(与草稿本同)
6. avgData.py——根据时间戳对数据分组取平均值处理
7. cutPower.py——截去高功率数据（依据：观察得功率高时无结冰）
8. svm_method.py——使用SVM算法训练模型
9. score.py——计算模型准确率及得分
10. tmp.py—求C参量脚本（未接入console.py）

### 其它备忘：

1. 用2016专业增强版打开15/15_failureInfo.csv文件会导致时间戳中秒数信息的丢失，其它文件暂未发现该问题；用EditPlus打开不会造成该现象，强烈建议使用EditPlus或其它文本编辑器查看所有的.csv文件
2. 错误认为15_failureInfo.csv没有秒数信息时，编写了脚本addSecTo15Failure.py处理这个问题：将原文件改名为15_failureInfo_raw.csv，运行脚本，得到新的15_failureInfo.csv补充秒数信息（start时间补充为00秒，end时间补充为59秒）。根据1，此脚本实际上是**不需要运行**的
3. 关于参量C，参考了论文Ice Detection Model of Wind Turbine Blades Based on Random Forest Classifier (Zhang et al._2018_energies-11-02548.pdf)，还有△C等更多参量尚未提取。
