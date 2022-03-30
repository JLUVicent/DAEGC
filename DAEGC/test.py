from torch_geometric.datasets import Planetoid


def get_dataset(dataset):
    datasets = Planetoid('./dataset', dataset)
    return datasets


datasets = get_dataset("Cora")
dataset = datasets[0]
input_dim = dataset.num_features
