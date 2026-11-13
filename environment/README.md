# Python 环境

本项目使用 Python 3.11，并在仓库根目录创建 `.venv` 作为 PyCharm 解释器。

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip install -r requirements-torch-cpu.txt
```

`requirements-torch-cpu.txt` 使用 PyTorch 官方 CPU 索引，适合当前以学习和小规模实验为主的阶段。若以后需要使用 NVIDIA GPU，请根据 PyTorch 官方安装页面选择和当前 CUDA 驱动兼容的版本。

`.venv` 已被 `.gitignore` 排除，不能提交解释器、第三方包或本地环境信息。

本次实际验证环境：

- Python 3.11.5
- PyTorch 2.15.0+cpu
- NumPy 1.26.4
- JupyterLab 4.6.6
- PyCharm 2023.1.6

在 PyCharm 中选择 `.venv\Scripts\python.exe` 后，可以直接运行第 03 章的 Python 文件；Notebook 会使用该项目解释器。
