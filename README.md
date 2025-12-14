# Indice generale argomenti di Analisi 1¬

## 1. Concetti di base

Cartella: `01-concetti-di-base`
 a
### 1.1 Insiemi ([appunti](01-concetti-di-base/1.1-insiemi.md))

* Concetto di insieme, elemento, appartenenza
* Insieme universo, insieme vuoto
* Sottoinsieme, inclusione `⊆`, inclusione stretta
* Uguaglianza di insiemi tramite doppia inclusione
* Operazioni: complementare, unione, intersezione, differenza, differenza simmetrica
* Prodotto cartesiano `A × B`
* Insieme delle parti `℘(A)`
* Cardinalità di un insieme finito

### 1.2 Logica delle proposizioni e dei predicati ([appunti](01-concetti-di-base/1.2-logica.md))

* Proposizioni vs predicati
* Connettivi logici: negazione, congiunzione, disgiunzione (inclusiva/esclusiva), implicazione, doppia implicazione
* Tavole di verità
* Tautologia, contraddizione
* Leggi di De Morgan (logiche)
* Quantificatori: esistenziale `∃`, universale `∀`
* Regole per negare frasi con quantificatori (scambio ∀/∃ + negazione interna)
* Modus ponens, modus tollens (schema logico delle dimostrazioni)
* Esempio classico: irrazionalità di √2 (come modello di dimostrazione per assurdo)

### 1.3 Relazioni  ([appunti](01-concetti-di-base/1.3-relazioni.md))

* Relazione su un insieme come sottoinsieme di `A × A`
* Relazioni di equivalenza: riflessiva, simmetrica, transitiva
* Classi di equivalenza, insieme quoziente `A / ~`
* Relazioni d’ordine parziale: riflessiva, antisimmetrica, transitiva
* Ordine totale (esempio `≤` su ℝ)

### 1.4 Funzioni ([appunti](01-concetti-di-base/1.4-funzioni.md))

* Definizione di funzione: dominio, codominio, legge, immagine
* Immagine di un sottoinsieme, restrizione di una funzione
* Immagine di una funzione `im(f)`
* Controimmagine (immagine inversa) di un punto e di un insieme
* Funzioni iniettive, suriettive, biiettive (biunivoche)
* Caratterizzazioni equivalenti dell’iniettività (`f(a1)=f(a2) ⇒ a1=a2`)
* Concetto di funzione inversa (come funzione definita solo se f è biiettiva)
* Composizione di funzioni

### 1.5 Insiemi numerici ([appunti](01-concetti-di-base/1.5-insiemi-numerici.md))

- 1.5.2 Funzioni elementari ([appunti](01-concetti-di-base/1.5-2-funzioni-elementari.md))
- 1.5.3 Numeri complessi ([appunti](01-concetti-di-base/1.5-3-numeri-complessi.md))

* Definizione e inclusioni tra N, Z, Q, R, C
* Operazioni algebriche di base, campo, anello, corpo
* Valore assoluto e sue proprietà (disuguaglianza triangolare, ecc.)
* Estremo superiore (sup), estremo inferiore (inf), maggiorante, minorante
* Proprietà di completezza di ℝ (ogni sottoinsieme non vuoto e limitato superiormente ha un sup)
* Intervalli e semirette: aperti, chiusi, semiaperti, illimitati

#### 1.5.2 Funzioni elementari

* Polinomi e funzioni razionali
* Potenze e radici (funzioni potenza)
* Funzione esponenziale e logaritmica (base `e`, cambi base)
* Funzioni trigonometriche: sin, cos, tan, ecc., loro proprietà di base
* Formule trigonometriche elementari (riassunte anche in appendice A) 
* Funzioni goniometriche inverse

#### 1.5.3 Numeri complessi 

* Forma algebrica `a + ib`, modulo, argomento
* Forma polare/esponenziale `re^{iθ}`
* Prodotto, quoziente, coniugato
* Formula di De Moivre, radici n-esime di un complesso
* Teorema fondamentale dell’algebra (enunciato) 

### 1.6 Principio di induzione ([appunti](01-concetti-di-base/1.6-induzione.md))

* Enunciato del principio di induzione su N
* Uso per dimostrare formule (es. binomio di Newton)
* Binomio di Newton (enunciato)

--- 

## 2. Successioni

Cartella: `02-successioni`

### 2.1 Successioni reali e loro proprietà ([appunti](02-successioni/2.1-successioni.md))

* Definizione di successione `{x_n}`
* Successioni limitate, superiormente/inferiormente limitate
* Successioni monotone (crescente, decrescente, strettamente)
* Successioni infinitesime

### 2.2 Limiti di successioni ([appunti](02-successioni/2.2-limiti.md))

