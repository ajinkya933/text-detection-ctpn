# Hire me:
I can do the entire setup of this repo for you personally. If you are interested write me an email at ajinkyabobade93@gmail.com


# Text-detection-ctpn UBUNTU Implementation

***
# Setup
nms and bbox utils are written in cython, hence you have to build the library first.
```shell
cd utils/bbox
chmod +x make.sh
./make.sh
```
```
go in make.sh and replace python by python3
```

It will generate a nms.so and a bbox.so in current folder.
***
# Demo
- follow setup to build the library 
- download the ckpt file from [googl drive](https://drive.google.com/file/d/1HcZuB_MHqsKhKEKpfF1pEU85CYy4OlWO/view?usp=sharing) or [baidu yun](https://pan.baidu.com/s/1BNHt_9fiqRPGmEXPaxaFXw)
- put checkpoints_mlt/ in text-detection-ctpn/
- put your images in data/demo, the results will be saved in data/res, and run demo in the root 
```shell
python3 ./main/demo.py model_checkpoint_path checkpoints_mlt/
```

```
(tensorflow_p36) ubuntu@ip-172-31-41-142:~/ajinkya/text-detection-ctpn$ python3 ./main/demo.py model_checkpoint_path checkpoints_mlt/
WARNING:tensorflow:From /home/ubuntu/anaconda3/envs/tensorflow_p36/lib/python3.6/site-packages/tensorflow/python/framework/op_def_library.py:263: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.
Instructions for updating:
Colocations handled automatically by placer.
WARNING:tensorflow:From /home/ubuntu/ajinkya/text-detection-ctpn/nets/model_train.py:30: LSTMCell.__init__ (from tensorflow.python.ops.rnn_cell_impl) is deprecated and will be removed in a future version.
Instructions for updating:
This class is equivalent as tf.keras.layers.LSTMCell, and will be replaced by that in Tensorflow 2.0.
WARNING:tensorflow:From /home/ubuntu/ajinkya/text-detection-ctpn/nets/model_train.py:33: bidirectional_dynamic_rnn (from tensorflow.python.ops.rnn) is deprecated and will be removed in a future version.
Instructions for updating:
Please use `keras.layers.Bidirectional(keras.layers.RNN(cell))`, which is equivalent to this API
WARNING:tensorflow:From /home/ubuntu/anaconda3/envs/tensorflow_p36/lib/python3.6/site-packages/tensorflow/python/ops/rnn.py:443: dynamic_rnn (from tensorflow.python.ops.rnn) is deprecated and will be removed in a future version.
Instructions for updating:
Please use `keras.layers.RNN(cell)`, which is equivalent to this API
Restore from checkpoints_mlt/ctpn_50000.ckpt
WARNING:tensorflow:From /home/ubuntu/anaconda3/envs/tensorflow_p36/lib/python3.6/site-packages/tensorflow/python/training/saver.py:1272: checkpoint_exists (from tensorflow.python.training.checkpoint_management) is deprecated and will be removed in a future version.
Instructions for updating:
Use standard file APIs to check for files with this prefix.
Find 5 images
===============
data/demo/006.jpg
cost time: 7.82s
===============
data/demo/008.jpg
cost time: 1.04s
===============
data/demo/010.png
cost time: 3.53s
===============
data/demo/009.jpg
cost time: 0.92s
===============
data/demo/007.jpg
cost time: 4.08s


```
***
# training

## prepare data
- download labelimg software and label the data
- Go to 'label_img_to_input_data' folder and use
```
python3 denormalise-multi.py
```
- This script converts all your custom labelled xml files into the format necessary for training this model
- Download the pre-trained model of VGG net and put it in data/vgg_16.ckpt. you can download it from [tensorflow/models](https://github.com/tensorflow/models/tree/1af55e018eebce03fb61bba9959a04672536107d/research/slim)
- Optionally you can also, download the dataset we prepared from [google drive](https://drive.google.com/file/d/1npxA_pcEvIa4c42rho1HgnfJ7tamThSy/view?usp=sharing) or [baidu yun](https://pan.baidu.com/s/1nbbCZwlHdgAI20_P9uw9LQ). put the downloaded data in data/dataset/mlt, then start the training. 
- Modify the DATA_FOLDER and OUTPUT in utils/prepare/split_label.py according to your dataset. And run split_label.py in the root
```shell
python3 ./utils/prepare/split_label.py
```
- it will generate the prepared data in data/dataset/output folder
- The input file format demo of split_label.py can be found in [gt_img_859.txt](https://github.com/eragonruan/text-detection-ctpn/blob/banjin-dev/data/readme/gt_img_859.txt). And the output file of split_label.py is [img_859.txt](https://github.com/eragonruan/text-detection-ctpn/blob/banjin-dev/data/readme/img_859.txt). A demo image of the prepared data is shown below.
<img src="/data/readme/demo_split.png" width=640 height=480 />

***
## train 
Simplely run
```shell
python3 ./main/train.py
```
- The model provided in checkpoints_mlt is trained on GTX1070 for 50k iters. It takes about 0.25s per iter. So it will takes about 3.5 hours to finished 50k iterations.
***
# some results
`NOTICE:` all the photos used below are collected from the internet. If it affects you, please contact me to delete them.
<img src="/data/res/006.jpg" width=320 height=480 /><img src="/data/res/008.jpg" width=320 height=480 />
<img src="/data/res/009.jpg" width=320 height=480 /><img src="/data/res/010.png" width=320 height=320 />
***
## oriented text connector
- oriented text connector has been implemented, i's working, but still need futher improvement.
- left figure is the result for DETECT_MODE H, right figure for DETECT_MODE O
<img src="/data/res/007.jpg" width=320 height=240 /><img src="/data/res_oriented/007.jpg" width=320 height=240 />
<img src="/data/res/008.jpg" width=320 height=480 /><img src="/data/res_oriented/008.jpg" width=320 height=480 />
***
