# Deep Learning

本仓库用于学习《动手学深度学习》（Dive into Deep Learning，D2L），按照教材的大章汇总代码、Notebook、笔记、练习和实验记录。

## 组织原则

- 只使用 15 个固定的大章目录，不在章内建立节级目录。
- Notebook 用于逐段运行、展示结果和理解过程。
- Python 文件用于调试、重构、练习和自动验证。
- 外部代码必须记录原始仓库、固定版本、作者、许可证和修改内容。
- 数据集、模型权重、大型输出、日志和本地环境不进入 Git 历史。
- 主分支只保存已经完成并验证的学习成果；每个大章在独立学习分支中完成后再合并。

## 章节目录

| 编号 | 教材大章 | 官方源码目录 |
| --- | --- | --- |
| 01 | 引言 | `chapter_introduction` |
| 02 | 预备知识 | `chapter_preliminaries` |
| 03 | 线性神经网络 | `chapter_linear-networks` |
| 04 | 多层感知机 | `chapter_multilayer-perceptrons` |
| 05 | 深度学习计算 | `chapter_deep-learning-computation` |
| 06 | 卷积神经网络 | `chapter_convolutional-neural-networks` |
| 07 | 现代卷积神经网络 | `chapter_convolutional-modern` |
| 08 | 循环神经网络 | `chapter_recurrent-neural-networks` |
| 09 | 现代循环神经网络 | `chapter_recurrent-modern` |
| 10 | 注意力机制 | `chapter_attention-mechanisms` |
| 11 | 优化算法 | `chapter_optimization` |
| 12 | 计算性能 | `chapter_computational-performance` |
| 13 | 计算机视觉 | `chapter_computer-vision` |
| 14 | 自然语言处理：预训练 | `chapter_natural-language-processing-pretraining` |
| 15 | 自然语言处理：应用 | `chapter_natural-language-processing-applications` |

前言、安装说明、符号说明、附录和参考资料统一放在 `00-辅助资料`，不占用章编号。个人跨章笔记放在 `notes`，数据下载说明放在 `data`。

## 当前内容

当前完成了第 03 章“线性神经网络”的最小学习与验证材料：

- 官方“线性回归的从零开始实现”原文快照；
- 去除 D2L 辅助包依赖、可直接运行的 PyTorch Python 文件；
- 与 Python 文件内容对应的 Notebook；
- 学习笔记、练习入口和固定来源记录。

其余章目录先作为固定入口保留，开始学习时再从主分支建立对应的整章学习分支。

## 学习分支约定

开始一个大章时：

```powershell
git switch main
git pull --ff-only
git switch -c study/chXX-chapter-name
```

完成整章、检查并提交后合并：

```powershell
git switch main
git merge --no-ff study/chXX-chapter-name
git push origin main
```

学习过程中只暂存本次实际完成的文件和笔记：

```powershell
git status
git diff
git add "03-线性神经网络/文件路径"
git commit -m "ch03: 完成线性回归从零实现"
git push -u origin study/ch03-linear-neural-networks
```

## PyCharm 使用

1. 用 PyCharm 直接打开本仓库根目录。
2. 在 `Settings → Project → Python Interpreter` 中选择根目录下创建的 `.venv\Scripts\python.exe`。
3. 安装依赖：

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   .\.venv\Scripts\python.exe -m pip install -r requirements-torch-cpu.txt
   ```

4. 运行第 03 章示例：

   ```powershell
   .\.venv\Scripts\python.exe "03-线性神经网络\linear_regression_scratch.py"
   ```

PyCharm 的 `.idea`、虚拟环境、Notebook 检查点和运行输出均已加入 `.gitignore`。

## 数据与外部代码

- 数据集只在 `data/README.md` 记录来源和下载方式，不提交大型数据文件。
- 外部代码及许可证记录见 `THIRD_PARTY_NOTICES.md`。
- 当前采用的官方中文教材仓库：[d2l-ai/d2l-zh](https://github.com/d2l-ai/d2l-zh)
- 固定版本：`e6b18ccea71451a55fcd861d7b96fddf2587b09a`（2023-08-17）
- 远程仓库：[huarunxin001-oss/deep-learning](https://github.com/huarunxin001-oss/deep-learning)

## 参考资料

- [中文在线教材](https://zh.d2l.ai/)
- [英文在线教材](https://d2l.ai/)
- [官方中文源码](https://github.com/d2l-ai/d2l-zh)
- [官方英文源码](https://github.com/d2l-ai/d2l-en)
