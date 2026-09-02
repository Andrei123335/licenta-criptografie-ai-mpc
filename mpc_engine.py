from typing import Tuple


class ShamirMPCNode:
    """Nod MPC care executa operatia Beaver pe fragmente Shamir."""

    def __init__(self, node_id: int, prime: int):
        if node_id not in (1, 2, 3):
            raise ValueError("node_id trebuie sa fie 1, 2 sau 3.")

        if prime <= 1:
            raise ValueError(
                "Modulul trebuie sa fie un numar intreg mai mare decat 1."
            )

        self.node_id = node_id
        self.prime = prime

    def compute_beaver_masks(self, x_share: int, y_share: int, a_share: int, b_share: int) -> Tuple[int, int]:
        """
        Calculeaza local mastile:
        d_i = x_i - a_i
        e_i = y_i - b_i
        """

        d_share = (x_share - a_share) % self.prime
        e_share = (y_share - b_share) % self.prime

        return d_share, e_share

    def evaluate_beaver_product(self, c_share: int, a_share: int, b_share: int, d_public: int, e_public: int) -> int:
        """
        Calculeaza fragmentul rezultatului Beaver:
        z = c + d*b + e*a + d*e
        """

        term_c = c_share % self.prime
        term_db = (d_public * b_share) % self.prime
        term_ea = (e_public * a_share) % self.prime
        term_de = (d_public * e_public) % self.prime

        return (term_c + term_db + term_ea + term_de) % self.prime


def lagrange_coefficient_at_zero(x_i: int, x_j: int, prime: int) -> int:
    """
    Calculeaza coeficientul Lagrange pentru reconstructia
    secretului in punctul x = 0 folosind doua fragmente.
    """

    numerator = (-x_j) % prime
    denominator = (x_i - x_j) % prime

    if denominator == 0:
        raise ZeroDivisionError(
            "Punctele Shamir trebuie sa fie distincte."
        )

    denominator_inverse = pow(denominator, prime - 2, prime)

    return (numerator * denominator_inverse) % prime


def reconstruct_shamir_2_of_3(share_1: int, x_1: int, share_2: int, x_2: int, prime: int) -> int:
    """
    Reconstruieste secretul din oricare doua fragmente
    ale schemei Shamir (2,3).
    """

    if x_1 == x_2:
        raise ValueError(
            "Punctele de interpolare trebuie sa fie distincte."
        )

    lambda_1 = lagrange_coefficient_at_zero(x_1, x_2, prime)
    lambda_2 = lagrange_coefficient_at_zero(x_2, x_1, prime)

    return (share_1 * lambda_1 + share_2 * lambda_2) % prime
