# licenta-criptografie-ai-mpc

Prototip pentru Privacy-Preserving Machine Learning folosind Multi-Party Computation

## Descriere

În cadrul acestui proiect am realizat un prototip prin care am urmărit să arăt cum pot fi efectuate anumite calcule asupra unor date fără ca valorile inițiale să fie transmise direct unui singur server. Pentru aceasta am folosit tehnici de secret sharing de tip Shamir și protocolul Beaver pentru multiplicarea valorilor în cadrul unui calcul MPC.

Implementarea este realizată în Python și folosește operații modulo un număr prim pentru lucrul în corpul finit. Codul din acest repository reprezintă partea demonstrativă a implementării prezentate în lucrarea de licență.

## Structura proiectului

Proiectul conține trei fișiere principale:

- `finite_field.py` conține clasa pentru efectuarea operațiilor aritmetice în corpul finit.
- `mpc_engine.py` conține componentele folosite pentru calculul MPC, inclusiv calculul măștilor Beaver și reconstrucția secretului.
- `main_demo.py` conține exemplul numeric folosit pentru demonstrarea protocolului.

## Exemplul folosit

Pentru demonstrație am folosit un exemplu simplificat cu o singură componentă. Valorile inițiale sunt `u₁ = 3` și `v₁ = 5`, iar scopul este obținerea produsului `u₁ · v₁`.

În loc ca valorile să fie transmise direct, acestea sunt reprezentate prin shares distribuite între două noduri, Server A și Server B. În calcul sunt folosite și valorile `a₁ = 6`, `b₁ = 7` și `c₁ = 42`, care formează tripla Beaver utilizată pentru multiplicare.

Pentru exemplul ales, rezultatul calculului este:

`3 · 5 = 15`

Valoarea este reconstruită la final din shares.

## Cum se rulează

Pentru rularea demonstrației este necesară instalarea Python. Din directorul proiectului se poate executa următoarea comandă:

```bash
python main_demo.py
```

Programul afișează rezultatul calculului și valoarea așteptată:

```text
[DEMO ANDREI] Resultat MPC u1 * v1: 15 (Așteptat: 15)
```

## Limitări

Codul prezent în acest repository este o demonstrație simplificată a mecanismului MPC și nu reprezintă o implementare completă a unui sistem de recomandare. Exemplul folosește două noduri și o singură componentă, pentru ca pașii calculului să poată fi urmăriți mai ușor. În lucrare este prezentat modelul general și modul în care aceste tehnici pot fi folosite în contextul Privacy-Preserving Machine Learning.