* Definizione `lim_{n→∞} x_n = ℓ` (epsilon–N)
* Unicità del limite
* Algebra dei limiti (somma, prodotto, quoziente, valore assoluto)
* Confronto tra successioni (≤, <)
* Teorema dei carabinieri (squeeze)
* Disuguaglianza della permanenza del segno
* Successioni estratte (sottosuccessioni)
* Teorema di Bolzano–Weierstrass (sottosuccessione convergente da successione limitata)
* Successioni di Cauchy e criterio di convergenza di Cauchy

### 2.2.1 Limiti notevoli

* Limite `(1+1/n)^n → e`
* Limiti con `sin x / x`, `(1+x)^{1/x}`, log, esponenziali ecc.

### 2.2.2 Successioni monotone

* Teorema: successione monotona e limitata ⇒ convergente
* Altri limiti notevoli ottenuti da successioni monotone

### 2.2.3 Caratterizzazione delle successioni convergenti 

* Equivalenze: convergenza ↔ Cauchy ↔ tutte le sottosuccessioni hanno stesso limite

--- 

## 3. Funzioni reali di variabile reale: limiti e continuità

Cartella: `03-limiti-continuita`

### 3.1 Limiti di funzioni ([appunti](03-limiti-continuita/3.1-limiti-funzioni.md))

* Definizione di limite finito in un punto (epsilon–delta)
* Limiti laterali, limiti infiniti, limiti all’infinito
* Caratterizzazione sequenziale del limite (Teorema: limite ⇔ limiti lungo tutte le successioni che tendono al punto)
* Algebra dei limiti di funzioni (teoremi algebrici) 
* Teoremi di confronto per limiti di funzioni (versione dei carabinieri e confronto I/II)
* Forme indeterminate e primi usi di de l’Hôpital (enunciato in seguito)

### 3.1.1 Limiti notevoli (per funzioni) ([appunti](03-limiti-continuita/3.1-limiti-funzioni.md))

* Tutti i limiti notevoli “standard” usati negli esercizi (sin x / x, (1+1/x)^x, log(1+x)/x, ecc.)

### 3.2 Continuità ([appunti](03-limiti-continuita/3.2-continuita.md))

* Definizione di continuità in un punto e su un intervallo
* Continuità per composizione, somma, prodotto, quoziente
* Punti di discontinuità e loro classificazione (prima/seconda specie, rimovibile, salto)
* Teorema di esistenza di massimo e minimo (Weierstrass) per funzioni continue su [a,b]
* Teorema degli zeri (Bolzano)
* Teorema dei valori intermedi
* Teorema di locale limitatezza delle funzioni continue

### 3.3 Continuità uniforme ([appunti](03-limiti-continuita/3.3-continuita-uniforme.md))

* Definizione di continuità uniforme
* Teorema di Heine–Cantor: continua su compatto ⇒ uniformemente continua

### 3.4 Infinitesimi e infiniti, confronto tra funzioni ([appunti](03-limiti-continuita/3.4-infinitesimi-infiniti.md))

* Notazione `o(·)` e `O(·)` (o-piccolo)
* Confronto asintotico tra funzioni vicino ad un punto

--- 

## 4. Calcolo differenziale

Cartella: `04-calcolo-differenziale`

### 4.1 Derivate ([appunti](04-calcolo-differenziale/4.1-derivate.md))

* Definizione di derivata in un punto (limite del rapporto incrementale)
* Derivate laterali
* Derivabilità ⇒ continuità (teorema)
* Regole di derivazione: somma, prodotto, quoziente, catena (derivata della composta) 
* Derivata dell’inversa (quando esiste)
* Derivate delle funzioni elementari (polinomi, razionali, exp, log, trig, inverse trig, potenze, radici)

### 4.1.2 Derivate successive ([appunti](04-calcolo-differenziale/4.1-derivate.md))

* Derivata seconda e derivate di ordine superiore

### 4.2 Teoremi fondamentali del calcolo differenziale ([appunti](04-calcolo-differenziale/4.2-teoremi-taylor.md))

* Teorema di Rolle
* Teorema di Lagrange (MVT)
* Teorema di Cauchy (forma generale del MVT)
* Teorema della permanenza del segno tramite la derivata
* Teorema di de l’Hôpital (forme 0/0, ∞/∞)

#### Formula di Taylor ([appunti](04-calcolo-differenziale/4.2-teoremi-taylor.md))

* Formula di Taylor con resto di Peano
* Formula di Taylor con resto di Lagrange
* (Opzionale/meno centrale: forma con resto integrale)

### 4.3 Proprietà delle funzioni: monotonia e punti estremali ([appunti](04-calcolo-differenziale/4.3-monotonia-estremi-convessita.md))

* Relazione tra segno della derivata e monotonia
* Teorema di Fermat (condizione necessaria per estremi interni)
* Criteri di primo e secondo ordine per massimi/minimi locali
* Concavità/convessità, flessi
* Convessità e funzioni convesse (definizione e proprietà base)

