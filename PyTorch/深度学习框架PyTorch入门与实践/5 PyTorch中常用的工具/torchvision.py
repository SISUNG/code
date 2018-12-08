from torchvision import models
from torch import nn

resnet34 = models.resnet34(pretrained=True, num_classes = 1000)
resnet34.fc = nn.Linear(512, 10)

from torchvision import datasets
dataset = datasets.MNIST('data/', download=True, train=False, transform=transform)

from torchvision import transforms
to_pil = transforms.ToPILImage()
to_pil(t.randn(3, 64, 64))

len(dataset)

dataloader = DataLoader(dataset, shuffle=True, batch_size = 16)

from torchvision.utils import make_grid, save_image
dataiter = iter(dataloader)
img = make_grid(next(dataiter)[0], 4)
to_img(img)

save_image(img, 'a.png')
Image.open('a.png')#读取保存的照片