from . import architectures
from . import callbacks
from . import objectives
from ._discriminative import DCCA, DCCA_NOI, BarlowTwins, DCCA_SDL, DTCCA
from ._generative import DVCCA, SplitAE, DCCAE

__all__ = [
    "DCCA",
    "DCCAE",
    "DCCA_NOI",
    "DCCA_SDL",
    "DVCCA",
    "BarlowTwins",
    "DTCCA",
    "SplitAE",
    "architectures",
    "objectives",
    "callbacks",
]

classes = [
    "DCCA",
    "DCCAE",
    "DCCA_NOI",
    "DCCA_SDL",
    "DVCCA",
    "BarlowTwins",
    "DTCCA",
    "SplitAE",
]
