```shell
 python pretrain.py --name Cora --max_epoch 50  #预训练
 python pretrain.py --name Citeseer --max_epoch 50 #预训练
 python daegc.py --update_interval 5 --name Cora --epoch 45 --max_epoch 200 #训练（--epoch是可变参数，根据预训练文件夹下的内容可以改变）
 python daegc.py --update_interval 5 --name Citeseer --epoch 45 --max_epoch 200 #训练
```

