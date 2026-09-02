from mpc_engine import ShamirMPCNode, reconstruct_shamir_2_nodes


if __name__ == "__main__":
    P = 97  # Primul din studiul de caz din Anexa B

    server_A = ShamirMPCNode(node_id=1, prime=P)
    server_B = ShamirMPCNode(node_id=2, prime=P)

    # Date de intrare mascate
    # Exemplul pentru d=1 din Anexa B
    # u_1 = 3, v_1 = 5, a_1 = 6, b_1 = 7, c_1 = 42
    u1_A, u1_B = 18, 33
    v1_A, v1_B = 15, 25
    a1_A, a1_B = 16, 26
    b1_A, b1_B = 19, 31
    c1_A, c1_B = 57, 72

    # Step 1: Mascare
    dA, eA = server_A.compute_beaver_masks(
        u1_A, v1_A, a1_A, b1_A
    )
    dB, eB = server_B.compute_beaver_masks(
        u1_B, v1_B, a1_B, b1_B
    )

    # Step 2: Broadcast & reconstrucție măști d și e
    d_public = reconstruct_shamir_2_nodes(
        dA, dB, 1, 2, P
    )
    e_public = reconstruct_shamir_2_nodes(
        eA, eB, 1, 2, P
    )

    # Step 3: Evaluare poartă Beaver pe servere
    zA = server_A.evaluate_beaver_product(
        c1_A, a1_A, b1_A, d_public, e_public
    )
    zB = server_B.evaluate_beaver_product(
        c1_B, a1_B, b1_B, d_public, e_public
    )

    # Step 4: Reconstrucție produs final u_1 * v_1
    produs_reconstruit = reconstruct_shamir_2_nodes(
        zA, zB, 1, 2, P
    )

    print(
        f"[DEMO ANDREI] Resultat MPC u1 * v1: "
        f"{produs_reconstruit} (Așteptat: 15)"
    )
