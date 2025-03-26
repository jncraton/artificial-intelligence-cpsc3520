import torch
import torch.nn as nn
from torchvision import datasets, transforms


def get_loader(is_train):
    dataset = datasets.MNIST(
        root="./data",
        train=is_train,
        download=True,
        transform=transforms.ToTensor(),
    )

    return torch.utils.data.DataLoader(dataset, batch_size=64, shuffle=True)


train_loader = get_loader(is_train=True)
test_loader = get_loader(is_train=False)


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.model = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28 * 28, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 10),
        )

    def forward(self, x):
        return self.model(x)


model = Net()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

epochs = 5
for epoch in range(epochs):
    for images, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    print(f"Epoch {epoch} accuracy: {100 * correct / total:.2f}%")
