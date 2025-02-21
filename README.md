# Simple Captcha Solver

**简体中文 | [English](README_en.md)**

一个简单易用的 Python 工具，用于识别图形验证码。支持从 URL 或本地路径加载图片，并通过 `ddddocr` 进行识别。

## 功能特性
1. **多语言支持**：根据系统语言自动切换中文或英文界面。
2. **图片下载**：支持从 URL 下载验证码图片。
3. **本地文件支持**：支持直接从本地路径加载图片。
4. **多文件格式支持**：支持多种图片格式。
5. **缓存清理**：自动清理缓存文件，避免占用过多磁盘空间。
6. **错误处理**：对常见错误进行处理并提供友好的提示信息。

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
运行以下命令：
```bash
python main.py -f <image_url_or_path>
```

#### 示例
- **从 URL 识别验证码**：
  ```bash
  python main.py -f https://example.com/captcha.jpg
  ```
- **从本地路径识别验证码**：
  ```bash
  python main.py -f ./captcha.jpg
  ```

### 2. 交互式输入
如果不提供 `-f` 参数，程序会提示输入图片 URL 或路径：
```bash
python main.py
```

#### 示例
```bash
请输入图片URL或路径：https://example.com/captcha.jpg
```

### 3. 输出结果
- **识别成功**：
  ```
  验证码文本为：1234
  ```
- **识别失败**：
  ```
  解码时发生错误：无法识别验证码
  ```

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

## 参数说明
| 参数 | 描述 |
|------|------|
| `-f` | 指定验证码图片的 URL 或本地路径 |
| `-h` | 显示帮助信息并退出 |

## 示例运行
### 1. 从 URL 识别验证码
```bash
$ python main.py -f https://example.com/captcha.jpg
验证码文本为：1234
```

### 2. 从本地路径识别验证码
```bash
$ python main.py -f ./captcha.jpg
验证码文本为：5678
```

### 3. 交互式输入
```bash
$ python main.py
请输入图片URL或路径：https://example.com/captcha.jpg
图片下载成功。
验证码文本为：1234
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



