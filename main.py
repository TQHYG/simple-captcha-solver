import tkinter as tk
from tkinter import filedialog, messagebox
import cli

def on_single_file():
    """处理单个文件或URL"""
    user_input = filedialog.askopenfilename(title="选择图片", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if user_input:
        parsed_url = cli.urlparse(user_input)
        if cli.os.path.isfile(user_input) or (parsed_url.scheme and parsed_url.netloc):
            cli.resolve_single(user_input)

def on_batch_directory():
    """批量处理目录"""
    directory = filedialog.askdirectory(title="选择要识别的目录")
    if directory:
        cli.batch_process_directory(directory)

def on_batch_urls():
    """通过文本文件中的URL批量处理"""
    url_file = filedialog.askopenfilename(title="选择包含URL的文本文件", filetypes=[("Text Files", "*.txt")])
    if url_file:
        cli.batch_process_urls(url_file)

def main_window():
    window = tk.Tk()
    window.title("验证码识别工具" if cli.lang == 'zh' else "Captcha Recognition Tool")

    btn_single = tk.Button(window, text="识别单个文件或URL", command=on_single_file)
    btn_single.pack(fill=tk.X)

    btn_batch_dir = tk.Button(window, text="批量识别目录中的所有文件", command=on_batch_directory)
    btn_batch_dir.pack(fill=tk.X)

    btn_batch_urls = tk.Button(window, text="批量识别在线URL", command=on_batch_urls)
    btn_batch_urls.pack(fill=tk.X)

    exit_button = tk.Button(window, text="退出程序", command=window.quit)
    exit_button.pack(fill=tk.X)

    window.mainloop()

if __name__ == "__main__":
    # 调整cli以适应GUI调用，例如可能需要调整函数使其不直接依赖于sys.exit()等。
    # 假设对cli进行了必要的调整以便在GUI环境下良好运行
    main_window()