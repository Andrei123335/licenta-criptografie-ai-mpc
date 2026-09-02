import random
from typing import List, Tuple


class ShamirMPCNode:
    """Nod computațional MPC ce execută poarta de multiplicare Beaver."""

    def __init__(self, node_id: int, prime: int):
        self.node_id = node_id
        self.prime = prime

    def compute_beaver_masks(
        self,
        x_share: int,
        y_share: int,
        a_share: int,
        b_share: int
    ) -> Tuple[int, int]:
        d_share = (x_share - a_share) % self.prime
        e_share = (y_share - b_share) % self.prime
        return d_share, e_share

    def evaluate_beaver_product(
        self,
        c_share: int,
        a_share: int,
        b_share: int,
        d_pub: int,
        e_pub: int
    ) -> int:
        term1 = c_share
        term2 = (d_pub * b_share) % self.prime
        term3 = (e_pub * a_share) % self.prime
        term4 = (d_pub * e_pub) % self.prime

        z_share = (
            term1 + term2 + term3 + term4
        ) % self.prime

        return z_share


def reconstruct_shamir_2_nodes(
    s1: int,
    s2: int,
    x1: int,
    x2: int,
    prime: int
) -> int:
    l1_num = (-x2) % prime
    l1_den = pow((x1 - x2) % prime, prime - 2, prime)
    l1 = (l1_num * l1_den) % prime

    l2_num = (-x1) % prime
    l2_den = pow((x2 - x1) % prime, prime - 2, prime)
    l2 = (l2_num * l2_den) % prime

    secret = (s1 * l1 + s2 * l2) % prime
    return secret
