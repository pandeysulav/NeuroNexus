import tensorflow as tf

# Check TensorFlow version
print("TensorFlow version:", tf.__version__)

# List available GPUs
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print("GPUs detected:", len(gpus))
    for gpu in gpus:
        print(" -", gpu)
else:
    print("No GPU detected. TensorFlow is running on CPU.")
