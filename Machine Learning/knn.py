import numpy as np
import collections

def generate_dataset():
    group = np.array([[1, 101], [5, 89], [108, 5], [115, 8]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def knn(test, group, labels, k):
    dist = np.sum((test - group)**2, axis = 1)**0.5 #axis=1表示行向量相加，列数减少
    k_labels = [labels[index] for index in dist.argsort()[0:k]]
    label = collections.Counter(k_labels).most_common(1)[0][0]
    return label

if __name__ == '__main__':
    group, labels = generate_dataset()
    test = [101, 20]
    test_class = knn(test, group, labels, 3)
    print(test_class)