import torch
import torchvision
import torch.nn as nn
import torchvision.transforms as transforms

import numpy as np

# ================================= #
#   1.Basic autograd example 1      #
# ================================= #
x = torch.tensor(1., requires_grad=True)
w = torch.tensor(2., requires_grad=True)
b = torch.tensor(3., requires_grad=True)

y = w * x + b

y.backward()
print(x.grad)
print(w.grad)
print(b.grad)

# ================================= #
#   2.Basic autograd example 2      #
# ================================= #
x = torch.randn(10,3)
y = torch.randn(10,2)
linear = nn.Linear(3,2)
print('w: ', linear.weight)
print('b: ', linear.bias)

criterion = nn.MSELoss()
optimizer = torch.optim.SGD(linear.parameters(),lr=0.01)

pred = linear(x)

loss = criterion(pred, y)

print('loss: ', loss.item())

loss.backward()

print('dL/dw: ', linear.weight.grad)
print('dL/db: ', linear.bias.grad)

optimizer.step()

pred = linear(x)
loss = criterion(pred, y)
print('loss after 1 step optimization: ', loss.item())


optimizer.step()

pred = linear(x)
loss = criterion(pred, y)
print('loss after 2 step optimization: ', loss.item())

for i in range(3, 100):
    optimizer.step()

    pred = linear(x)
    loss = criterion(pred, y)
    print('loss after {} step optimization: {}'.format(
        i,
        loss.item()
    ))

#you can also perform gradient descent at the low level
#linear.weight.data.sub_(0.01 * linear.weight.grad.data)
#linear.bias.data.sub_(0.01 * linear.bias.grad.data)



# ======================================== #
#        3. Loading data from numpy        #
# ======================================== #
x = np.array([[1, 2],
              [3, 4]])
y = torch.from_numpy(x)
z = y.numpy()


# # ======================================== #
# #        4. Input pipline                  #
# # ======================================== #
# train_dataset = torchvision.datasets.CIFAR10(root='../../data/',
#                                              train=True,
#                                              transform=transforms.ToTensor(),
#                                              download=True)
# image, label = train_dataset[0]
# print(image.size())
# print(label)
#
# train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
#                                            batch_size=64,
#                                            shuffle=True)
# data_iter = iter(train_loader)
# images, labels = data_iter.next()
# for images, labels in train_loader:
#     pass
#
# # ======================================== #
# #    5. Input pipline for custom dataset   #
# # ======================================== #
# class CustomDataset(torch.utils.data.Dataset):
#     def __init__(self):
#         # TODO
#         pass
#     def __getitem__(self):
#         # TODO
#         pass
#     def __len__(self):
#         return 0
#
# custom_dataset = CustomDataset()
# train_loader = torch.utils.data.DataLoader(
#     dataset=custom_dataset,
#     batch_size=64,
#     shuffle=True)


# ======================================== #
#            6. Pretrained model           #
# ======================================== #
resnet = torchvision.models.resnet18(pretrained=True)

#if you want to finetune only the top layer of the model,set as below
for param in resnet.parameters():
    param.requires_grad = False

resnet.fc = nn.Linear(resnet.fc.in_features, 100)

#forward pass
images = torch.randn(64, 3, 224, 224)
outputs = resnet(images)
print(outputs.size())

# ======================================== #
#       7. Save and load the model         #
# ======================================== #
torch.save(resnet, 'model.ckpt')
model = torch.load('model.ckpt')

torch.save(resnet.state_dict(), 'params.ckpt')
resnet.load_state_dict(torch.load('params.ckpt'))


