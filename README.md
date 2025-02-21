# Simple Captcha Solver

**简体中文 | [English](README_en.md)**

一个简单易用的 Python 工具，用于识别图形验证码。支持从 URL 或本地路径加载图片，并通过 `ddddocr` 进行识别。

## 功能特性

- 支持单个验证码识别（本地文件或网络URL）
- 支持批量处理目录下的所有图片文件
- 支持根据文本文件中的URL列表进行批量验证码识别
- 自动检测系统语言环境并调整输出语言（中文或英文）
- 提供命令行参数支持直接执行特定任务

## 安装
1. 克隆仓库：
   ```bash
   git clone https://github.com/yourusername/simple-captcha-solver.git
   ```
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
   如果没有 `requirements.txt` 文件，可以手动安装依赖：
   ```bash
   pip install ddddocr requests
   ```

## 使用方法
### 1. 通过命令行参数调用

运行脚本时可以指定以下参数：

- `-f <url_or_path>`：通过提供的URL或文件路径识别验证码。
- `-d <directory>`：批量识别指定目录下的所有文件。
- `-i <url_file>`：通过提供的文本文件中的URL批量识别验证码。

例如：

```bash
python captcha_tool.py -f "http://example.com/captcha.jpg"
python captcha_tool.py -d "/path/to/directory"
python captcha_tool.py -i "/path/to/urls.txt"
```

### 2. 交互式输入

如果未指定任何命令行参数，程序将显示一个交互式菜单，您可以通过输入数字选择相应的功能：

1. 识别单个文件或URL
2. 批量识别目录中的所有文件
3. 批量识别在线URL
4. 退出程序

根据提示输入相关信息即可开始识别过程。


## 代码结构
```plaintext
simple-captcha-solver/
├── main.py                # 主程序入口
├── captcha_solver.py/     # 验证码识别模块
├── requirements.txt       # 依赖文件
├── test_image/            # 测试图片
│   ├── test.png
│   ├── test.bmp
│   ├── test.jpg
│   ├── test.webp
├── README.md              # 项目说明文档
└── LICENSE                # 开源许可证
```


## 注意事项
1. **依赖项**：
   - `ddddocr`：用于验证码识别。
   - `requests`：用于从 URL 下载图片。
2. **缓存清理**：
   - 程序会在 `pic_cache` 目录中缓存下载的图片，运行结束后会自动清理。
3. **语言支持**：
   - 程序会根据系统语言自动切换为中文或英文。

## 贡献指南
欢迎贡献代码或提出改进建议！如果你发现任何问题或有新的功能需求，请提交 [Issue](https://github.com/yourusername/simple-captcha-solver/issues)。

## 开源许可证
本项目采用 [GPL-3.0 License](LICENSE) 开源许可证。



