"""
#第一种情况，所有图片放在一个文件夹内，另外有一个TXT文件显示标签
#第一步：前期工程，生成图片路径和标签的txt文件
import torch
import torchvision  #models;datasets;transforms;
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

mnist_test = torchvision.datasets.MNIST(
    './mnist', train=False, download=True
)
print(len(mnist_test))
img, label = mnist_test[0]
img.show()

f=open('mnist_test.txt','w')

for i,(img,label) in enumerate(mnist_test):
    img_path=os.path.join("./mnist_test/"+str(i)+".jpg")

    cv2.imwrite(img_path, np.array(img))

    int_label = str(label).replace('tensor(', '')
    int_label = int_label.replace(')', '')

    f.write(img_path+' '+str(int_label)+'\n')
f.close()
"""

"""

"""
#第二步：自定义了MyDataset, 继承自torch.utils.data.Dataset。然后利用torch.utils.data.DataLoader将整个数据集分成多个批次。
from torchvision import transforms, utils
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt
from PIL import Image


def default_loader(path):
    return Image.open(path).convert('RGB')


class MyDataset(Dataset):
    def __init__(self, txt, transform=None, target_transform=None, loader=default_loader):
        fh = open(txt, 'r')
        imgs = []
        for line in fh:
            line = line.strip('\n')
            line = line.rstrip()
            words = line.split()
            imgs.append((words[0],int(words[1])))
        self.imgs = imgs
        self.transform = transform
        self.target_transform = target_transform
        self.loader = loader

    def __getitem__(self, index):
        fn, label = self.imgs[index]
        img = self.loader(fn)
        if self.transform is not None:
            img = self.transform(img)
        return img,label

    def __len__(self):
        return len(self.imgs)

train_data=MyDataset(txt='mnist_test.txt', transform=transforms.ToTensor())
data_loader = DataLoader(train_data, batch_size=100,shuffle=True)
print(len(data_loader))


def show_batch(imgs):
    grid = utils.make_grid(imgs)
    plt.imshow(grid.numpy().transpose((1, 2, 0)))
    plt.title('Batch from dataloader')


for i, (batch_x, batch_y) in enumerate(data_loader):
    if(i<4):
        print(i, batch_x.size(),batch_y.size())
        show_batch(batch_x)
        plt.axis('off')
        plt.show()

"""
#第二种情况，不同类别的图片放在不同的文件夹内，文件夹就是图片的类别
#torchvision.datasets.ImageFolder
#torch.utils.data.DataLoader

import torch
import torchvision
from torchvision import transforms, utils
import matplotlib.pyplot as plt

img_data = torchvision.datasets.ImageFolder('D:/ZXS/music/animals',
                                            transform=transforms.Compose([
                                                transforms.Scale(256),
                                                transforms.CenterCrop(224),
                                                transforms.ToTensor()])
                                            )

print(len(img_data))
data_loader = torch.utils.data.DataLoader(img_data, batch_size=10,shuffle=True)
print(len(data_loader))


def show_batch(imgs):
    grid = utils.make_grid(imgs,nrow=5)
    plt.imshow(grid.numpy().transpose((1, 2, 0)))
    plt.title('Batch from dataloader')


for i, (batch_x, batch_y) in enumerate(data_loader):
    if(i<4):
        print(i, batch_x.size(), batch_y.size())

        show_batch(batch_x)
        plt.axis('off')
        plt.show()
"""


