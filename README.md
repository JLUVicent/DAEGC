# DAEGC运行步骤

[toc]

疫情期间：目前是在个人PC上搭建了DAEGC的环境并能够跑通，现将过程记录如下以备以后使用

> 个人PC：windows10，python3.7，1050Ti,cuda 11.2

## 1.首先查看自己的GPU版本和cuda版本

```shell
nvidia-smi
```

![image](https://cdn.jsdelivr.net/gh/JLUVicent/picx_imagesaving@master/20211103/image.5kaj9p5erdc0.webp)

## 2.可以看到我的cuda版本为11.2因此安装对应版本torch

```shell
pip install torch==1.7.0+cu110 torchvision==0.8.1+cu110 -f https://download.pytorch.org/whl/torch_stable.html
```

## 3.安装`torch-scatter,torch-sparse,torch-cluster,torch-spline-conv`

我是直接通过`wheel`文件安装，个人感觉这种安装方式最直接，而且不会有什么问题，直接去[whl地址](https://pytorch-geometric.com/whl/)根据对应的`torch,cuda,以及python版本`下载对应的`wheel`文件，比如我是`cuda110+torch1.7.0+python37`，根据电脑系统选择win还是linux

![image](https://cdn.jsdelivr.net/gh/JLUVicent/picx_imagesaving@master/20211103/image.6yfrvieohxc0.webp)

![image](https://cdn.jsdelivr.net/gh/JLUVicent/picx_imagesaving@master/20211103/image.4nzdogbxaas0.webp)

## 4.cd到已经下载文件的目录

```shell
pip install +下载的包名
#如：pip install .\torch_cluster-1.5.9-cp37-cp37m-win_amd64.whl
#依次将四个都运行
```

## 5.安装`torch-geometric`

```shell
pip install torch-geometric
```

## 6.安装`DAEGC`所需要的包

```shell
pip install munkres
pip install -U scikit-learn #-U表示更新到最新版本
```

## 7.至此环境搭建完成，`cd`到`DAEGC`目录下

### 预训练（Cora,Citeseer）：

```shell
 python pretrain.py --name Cora --max_epoch 50  #预训练
 python pretrain.py --name Citeseer --max_epoch 50 #预训练
```

![image](https://cdn.jsdelivr.net/gh/JLUVicent/image-saving@master/20210731/image.639ryz1wezk0.webp)

### 训练（Cora Citeseer）：

```shell
 python daegc.py --update_interval 5 --name Cora --epoch 45 --max_epoch 200 #训练（--epoch是可变参数，根据预训练文件夹下的内容可以改变）
 python daegc.py --update_interval 5 --name Citeseer --epoch 45 --max_epoch 200 #训练
```

## 参考链接：

[Colab Notebook](https://colab.research.google.com/drive/1q2LBRiUqHgtyk2QMa3fy7kPZdbso8ilA?usp=sharing)

## 原论文：

 [Attributed Graph Clustering: A Deep Attentional Embedding Approach](https://www.ijcai.org/Proceedings/2019/0509.pdf)
