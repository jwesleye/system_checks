import tensorflow as tf 

def test_torch_version():
    assert tf.__version__ >= '2.9pip.0'

def test_gpu():
    assert len(tf.config.list_physical_devices('GPU')) != 0

