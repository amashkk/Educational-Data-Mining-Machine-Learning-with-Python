"""
DCT 影像壓縮預處理

用於減少振鈴失真的 DCT 影像壓縮選擇性預處理方法。

參考論文：
M. Oizumi, "Preprocessing method for DCT-based image-compression," 
IEEE Transactions on Consumer Electronics, vol. 52, no. 3, pp. 1021-1026, Aug. 2006.
DOI: 10.1109/TCE.2006.1706502
"""

from .preprocessors import DCTPreprocessorFixed, DCTPreprocessorAdaptive, UniformPreprocessor
from .compressor import DCTCompressor
from .metrics import calculate_psnr, calculate_ssim, calculate_edge_preservation, calculate_texture_preservation, calculate_sharpness
from .utils import rgb_to_yuv, yuv_to_rgb

__version__ = '1.0.0'
__author__ = '孔祥庭, 王翊丞'

__all__ = [
    'DCTPreprocessorFixed',
    'DCTPreprocessorAdaptive', 
    'UniformPreprocessor',
    'DCTCompressor',
    'calculate_psnr',
    'calculate_ssim',
    'calculate_edge_preservation',
    'calculate_texture_preservation',
    'calculate_sharpness',
    'rgb_to_yuv',
    'yuv_to_rgb',
]
