"""
fit BN_CNN models
"""
import tensorflow as tf
from deepretina.core import train
from deepretina.models import bn_cnn


if __name__ == '__main__':
    expts = ('15-10-07', '15-11-21a', '15-11-21b')
    stims = ('whitenoise', 'naturalscene')

    with tf.device('/gpu:0'):
        for expt in expts:
            for stim in stims:
                train(bn_cnn, expt, stim, lr=1e-2, nb_epochs=250, val_split=0.05)