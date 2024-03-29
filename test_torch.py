import torch


#version
def test_torch_version():
    assert torch.__version__ >= '1.10'


def test_cuda():
    assert torch.cuda.is_available() == True


def test_gpu():
    assert torch.cuda.device_count() != 0 


def test_multiple_gpu():
    assert torch.cuda.device_count() > 1



