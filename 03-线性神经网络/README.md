# 03 线性神经网络

教材大章：线性神经网络

官方源码目录：[`chapter_linear-networks`](https://github.com/d2l-ai/d2l-zh/tree/e6b18ccea71451a55fcd861d7b96fddf2587b09a/chapter_linear-networks)

## 官方教材源码

以下文件来自 `d2l-ai/d2l-zh` 的 `chapter_linear-networks`，是官方构建生成的完整 Markdown 教学源文件。文件内容保持原始字节不转换，便于与上游逐文件校验。

| 教材内容 | 本地官方快照 |
| --- | --- |
| 本章导读 | `index.official.md` |
| 线性回归 | `linear-regression.official.md` |
| 线性回归的从零开始实现 | `linear-regression-scratch.official.md` |
| 线性回归的简洁实现 | `linear-regression-concise.official.md` |
| Softmax 回归 | `softmax-regression.official.md` |
| Softmax 回归的从零开始实现 | `softmax-regression-scratch.official.md` |
| Softmax 回归的简洁实现 | `softmax-regression-concise.official.md` |
| 图像分类数据集 | `image-classification-dataset.official.md` |

官方目录中的 `_origin.md` 是生成正式章节文件前的工作草稿，正文和代码与对应的非 `_origin.md` 文件重复，因此不作为第二套学习材料重复放入仓库。

学习时重点查看 `#@tab pytorch` 和 `#@tab all` 代码块。官方文件同时维护 PyTorch、MXNet、TensorFlow 和 Paddle 版本；当前项目只需要 PyTorch 路径。

## 可运行与个人学习文件

- `linear_regression_scratch.py`：基于官方“从零实现”PyTorch 代码整理的可运行版本。
- `linear_regression_scratch.ipynb`：与 Python 文件对应的逐段学习 Notebook。
- `linear_regression_annotated.ipynb`：个人逐行注释版，由学习者从基线 Notebook 复制并按需提交。
- `notes.md`：概念、运行方法和练习记录。

来源、版本、许可证和修改说明见仓库根目录的 `THIRD_PARTY_NOTICES.md`。

运行：

```powershell
.\.venv\Scripts\python.exe "03-线性神经网络\linear_regression_scratch.py"
```
