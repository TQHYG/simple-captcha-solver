import os
import sys
import requests
import shutil
from urllib.parse import urlparse
from captcha_solver import solve_captcha  
import argparse

def get_system_language():
    """获取系统语言"""
    if 'win' in sys.platform.lower():
        import ctypes
        windll = ctypes.windll.kernel32
        language = hex(windll.GetUserDefaultUILanguage())
        return 'zh' if language.startswith('0x804') else 'en'
    elif 'linux' in sys.platform.lower() or 'darwin' in sys.platform.lower():
        import locale
        language_code = locale.getdefaultlocale()[0]
        return 'zh' if 'zh' in language_code else 'en'
    return 'en'

def preprocess_user_input(user_input):
    """
    预处理用户输入，去除首尾可能存在的空格和引号。
    
    参数:
        user_input (str): 用户提供的原始输入。
    
    返回:
        str: 清理后的输入字符串。
    """
    # 去除首尾的空白字符
    user_input = user_input.strip()
    
    # 如果同时存在首尾的单引号或双引号，则去除它们
    if (user_input.startswith('"') and user_input.endswith('"')) or \
       (user_input.startswith("'") and user_input.endswith("'")):
        user_input = user_input[1:-1]
    
    return user_input.strip()  # 再次去除可能由于引号去除而产生的额外空白

