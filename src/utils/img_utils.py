import numpy as np
from PIL import Image

def resize_center_crop(img, target_h: int, target_w: int):
    """
    将图像按比例缩放后进行中心裁剪到指定尺寸 (target_h, target_w)，保证不拉伸、不形变。

    参数:
        img: 输入图像，可以是 numpy.ndarray (H, W, C) 或 PIL.Image.Image
        target_h: 目标高度
        target_w: 目标宽度

    返回:
        numpy.ndarray，形状为 (target_h, target_w, C)
    """
    # 转成 PIL Image 统一处理
    if isinstance(img, np.ndarray):
        pil_img = Image.fromarray(img)
    else:
        pil_img = img

    w, h = pil_img.size

    # 先按长边缩放，使得缩放后图像可以覆盖目标尺寸，再中心裁剪
    scale = max(target_w / w, target_h / h)
    new_w = int(round(w * scale))
    new_h = int(round(h * scale))

    pil_img = pil_img.resize((new_w, new_h), Image.BILINEAR)

    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    right = left + target_w
    bottom = top + target_h

    pil_img = pil_img.crop((left, top, right, bottom))

    return np.array(pil_img)

