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

def download_image(url, filename):
    """从给定的URL下载图片"""
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

def copy_file(src, dst):
    """复制文件到目标位置，如果目标文件存在则覆盖"""
    shutil.copyfile(src, dst)

def clear_cache(cache_dir):
    """清空缓存目录中的内容，但不删除目录本身"""
    for filename in os.listdir(cache_dir):
        file_path = os.path.join(cache_dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

def main():
    lang = get_system_language()
    description = "验证码识别工具" if lang == 'zh' else "Captcha recognition tool"
    help_msg = "显示帮助信息并退出" if lang == 'zh' else "Show help message and exit"

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-f', type=str, help='通过提供的URL识别验证码' if lang == 'zh' else 'Identify captcha via provided URL')
    
    args = parser.parse_args()

    cache_dir = 'pic_cache'
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
        clear_cache(cache_dir)
        if error_log == 0:
            print(captcha_text)
            sys.exit(0)
        else:
            print(error_log)
            sys.exit(1)
    else:
        welcome_text = "Please input the image URL or path:" if lang == 'en' else "请输入图片URL或路径："
        print(welcome_text)
        user_input = input().strip()
        parsed_url = urlparse(user_input)
        ext = os.path.splitext(parsed_url.path)[1] if len(os.path.splitext(parsed_url.path)[1]) > 0 else '.jpg'
        local_filename = os.path.join(cache_dir, f"captcha{ext}")

        if parsed_url.scheme and parsed_url.netloc:
            try:
                download_image(user_input, local_filename)
                print("Image downloaded successfully." if lang == 'en' else "图片下载成功。")
            except Exception as e:
                print(f"Failed to download image: {str(e)}" if lang == 'en' else f"下载图片失败: {str(e)}")
                sys.exit(1)
        else:
            try:
                copy_file(user_input, local_filename)
                print("File copied successfully." if lang == 'en' else "文件复制成功。")
            except Exception as e:
                print(f"Failed to copy file: {str(e)}" if lang == 'en' else f"复制文件失败: {str(e)}")
                sys.exit(1)

        captcha_text, error_log = solve_captcha(local_filename)
        if error_log == 0:
            print(f"The captcha text is: {captcha_text}" if lang == 'en' else f"验证码文本为：{captcha_text}")
        else:
            print(f"Error occurred during solving captcha: {error_log}" if lang == 'en' else f"解码时发生错误：{error_log}")

        clear_cache(cache_dir)

if __name__ == '__main__':
    main()