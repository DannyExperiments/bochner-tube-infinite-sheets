# Q1338: Infinite sheets for a Bochner tube at infinity

## Exact question and editions

Suprokash Hazra, *Some open problems on the envelope of holomorphy*, Concrete Operators 13 (2026), 20250014, [publisher-layout version of record, PDF p. 2, Definition 2.2 and Open Question 2.3](https://diva-portal.org/smash/get/diva2:2043979/FULLTEXT01.pdf#page=2), [DOI](https://doi.org/10.1515/conop-2025-0014), asks of the envelope: “always finitely sheeted? Is the envelope ℰ(D) always schlicht?” The setup is a domain \(D\subset\mathbb C^n\), \(n\ge2\), which for \(\|\operatorname{Im} z\|>r\) agrees exactly with the full tube \(G+i\mathbb R^n\), where the tube type \(G\subset\mathbb R^n\) is relatively compact with smooth connected boundary. There is no smoothness requirement on the entire boundary of \(D\) in this question. [Hazra's final thesis](https://diva-portal.org/smash/get/diva2:2049697/FULLTEXT01.pdf#page=72), Question 6.1.3, separately asks the case of a centered ball tube type.

**Result.** Both answers are negative, even when \(n=2\) and \(G\) is a round disk, which can be centered at zero. The constructed envelope has infinitely many points in the fiber over every point of a particular circle.

## 1. Bounded seed and a polynomial suited to the tail

Use the spiral-domain construction of Hazra–Porten, [arXiv:2306.00441v1, §2, Lemma 2.3](https://arxiv.org/html/2306.00441v1#S2), or [§3, Proposition 3.1](https://arxiv.org/html/2306.00441v1#S3), published as *Truncated tube domains with multi-sheeted envelope*, [Proc. AMS 153 (2025), 2981–2994](https://doi.org/10.1090/proc/17179). The arXiv full text supplies the spiral construction used here; publication identity was verified separately. Specifically the semi-infinite strip parametrization in §2 gives a simply connected open \(X\subset\{u\in\mathbb R^2:1<|u|<2\}\) and a seed \(S=X+i B_{1/4}(0)\). Their transversality condition holds for the line \(w_1=iw_2\) because its real and imaginary vectors have equal norm. The envelope of \(S\) has a continuous lift of the real unit circle parametrization \(\theta\mapsto(\cos\theta,\sin\theta)\) for all sufficiently large \(\theta\), in a single connected envelope. This is the curve of germs constructed in the proof of Lemma 2.3. Equivalently one can use the universally covered circle from §3, with its simply connected annular spiral thickening.

Let \(e=1/10\), \(c=(1,i)\), \(A(w)=c+e w\), and \(S'=A(S)\). Use the entire polynomial
\[
P(z)=z_1^2+z_2^2=(z_1+i z_2)(z_1-i z_2).
\]
It obeys
\[
P(A(w))=e(w_1+i w_2)\bigl(2+e(w_1-i w_2)\bigr).
\]
For \(w=u+iv\in S\), \(|w_1+i w_2|\ge |u|-|v|>3/4\) and \(|w_1-i w_2|\le |u|+|v|<9/4\). Consequently \(P\) has no zeros on \(S'\), and it has a holomorphic logarithm there because \(S'\) is simply connected. The transformed real base of \(S'\) is \(X'=(1,0)+e X\) and its imaginary base is \(Y'=B_{1/40}((0,1))\).

## 2. Complete the tail without losing the logarithm

Choose an open round disk \(G\) with \(\overline G\subset X'\) on which the second real coordinate has one strict nonzero sign even on \(\overline G\). Such a disk exists since \(X'\) is open and nonempty. Set \(m=\min_{x\in\overline G}|x_2|>0\) and \(K=\max_{x\in\overline G}|x_1|\). Choose \(0<\delta<\min(1/40,m/(2(K+1)))\). Define
\[
V=G+i\{y:|y_1|<\delta,\ 1<y_2<4\},\qquad
T=G+i\{y:|y|>3\},\qquad
D=S'\cup V\cup T.
\]
Both overlaps \(S'\cap V\) and \(V\cap T\) are nonempty and connected. The first is the product with \(G\) of the intersection of a disk and a rectangle. In the second, the imaginary coordinates satisfy \(|y_1|<\delta\) and \(\sqrt{9-y_1^2}<y_2<4\), a connected strip of nonempty intervals. The other overlap is empty because all imaginary parts in \(S'\) have norm less than \(41/40\). Thus \(D\) is a domain. Outside \(|y|\le3\), it agrees exactly with \(T\), since \(V\) adds no real points outside \(G\).

On \(V\), \(\operatorname{Im}P=2(x_1y_1+x_2y_2)\) has the sign of \(x_2\): the first term in parentheses has magnitude at most \(K\delta<m/2\), while the second has magnitude greater than \(m\). Hence \(P(V)\) is in one open half-plane avoiding zero. On \(T\), \(\operatorname{Re}P=|x|^2-|y|^2<0\) since \(|x|<6/5\) on \(X'\). Thus both \(V\) and \(T\) admit holomorphic logs of \(P\). On the connected overlaps the logs differ by constants in \(2\pi i\mathbb Z\). Choose the additive constant on \(V\) to match \(S'\), then on \(T\) to match \(V\). The result is a single \(f\in\mathcal O(D)\) with \(\exp f=P\).

## 3. Witness distinct sheets on the envelope of the enlarged domain

The inclusion \(S'\subset D\) induces a projection-preserving holomorphic map \(\mathcal E(S')\to\mathcal E(D)\) by the universal property of the envelope (or by restricting all analytic continuation germs to functions from \(D\)). This map need not be injective, so multiplicity must be proved, not assumed. The holomorphic extension \(\widetilde f\) of \(f\) satisfies \(\exp\widetilde f=P\circ\pi_D\) by the identity theorem on the connected envelope.

Map the lifted half-infinite circle from the seed into \(\mathcal E(D)\). Its projected curve is \(z(\theta)=c+e(\cos\theta,\sin\theta)\). There,
\[
P(z(\theta))=e e^{i\theta}(2+e e^{-i\theta}).
\]
The second factor lies in the open right half-plane and has a periodic continuous logarithm. Thus the value of \(\widetilde f\) along the lifted curve increases by \(2\pi i\) every full turn, by uniqueness of continuous lifts under the exponential. At every fixed phase this yields infinitely many distinct values at points with exactly the same projection, proving infinite multiplicity. A real translation sends the center of \(G\) to zero, preserves the imaginary-tail equality with \(r=3\), and preserves fiber multiplicities.

## Prior-work check (2026-11-27)

Checked the final Concrete Operators PDF (the question's version of record) and the thesis formulation. Searched the exact phrasing, DOI, Bochner tubes at infinity, finite-sheet and logarithmic/spiral counterexamples. No exact prior negative example for the required tail was found. Ordinary Bochner convexification applies to a full tube, not to this union. The 2025 Hazra–Porten bounded spiral gives only the seed, which has no prescribed unbounded exterior; adjoining a tail without a compatible separating function does not preserve the sheet count by functoriality alone. The extension here is the polynomial factorization that retains winding locally while providing a half-plane-valued function on the entire required exterior, together with the connector and compatible logarithms. The seed geometry and standard envelope facts are explicitly credited. No independent peer review or exhaustive priority claim.
