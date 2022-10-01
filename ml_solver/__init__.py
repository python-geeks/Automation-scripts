# flake8: noqa
try:
    from importlib.metadata import PackageNotFoundError, version
except ImportError:  # pragma: no cover
    from importlib_metadata import PackageNotFoundError, version

from .solver import solver, metrics_dict, models_dict

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = "0.4.0"


__author__ = "Kushagra Shukla"
__email__ = "1kuspia@gmail.com"
