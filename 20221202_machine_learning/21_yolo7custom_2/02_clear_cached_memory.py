import torch
# torch.cuda.empty_cache()


# pip install GPUtil
# from GPUtil import showUtilization as gpu_usage
# gpu_usage()

# max_split_size_mb
# Default value is unlimited, i.e. all blocks can be split.
# The memory_stats() and memory_summary() methods are useful for tuning

### set 'PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:512'

#     import os
# os.environ["PYTORCH_CUDA_ALLOC_CONF"] = 'max_split_size_mb:<enter-size-here>
# ref https://pytorch.org/docs/stable/notes/cuda.html#memory-management

torch.cuda.current_device()
