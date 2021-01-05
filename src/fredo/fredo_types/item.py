from __future__ import annotations
from typing import TypedDict, Union, Optional


class ItemMust(TypedDict):
    title: str
    command: Union[str, int, list, tuple]


class Item(ItemMust, total=False):
    subtitle: Optional[str]
