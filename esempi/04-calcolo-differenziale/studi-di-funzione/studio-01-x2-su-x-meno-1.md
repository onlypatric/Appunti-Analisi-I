# Studio 01 — $f(x)=\dfrac{x^2}{x-1}$

**Teoria usata.** [`04-calcolo-differenziale/4.4-studio-di-funzione.md`](../../../04-calcolo-differenziale/4.4-studio-di-funzione.md) (dominio, zeri/segno, limiti e asintoti, monotonia ed estremi, convessità).

Grafico: ![](../../../assets/plots/studi-di-funzione/studio-01-x2-su-x-meno-1.svg)

---

## 1) Dominio

```math
f(x)=\frac{x^2}{x-1}\quad \Rightarrow\quad D=\mathbb{R}\setminus\{1\}.
```

---

## 2) Simmetrie

Non è né pari né dispari (in generale $f(-x)\ne f(x)$ e $f(-x)\ne -f(x)$).

---

## 3) Zeri e segno

```math
f(x)=0 \iff x^2=0 \iff x=0 \quad (\text{con } x\ne 1).
```

Per il segno: $x^2\ge 0$ e vale $x^2>0$ per $x\ne 0$.

- Se $x>1$, allora $x-1>0$ e $f(x)>0$.
- Se $x<1$ e $x\ne 0$, allora $x-1<0$ e $f(x)<0$.
- In $x=0$, $f(0)=0$.

---

## 4) Limiti e asintoti

### Asintoto verticale

```math
\lim_{x\to 1^-}\frac{x^2}{x-1}=-\infty,\qquad
\lim_{x\to 1^+}\frac{x^2}{x-1}=+\infty,
```
quindi $x=1$ è asintoto verticale.

### Asintoto obliquo

Divisione:
```math
\frac{x^2}{x-1}=x+1+\frac{1}{x-1}.
```
Per $x\to\pm\infty$, $\frac{1}{x-1}\to 0$, quindi l’asintoto obliquo è
```math
y=x+1.
```

---

## 5) Derivata prima: monotonia ed estremi

```math
f'(x)=\frac{2x(x-1)-x^2}{(x-1)^2}=\frac{x(x-2)}{(x-1)^2}.
```

Punti critici (dove $f'=0$): $x=0$ e $x=2$ (con $x\ne 1$).

Poiché $(x-1)^2>0$ per $x\ne 1$, il segno di $f'$ dipende da $x(x-2)$:

- per $x<0$: $x<0$, $x-2<0$ ⇒ $f'>0$;
- per $0<x<1$: $x>0$, $x-2<0$ ⇒ $f'<0$;
- per $1<x<2$: $x>0$, $x-2<0$ ⇒ $f'<0$;
- per $x>2$: $x>0$, $x-2>0$ ⇒ $f'>0$.

Conclusione:

- crescente su $(-\infty,0)$ e $(2,+\infty)$;
- decrescente su $(0,1)$ e $(1,2)$.

Valori notevoli:

- $f(0)=0$ è un massimo locale (da crescente a decrescente).
- $f(2)=4$ è un minimo locale (da decrescente a crescente).

---

## 6) Derivata seconda: concavità e flessi

Partendo da $f(x)=x+1+\frac{1}{x-1}$:
```math
f''(x)=\left(\frac{1}{x-1}\right)''=\frac{2}{(x-1)^3}.
```

Quindi:

- per $x<1$: $(x-1)^3<0$ ⇒ $f''(x)<0$ ⇒ concava;
- per $x>1$: $(x-1)^3>0$ ⇒ $f''(x)>0$ ⇒ convessa.

Non ci sono flessi nel dominio (il cambio di concavità avviene “attraverso” $x=1$, che non è nel dominio).

---

## 7) Riassunto finale

- Dominio: $R\setminus\{1\}$.
- Asintoti: verticale $x=1$, obliquo $y=x+1$.
- Estremi: massimo locale in $x=0$ con $f(0)=0$; minimo locale in $x=2$ con $f(2)=4$.
- Concavità: concava su $(-\infty,1)$, convessa su $(1,+\infty)$.


---

**Teoria usata.** [`04-calcolo-differenziale/4.4-studio-di-funzione.md`](../../../04-calcolo-differenziale/4.4-studio-di-funzione.md) (dominio, zeri/segno, limiti e asintoti, monotonia ed estremi, convessità).
