from typing import Tuple, Any, Union, Type

from ray.rllib.utils.annotations import DeveloperAPI, override
from ray.rllib.utils.framework import try_import_torch
from ray.rllib.models.specs.specs_base import TensorSpecs


torch, _ = try_import_torch()


@DeveloperAPI
class TorchSpecs(TensorSpecs):
    @override(TensorSpecs)
    def get_type(cls) -> Type:
        return torch.Tensor

    @override(TensorSpecs)
    def get_shape(self, tensor: torch.Tensor) -> Tuple[int]:
        return tuple(tensor.shape)

    @override(TensorSpecs)
    def get_dtype(self, tensor: torch.Tensor) -> Any:
        return tensor.dtype

    @override(TensorSpecs)
    def _full(
        self, shape: Tuple[int], fill_value: Union[float, int] = 0
    ) -> torch.Tensor:
        return torch.full(shape, fill_value, dtype=self.dtype)