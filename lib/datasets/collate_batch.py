from torch.utils.data.dataloader import default_collate
import torch
import numpy as np
from lib.config import cfg


def none_collate(batch):
    return batch[0]

_collators = {
    'none': none_collate,
}

def make_collator(cfg, is_train):
    collator = cfg.train.collator if is_train else cfg.test.collator
    if collator in _collators:
        return _collators[collator]
    else:
        return default_collate
