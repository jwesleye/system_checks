try:
    import tensorflow as tf 
    for dev in tf.config.list_physical_devices():
        print(dev)
except Exception as e:
    print(e)
