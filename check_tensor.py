import tensorflow as tf 

def test_gpu():
    assert len(tf.config.list_physical_devices('GPU')) != 0

