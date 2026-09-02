from mpc_engine import ShamirMPCNode, reconstruct_shamir_2_of_3


if __name__ == "__main__":
    # Corpul finit F_97
    P = 97

    # Initializarea celor trei servere MPC
    server_A = ShamirMPCNode(node_id=1, prime=P)
    server_B = ShamirMPCNode(node_id=2, prime=P)
    server_C = ShamirMPCNode(node_id=3, prime=P)

    # Datele utilizatorului:
    # u = (3, 4)
    # v = (5, 2)
    #
    # Produsul scalar:
    # u * v = 3 * 5 + 4 * 2 = 23

    # Fragmente Shamir pentru u1 = 3
    u1_A, u1_B, u1_C = 18, 33, 48

    # Fragmente Shamir pentru u2 = 4
    u2_A, u2_B, u2_C = 24, 44, 64

    # Fragmente Shamir pentru v1 = 5
    v1_A, v1_B, v1_C = 15, 25, 35

    # Fragmente Shamir pentru v2 = 2
    v2_A, v2_B, v2_C = 10, 18, 26

    # Triplet Beaver pentru prima componenta:
    # a1 = 6, b1 = 7, c1 = 42
    a1_A, a1_B, a1_C = 16, 26, 36
    b1_A, b1_B, b1_C = 19, 31, 43
    c1_A, c1_B, c1_C = 57, 72, 87

    # Triplet Beaver pentru a doua componenta:
    # a2 = 4, b2 = 9, c2 = 36
    a2_A, a2_B, a2_C = 9, 14, 19
    b2_A, b2_B, b2_C = 12, 15, 18
    c2_A, c2_B, c2_C = 43, 50, 57

    # Serverele A si B calculeaza mastile pentru prima componenta
    d1_A, e1_A = server_A.compute_beaver_masks(u1_A, v1_A, a1_A, b1_A)
    d1_B, e1_B = server_B.compute_beaver_masks(u1_B, v1_B, a1_B, b1_B)

    # Serverele A si B calculeaza mastile pentru a doua componenta
    d2_A, e2_A = server_A.compute_beaver_masks(u2_A, v2_A, a2_A, b2_A)
    d2_B, e2_B = server_B.compute_beaver_masks(u2_B, v2_B, a2_B, b2_B)

    # Serverul C este temporar offline.
    # Schema Shamir (2,3) permite reconstructia folosind A si B.

    # Reconstructia publica a mastilor pentru prima componenta
    d1_public = reconstruct_shamir_2_of_3(d1_A, 1, d1_B, 2, P)
    e1_public = reconstruct_shamir_2_of_3(e1_A, 1, e1_B, 2, P)

    # Reconstructia publica a mastilor pentru a doua componenta
    d2_public = reconstruct_shamir_2_of_3(d2_A, 1, d2_B, 2, P)
    e2_public = reconstruct_shamir_2_of_3(e2_A, 1, e2_B, 2, P)

    # Evaluarea produsului Beaver pentru prima componenta
    z1_A = server_A.evaluate_beaver_product(c1_A, a1_A, b1_A, d1_public, e1_public)
    z1_B = server_B.evaluate_beaver_product(c1_B, a1_B, b1_B, d1_public, e1_public)

    # Evaluarea produsului Beaver pentru a doua componenta
    z2_A = server_A.evaluate_beaver_product(c2_A, a2_A, b2_A, d2_public, e2_public)
    z2_B = server_B.evaluate_beaver_product(c2_B, a2_B, b2_B, d2_public, e2_public)

    # Adunarea fragmentelor pentru produsul scalar
    score_A = (z1_A + z2_A) % P
    score_B = (z1_B + z2_B) % P

    # Reconstructia rezultatului final
    rezultat_mpc = reconstruct_shamir_2_of_3(score_A, 1, score_B, 2, P)

    # Calcul direct pentru verificare
    rezultat_direct = (3 * 5 + 4 * 2) % P

    # Afisarea rezultatelor
    print("[DEMO ANDREI]")
    print(f"Rezultat MPC:    {rezultat_mpc}")
    print(f"Rezultat direct: {rezultat_direct}")

    # Verificarea corectitudinii
    assert rezultat_mpc == rezultat_direct
    assert rezultat_mpc == 23

    print("Verificare: OK")
