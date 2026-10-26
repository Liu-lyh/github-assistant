# GitHub API Assistant

一个基于 Python 和 GitHub REST API 编写的仓库信息查询工具，可以根据用户输入的用户名和仓库名，查询 GitHub 仓库的基本信息。

## 功能介绍

- 根据用户名和仓库名查询 GitHub 仓库。
- 获取仓库名称、Star 数量和 Fork 数量。
- 使用 `requests` 发送 HTTP 请求。
- 设置请求超时时间，并处理常见网络异常。
- 根据 HTTP 状态码处理请求结果，包括 404、403 和 429。
- 对用户输入进行基础校验，避免用户名或仓库名为空。

## 环境要求

- Python 3.10+
- requests

## 安装依赖

在终端中执行：

```bash
pip install requests
```

## 运行方式

进入项目目录，在终端中执行：

```bash
python main.py
```

根据提示输入 GitHub 用户名和仓库名，即可查询对应仓库的信息。

## 运行示例

```text
用户名：huggingface
仓库：transformers

transformers
（Star 数量）
（Fork 数量）
```

实际输出的 Star 和 Fork 数量以 GitHub API 返回的数据为准。

## 项目结构

```text
github-assistant/
├── main.py
├── github_api.py
└── README.md
```

- `main.py`：负责接收用户输入、校验输入、调用查询函数并展示结果。
- `github_api.py`：负责调用 GitHub API、处理网络异常和 HTTP 状态码，并返回仓库数据。
- `README.md`：项目说明文档。

## 技术栈

- Python
- requests
- HTTP / REST API
- JSON
- Git

## 后续改进

- 增加更完善的用户名和仓库名校验。
- 优化错误提示和日志记录。
- 支持查询更多仓库信息。
- 将项目整理为更易维护和扩展的结构。