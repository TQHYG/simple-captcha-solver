import os
import sys
import ddddocr
from PIL import Image
import numpy as np

def solve_captcha(image_path):
    try:
        # 保存原stdout
        original_stdout = sys.stdout
        # 打开os.devnull作为新的stdout
        sys.stdout = open(os.devnull, 'w')

        # 初始化DdddOcr对象
        ocr = ddddocr.DdddOcr()

        # 恢复原stdout
        sys.stdout = original_stdout
        # 打开图片
        with open(image_path, 'rb') as image:
            img_bytes = image.read()
        captcha_text = ocr.classification(img_bytes)
        return captcha_text,0
    except Exception as e:
        # 打印错误日志
        error_log = f"错误发生：{e}"
        # 返回 NaN
        try:
            import numpy as np
            return np.nan,error_log
        except ImportError:
            return float('nan'),error_log