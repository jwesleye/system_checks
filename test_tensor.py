import tensorflow as tf 

def test_torch_version():
    assert tf.VERSION >= '2.0.0'

def test_gpu():
    assert len(tf.config.list_physical_devices('GPU')) != 0

