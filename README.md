# licenta-criptografie-ai-mpc

Prototip Python pentru Privacy-Preserving Machine Learning (PPML) folosind Multi-Party Computation (MPC).

## Descriere

Acest repository conține partea demonstrativă a implementării realizate pentru lucrarea de licență:

„Criptografie pentru Inteligența Artificială: Calcul securizat prin Multi-Party Computation (MPC)”

Scopul proiectului este demonstrarea modului în care anumite operații pot fi efectuate asupra unor date reprezentate prin fragmente criptografice, fără ca valorile inițiale să fie transmise direct unui singur server.

Implementarea folosește:

- Secret Sharing Shamir în configurație (2,3);
- operații aritmetice într-un corp finit F_p;
- triplete Beaver pentru efectuarea multiplicărilor;
- interpolare Lagrange pentru reconstruirea rezultatului.

Prototipul este implementat în Python și este destinat demonstrării mecanismului matematic și a pașilor principali ai calculului MPC.

## Structura proiectului

Repository-ul conține următoarele fișiere:

licenta-criptografie-ai-mpc/

     README.md
     finite_field.py
     mpc_engine.py
     main_demo.py

## finite_field.py

Conține clasa FiniteFieldElement, utilizată pentru efectuarea operațiilor aritmetice în corpul finit F_p.

Sunt implementate:

- adunarea;
- scăderea;
- înmulțirea;
- inversul multiplicativ;
- împărțirea.

## mpc_engine.py

Conține componentele principale utilizate în demonstrația MPC:

- clasa ShamirMPCNode;
- calcularea măștilor Beaver;
- evaluarea produsului Beaver;
- calcularea coeficienților Lagrange;
- reconstruirea unui secret folosind două fragmente Shamir.

## main_demo.py

Conține demonstrația numerică propriu-zisă.

În acest fișier sunt definite valorile de intrare, fragmentele Shamir și tripletele Beaver, iar apoi sunt executați pașii necesari pentru obținerea și verificarea rezultatului final.

## Exemplul utilizat

Demonstrația folosește corpul finit:

F_97

și trei servere logice:

Server A
Server B
Server C

Schema utilizată este Shamir (2,3), ceea ce înseamnă că sunt suficiente două fragmente pentru reconstruirea unui secret.

În demonstrația curentă, Server C este considerat temporar offline, iar calculul este realizat folosind fragmentele disponibile la Serverele A și B.

Datele de intrare sunt doi vectori:

u = (3, 4)
v = (5, 2)

## Produsul scalar calculat este:

u · v = 3 * 5 + 4 * 2 = 23

Pentru fiecare componentă este utilizat câte un triplet Beaver.

Pentru prima componentă:

(a1, b1, c1) = (6, 7, 42)

unde:

c1 = a1 * b1 = 42

Pentru a doua componentă:

(a2, b2, c2) = (4, 9, 36)

unde:

c2 = a2 * b2 = 36

Pentru fiecare multiplicare sunt calculate valorile mascate:

d = x - a
e = y - b

iar apoi se utilizează formula Beaver:

z = c + d*b + e*a + d*e

Operațiile sunt efectuate modulo 97.

La final, fragmentele rezultatului sunt reconstruite prin interpolare Lagrange folosind două fragmente.

Rezultatul calculului MPC este:

23

iar calculul direct este:

3 * 5 + 4 * 2 = 23

Cele două rezultate coincid.

## Semnificația datelor de intrare

Vectorii utilizați în demonstrație reprezintă date numerice asupra cărora se efectuează produsul scalar:

u = (3, 4)
v = (5, 2)

Aceste valori nu sunt introduse printr-o interfață grafică sau printr-o conexiune de rețea. Ele sunt definite direct în main_demo.py, deoarece repository-ul are rolul de a demonstra mecanismul matematic al protocolului.

Valorile sunt reprezentate prin fragmente Shamir înainte de efectuarea calculului MPC.

## Modul de interacțiune cu programul

Programul este rulat din linia de comandă prin fișierul main_demo.py.

La rulare sunt executați, în ordine, principalii pași ai demonstrației:

1. inițializarea celor trei noduri logice MPC;
2. utilizarea fragmentelor Shamir pentru datele de intrare;
3. calcularea măștilor Beaver;
4. reconstruirea valorilor mascate necesare protocolului;
5. evaluarea locală a produselor Beaver;
6. combinarea fragmentelor rezultatului;
7. reconstruirea rezultatului final folosind două fragmente;
8. compararea rezultatului MPC cu rezultatul calculat direct.

Programul verifică automat corectitudinea rezultatului prin instrucțiunea assert.

## Cum se rulează

Este necesară instalarea Python 3.

Proiectul nu necesită biblioteci externe.

Din directorul repository-ului se execută:

python main_demo.py

Rezultatul așteptat este:

[DEMO ANDREI]
Rezultat MPC:    23
Rezultat direct: 23
Verificare: OK

## Limitări

Repository-ul reprezintă un prototip didactic și nu o implementare completă a unui sistem PPML distribuit.

Implementarea actuală:

- demonstrează calculul securizat al unui produs scalar;
- utilizează secret sharing Shamir (2,3);
- utilizează triplete Beaver pentru multiplicare;
- utilizează interpolarea Lagrange pentru reconstruirea rezultatului;
- execută demonstrația local, într-un singur proces Python;
- modelează trei noduri logice MPC;
- poate efectua demonstrația folosind două noduri active, în timp ce al treilea este considerat offline;
- nu implementează comunicație reală între servere;
- nu implementează comunicație TCP/IP;
- nu implementează execuție asincronă asyncio;
- nu reprezintă un sistem complet de recomandare;
- nu implementează un mecanism complet de selecție Top-K în domeniul secret;
- nu implementează direct calculul complet al similarității cosinus, inclusiv normele și radicalii.

Extinderea prototipului către un sistem distribuit real și integrarea completă într-o aplicație de recomandare reprezintă direcții de dezvoltare ulterioară.

## Relația cu lucrarea de licență

Codul din acest repository corespunde demonstrației practice prezentate în lucrarea de licență.

Exemplul numeric principal utilizează:

p = 97
u = (3, 4)
v = (5, 2)

iar rezultatul verificat este:

u · v = 23

În demonstrația numerică sunt utilizate direct valori întregi în F_97. Factorul de scalare cu punct fix prezentat în descrierea generală a metodei nu este utilizat în acest exemplu.

Scopul repository-ului este reproducerea experimentului matematic și verificarea implementării Python descrise în lucrare.
