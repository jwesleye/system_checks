try:
    import torch
    if torch.cuda.is_available():
        gpu_device_count = torch.cuda.device_count()
        print("GPU devices available: %d" % gpu_device_count)
        for c in range(0, gpu_device_count):
            print(torch.cuda.get_device_name(device=c), torch.cuda.get_device_capability(device=c))
    else:
        print("CPU only")
except Exception as e:
    print(e)