### 4.4 Studio di funzione ([appunti](04-calcolo-differenziale/4.4-studio-di-funzione.md))

* Dominio, simmetrie
* Limiti e calcolo degli asintoti (verticali, orizzontali, obliqui)
* Segno della funzione
* Derivate prima e seconda: intervalli di monotonia e concavità/convessità, punti critici
* Costruzione del grafico complessivo

--- 

## 5. Integrazione

Cartella: `05-integrali`

### 5.1 Integrale di Riemann ([appunti](05-integrali/5.1-integrale-riemann.md))

* Partizioni di un intervallo, somme superiori ed inferiori (somme di Riemann)
* Definizione di funzione integrabile in senso di Riemann
* Criterio di integrabilità: funzioni continue e funzioni monotone limitate sono integrabili (teoremi)
* Interpretazione geometrica (area sottografico)

### 5.2 Proprietà dell’integrale ([appunti](05-integrali/5.2-proprieta-teorema-fondamentale.md))

* Linearità, monotonia, additività rispetto all’intervallo
* Teorema di spezzamento
* Teorema della media integrale

#### 5.2.1 Integrali definiti e teorema fondamentale del calcolo ([appunti](05-integrali/5.2-proprieta-teorema-fondamentale.md))

* Teorema fondamentale del calcolo integrale (Torricelli–Barrow)
* Relazione tra integrale definito e primitive
* Continuità e derivabilità della funzione integrale

### 5.3 Integrali indefiniti e regole di integrazione ([appunti](05-integrali/5.3-integrali-indefiniti.md))

* Primitive e integrali indefiniti
* Integrazione per parti (teorema e formula)
* Integrazione per sostituzione (cambiamento di variabile)

### 5.4 Tecniche di integrazione ([appunti](05-integrali/5.4-tecniche-integrazione.md))

* Integrazione di funzioni razionali fratte tramite frazioni semplici (teorema specifico)
* Altre tecniche standard (sostituzioni trigonometrie, Weierstrass, ecc., richiamate anche in appendice)

### 5.5 Integrali impropri ([appunti](05-integrali/5.5-integrali-impropri.md))

* Definizione di integrale improprio per:

  * intervalli infiniti
  * funzioni con singolarità interne / ai bordi
* Criteri di convergenza:

  * confronto per integrali impropri
  * caratterizzazione dell’integrabilità in senso improprio

### 5.6 Applicazioni degli integrali ([appunti](05-integrali/5.6-applicazioni.md))

* Calcolo di aree piane
* Volumi di solidi di rotazione
* Lunghezza di curva (curva rettificabile)

### 5.7 Alcune disuguaglianze importanti ([appunti](05-integrali/5.7-disuguaglianze.md))

* Disuguaglianza triangolare per integrali
* Disuguaglianza di Cauchy–Schwarz (versione integrale)
* Disuguaglianza di Hölder
* Disuguaglianza di Young
* Disuguaglianza di Jensen

--- 

## 6. Equazioni differenziali ordinarie

Cartella: `06-equazioni-differenziali`

### 6.0 Introduzione ([appunti](06-equazioni-differenziali/6.0-introduzione.md))

* Definizione di equazione differenziale ordinaria (EDO), ordine, soluzione generale/particolare
* Problema di Cauchy (dato iniziale)

### 6.1 Metodi risolutivi di alcune EDO ([appunti](06-equazioni-differenziali/6.1-metodi.md))

* EDO del primo ordine:

  * a variabili separabili (metodo standard)
  * omogenee nelle variabili (sostituzione y=ux)
  * lineari del primo ordine (fattore integrante)
  * Bernoulli, Riccati (forme notevoli)
* EDO lineari di ordine superiore (in particolare 2° ordine):

  * omogenee a coefficienti costanti
  * equazione caratteristica, soluzioni reali, complesse, multiple
  * equazioni forzate e metodo di variazione delle costanti

### 6.2 Buona positura del problema di Cauchy (parte teorica) ([appunti](06-equazioni-differenziali/6.2-buona-positura.md))

* Spazi metrici, completezza, compattezza (quanto basta per i teoremi)
* Funzioni lipschitziane, contrazioni
* Lemma di Grönwall (enunciato, uso)
* Teorema delle contrazioni (Banach–Caccioppoli)
* Teorema di Picard–Lindelöf (esistenza e unicità locale del problema di Cauchy)
* Teorema di Peano (esistenza senza unicità)
* Dipendenza continua dai dati iniziali
* Intervalli massimali di esistenza, estensione delle soluzioni

### 6.3 Studi qualitativi ([appunti](06-equazioni-differenziali/6.3-studi-qualitativi.md))

* Punti di equilibrio di un’EDO autonoma
* Stabilità/instabilità qualitativa
* Diagrammi di fase in R (linea delle fasi)
