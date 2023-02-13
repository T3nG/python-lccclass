import dlib
print(dlib.DLIB_USE_CUDA)
# True => 才表示有讀取到GPU

print(dlib.cuda.get_num_devices())  # 1

# 若 dlib.DLIB_USE_CUDA 為 False
# 有可能 cuda沒裝, 且 dlib > 19.21.0, 或 CMake版本問題, 降版本試試 3.24 ~ 3.25
