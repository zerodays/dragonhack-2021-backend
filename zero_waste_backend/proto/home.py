# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: home.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class GetHomeInfo(betterproto.Message):
    """type = 'get-home-info'origin = client"""

    nfc_ids: List[str] = betterproto.string_field(1)


@dataclass
class HomeInfo(betterproto.Message):
    """type = 'home-info'origin = serverclient cache = years(1)"""

    n_containers: int = betterproto.int32_field(1)
    food_g: int = betterproto.int32_field(2)
    waste_saved_g: int = betterproto.int32_field(3)
    co2_saved_g: int = betterproto.int32_field(4)
    n_rewards: int = betterproto.int32_field(5)
