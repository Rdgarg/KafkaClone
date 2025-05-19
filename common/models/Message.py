from dataclasses import dataclass
from typing import Optional


@dataclass(unsafe_hash=True)
class Message:
    value : str
    key : Optional[str]
    timestamp : Optional[int]
    headers : Optional[dict[str, str]]