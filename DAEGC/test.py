# from torch_geometric.datasets import Planetoid


# def get_dataset(dataset):
#     datasets = Planetoid('./dataset', dataset)
#     return datasets


# datasets = get_dataset("Cora")
# dataset = datasets[0]
# input_dim = dataset.num_features
# print(dataset)
from torch_geometric.data import Data
import torch
x = torch.tensor([[-1], [0], [1]], dtype=torch.float)
edge_index = torch.tensor([[0, 1, 1, 2],
                           [1, 0, 2, 1]], dtype=torch.long)
data = Data(x=x, edge_index=edge_index)
print(data)
