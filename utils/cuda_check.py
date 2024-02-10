import torch


def get_gpu_info():
    available = torch.cuda.is_available()
    print("GPU available: ", available)
    if available == "True":
        count = torch.cuda.device_count()
        print("GPU count: ", count)
        for i in range(count):
            print("GPU ", i, ": ", torch.cuda.get_device_name(i))
    else:
        print("No GPU available")
    