def download_image(url, filename):
    """从给定的URL下载图片"""
    try:
        response = requests.get(url, stream=True)
        # 检查状态码是否表示请求成功
        if response.status_code == 200:
            # 使用上下文管理器确保文件正确写入并关闭
            with open(filename, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
        else:
            print(f"Failed to download image: HTTP {response.status_code}")
    except requests.RequestException as e:
        # 处理所有类型的请求异常
        print(f"Failed to download image: {str(e)}")
    finally:
        # 确保即使发生错误也释放响应对象
        response.close()

def copy_file(src, dst):
    """复制文件到目标位置，如果目标文件存在则覆盖"""
    shutil.copyfile(src, dst)

def clear_cache():
    """清空缓存目录中的内容，但不删除目录本身"""
    global cache_dir
    for filename in os.listdir(cache_dir):
        file_path = os.path.join(cache_dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

def show_menu():
    global lang
    menu_text = "请选择要执行的操作：\n1. 识别单个文件或URL\n2. 批量识别目录中的所有文件\n3. 批量识别在线URL\n4. 退出程序" if lang == 'zh' else "Please choose an operation:\n1. Identify a single file or URL\n2. Batch recognize all files in a directory\n3. Batch recognize online URLs\n4. Exit the program"
    print(menu_text)

def resolve_single(file_url):
    global cache_dir
    global lang
    parsed_url = urlparse(file_url)
    ext = os.path.splitext(parsed_url.path)[1] if len(os.path.splitext(parsed_url.path)[1]) > 0 else '.jpg'
    local_filename = os.path.join(cache_dir, f"captcha{ext}")
    if parsed_url.scheme and parsed_url.netloc:
        try:
            download_image(file_url, local_filename)
            print("Image downloaded successfully." if lang == 'en' else "图片下载成功。")
        except Exception as e:
            print(f"Failed to download image: {str(e)}" if lang == 'en' else f"下载图片失败: {str(e)}")
            return()
    else:
        try:
            copy_file(file_url, local_filename)
            print("File copied successfully." if lang == 'en' else "文件复制成功。")
        except Exception as e:
            print(f"Failed to copy file: {str(e)}" if lang == 'en' else f"复制文件失败: {str(e)}")
            return()

        captcha_text, error_log = solve_captcha(local_filename)
        if error_log == 0:
            print(f"The captcha text is: {captcha_text}" if lang == 'en' else f"验证码文本为：{captcha_text}")
        else:
            print(f"Error occurred during solving captcha: {error_log}" if lang == 'en' else f"解码时发生错误：{error_log}")

def batch_process_directory(directory):
    """批量处理目录中的文件"""
    global cache_dir
    global lang
    try:
        shutil.copytree(directory, os.path.join(cache_dir, 'batch'))
    except Exception as e:
        print(f"Failed to copy directory: {str(e)}" if lang == 'en' else f"复制目录失败: {str(e)}")
        return

    success, failure = 0, 0
    for filename in os.listdir(os.path.join(cache_dir, 'batch')):
        filepath = os.path.join(cache_dir, 'batch', filename)
        captcha_text, error_log = solve_captcha(filepath)
        if error_log == 0:
            print(f"{filename}: {captcha_text}")
            success += 1
        else:
            print(f"{filename}: Error - {error_log}")
            failure += 1
    
    clear_cache()
    print(f"Total: {success + failure}, Success: {success}, Failure: {failure}" if lang == 'en' else f"总共: {success + failure}, 成功: {success}, 失败: {failure}")

def batch_process_urls(url_file):
    """批量处理在线URL"""
    global lang
    global cache_dir
    with open(url_file) as f:
        urls = f.readlines()

    success, failure = 0, 0
    for url in urls:
        url = url.strip()
        parsed_url = urlparse(url)
        ext = os.path.splitext(parsed_url.path)[1] if len(os.path.splitext(parsed_url.path)[1]) > 0 else '.jpg'
        local_filename = os.path.join(cache_dir, f"captcha{ext}")

        try:
            download_image(url, local_filename)
        except Exception as e:
            print(f"Failed to download image from {url}: {str(e)}" if lang == 'en' else f"从 {url} 下载图片失败: {str(e)}")
            failure += 1
            continue
        
        captcha_text, error_log = solve_captcha(local_filename)
        if error_log == 0:
            print(f"{url}: {captcha_text}")
            success += 1
        else:
            print(f"{url}: Error - {error_log}")
            failure += 1
    
    clear_cache()
    print(f"Total URLs: {len(urls)}, Success: {success}, Failure: {failure}" if lang == 'en' else f"总共URL: {len(urls)}, 成功: {success}, 失败: {failure}")


lang = get_system_language()
cache_dir = 'pic_cache'

def main():
    global cache_dir
    global lang
    description = "验证码识别工具" if lang == 'zh' else "Captcha recognition tool"
    help_msg = "显示帮助信息并退出" if lang == 'zh' else "Show help message and exit"

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-f', type=str, help='通过提供的URL识别验证码' if lang == 'zh' else 'Identify captcha via provided URL')
    parser.add_argument('-d', type=str, help='批量识别指定目录下的所有文件' if lang == 'zh' else 'Batch recognize all files in the specified directory')
    parser.add_argument('-i', type=str, help='通过提供的文本文件中的URL批量识别验证码' if lang == 'zh' else 'Batch identify captchas via provided URLs in text file')
    
    args = parser.parse_args()

    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    if args.f:
        user_input = args.f
        parsed_url = urlparse(user_input)
        ext = os.path.splitext(parsed_url.path)[1] if len(os.path.splitext(parsed_url.path)[1]) > 0 else '.jpg'
        local_filename = os.path.join(cache_dir, f"captcha{ext}")

        if parsed_url.scheme and parsed_url.netloc:
            try:
                download_image(user_input, local_filename)
            except Exception as e:
                print(f"Failed to download image: {str(e)}" if lang == 'en' else f"下载图片失败: {str(e)}")
                sys.exit(1)
        else:
            try:
                copy_file(user_input, local_filename)
            except Exception as e:
                print(f"Failed to copy file: {str(e)}" if lang == 'en' else f"复制文件失败: {str(e)}")
                sys.exit(1)

        
        captcha_text, error_log = solve_captcha(local_filename)
        clear_cache()
        if error_log == 0:
            print(captcha_text)
            sys.exit(0)
        else:
            print(error_log)
            sys.exit(1)
    elif args.d:
        user_input = args.d
        directory = preprocess_user_input(user_input)
        batch_process_directory(directory)
    elif args.i:
        user_input = args.i
        url_file = preprocess_user_input(user_input)
        batch_process_urls(url_file)
    else:
        welcome_text = "Welcome to use the Captcha recgnition tool." if lang == 'en' else "欢迎使用验证码识别工具"
        print(welcome_text)
        while True:
            clear_cache()
            show_menu()
            choice = input(">").strip()
            if choice == '1':
                input_text = "Please input the URL or Picture file: " if lang == 'en' else "请输入要识别的图片路径或URL："
                user_input = input(input_text)
                file_url = preprocess_user_input(user_input)
                resolve_single(file_url)
            elif choice == '2':
                input_text = "Please input the directory: " if lang == 'en' else "请输入要批量识别的路径："
                user_input = input(input_text)
                directory = preprocess_user_input(user_input)
                batch_process_directory(directory)
            elif choice == '3':
                input_text = "Please input the URL file: " if lang == 'en' else "请输入要批量识别的URL文件路径："
                user_input = input(input_text)
                url_file = preprocess_user_input(user_input)
                batch_process_urls(url_file)
            elif choice == '4':
                clear_cache()
                sys.exit(0)

if __name__ == '__main__':
    main()