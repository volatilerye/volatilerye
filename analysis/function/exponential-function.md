# 指数関数・べき関数とその考察

この記事ではべき関数についてのより厳密な議論をするために **べき乗** から始め, 最終的には複素関数にまで拡張することを目標に議論する.

## べき乗 (累乗, exponentiation)

> [!DEFINITION] Definition 1:  べき乗 (基本)
> $b$ を実数, $n$ を正の整数 としたとき, **べき乗 (累乗, exponentiation)** $b^n$ は次のように定義される. ($b^n$ は $b$ の $n$ 乗という.)
> $$
> b^n := 
> \begin{cases}
>   b & \text{if\quad$n=1$}, \\
>   b^{n-1} \times b & \text{otherwise}.
> \end{cases}
> $$
> このとき, $b$ を **底 (基数, base)**, $n$ を **指数 (べき数, exponent)** という. 

すなわち, $b^n = \underbrace{b\times b\times\dots\times b\,}_{n\text{ times}}$ というように $b$ を $n$ 個掛けたものを $b^n$ と定義している.

> [!REMARK]
> 括弧を用いず $a^{b^c}$ と書いた場合, $a^{(b^c)}$ のように右側から計算するのが一般的である. (右結合性)


> [!NOTE] Note: 群との関係性
> ここでは実数体 (実数と四則演算で構成された体系) を前提に定義しているが, 定義1はより一般化した群にも同じように定義できる. また, 群の結合律によって定義1が well-defined であることが保証されている.
>
> ただし, 以降の定理3から一般の体系では成立しない法則も存在するので注意.

定義から次の命題は明らかであろう.

> [!PROPOSITION] Proposition 2:  自明なべき乗
> $b$ を実数, $n$ を正の整数としたとき, 次が成立する.
> 1. $$b^1=b.$$
> 2. $$1^n=1.$$
> 3. $$b^n = 0 \Longleftrightarrow b=0.$$

べき乗は次の **指数法則** が成立する.

> [!THEOREM] Theorem 3:  指数法則
> $a, b$ を実数, $m,n$ を正の整数としたとき, 次が成立する.
> 1. $$a^mb^n = a^{m+n}.$$
> 2. $$(a^m)^n = a^{mn}.$$
> 3. $$(ab)^n = a^nb^n.$$
> 3. $b=0$ のとき, $$\left(\dfrac{a}{b}\right)^n = \dfrac{a^n}{b^n}.$$

<details>
<summary>証明 (クリックで展開)</summary>

> [!PROOF]  
> **1.**  
> $n=1$ のときは定義より明らか. $n=k$ のとき成立すると仮定すると, 
> $$a^ma^{k+1}=a^m(a^ka)=(a^ma^k)a=a^{m+k}a=a^{m+(k+1)}$$
> であるから, $n=k+1$ のときにも成立し, 帰納法によって示された.
> 
> **2.**  
> $n=1$ のときは明らか. $n=k$ のとき成立すると仮定すると, 1の法則を用いて
> $$(a^m)^{k+1}=(a^m)^ka^m=a^{mk}a^m=a^{mk+m}=a^{m(k+1)}$$
> であるから, $n=k+1$ のときにも成立し, 帰納法によって示された.
>
> **3.**  
> $n=1$ のときは明らか. $n=k$ のとき成立すると仮定すると, 1の法則を用いて
> $$(ab)^{k+1}=(ab)^kab=a^kb^kab=a^kab^kb=a^{k+1}b^{k+1}$$
> であるから, $n=k+1$ のときにも成立し, 帰納法によって示された.
>
> **4.**  
> 法則3より, 
> $$
> \left(\dfrac{a}{b}\cdot b\right)^n=\left(\dfrac{a}{b}\right)^nb^n \Longrightarrow a^n = \left(\dfrac{a}{b}\right)^nb^n
> \Longrightarrow \left(\dfrac{a}{b}\right)^n = \dfrac{a^n}{b^n}.
> $$

</details>


## 負の整数の乗

先ほどの定義は $b$ を $n$ 個掛けるという直感的に分かりやすい定義から始めたが, $n$ を **正の整数** に限定しているため, **0乗** や **負の整数** へ拡張することができない.

そこで, 発想を逆転させて **べき乗の定義から得られた指数法則を定義内へ自然に埋め込もう**.

> [!DEFINITION] Definition 4:  べき乗 (整数)
> $b$ を **0でない実数**, $n$ を **整数** としたとき, $b^n$ は次のように定義される.
> $$
> b^n := 
> \begin{cases}
>   1 & \text{if\quad$n=0$}, \\
>   b^{n-1} \times b & \text{if\quad$n>0$}, \\
>   \dfrac{1}{b^n} & \text{otherwise.}
> \end{cases}
> $$

拡張前 (定義1) で定義可能なべき乗は拡張後 (定義4) と一致していることは明らかであろう.

指数法則 $a^{m+n}=a^ma^n$ の $m,n$ は正の整数としていたが, この $m,n$ の定義域を整数へ拡張することで, 
$$
    a^na^0 = a^n \Longrightarrow a^0= 1
$$
から $a^0=1$ と定義できる.

また, 
$$
    a^na^{-n} = a^0 \Longrightarrow a^{-n} = \dfrac{1}{a^n}
$$
とすることで $n$ を整数全体へ拡張することができる.


> [!REMARK] Remark:  底が 0 のとき
> ただし底が 0 のときは $n<0$ のときの定義に当てはめると $\dfrac{1}{0}$ となるため, $0^n\;(n\leq0)$は定義することができない.
> 
> また, 系3の3番目の命題は成立しなくなることに留意せよ.

今回の定義の拡張では定理2の法則1のみを利用したが, 残りの指数法則の性質も引き継がれる.
以降の定義の拡張にも指数法則を元に底と指数の定義域を拡張していくことに留意しよう.

> [!PROPOSITION] Proposition 5:  自明なべき乗
> $b$ を0でない実数, $n$ を整数としたとき, 次が成立する.
> 1. $$b^0=1.$$
> 2. $$b^1=b.$$
> 3. $$1^n=1.$$
> 3. $$b^nb^{-n}=1.$$
> 4. $$b^n \neq 0.$$


> [!PROPOSITION] Proposition 6:  べき乗同士の除法
> $a$ を0でない実数, $m,n$ を整数としたとき,
> $$\dfrac{a^m}{a^n} = a^{m-n}.$$

<details>
<summary>証明 (クリックで展開)</summary>

> [!PROOF] 
> $a^{m-n}a^{n}=a^m$ を示せばよい. また, 定義より $a^0 = 1 = \dfrac{1}{a^0}$ に留意せよ. 
> - $m> n,\;n\ge0$ のとき, 定理3より明らか.
> - $m> n,\;n<0$ のとき, 定理3から $a^{m-n}a^{n} = \dfrac{a^{m-n}}{a^{-n}} = \dfrac{a^na^{m-n}}{a^na^{-n}} =a^m$ より成立.
> - $m\le n,\;n\ge0$ のとき, 定理3から $a^{m-n}a^{n} = \dfrac{a^{n}}{a^{n-m}} = \dfrac{a^ma^{n}}{a^ma^{n-m}}
>   = \dfrac{a^ma^{n}}{a^n} = a^m$ より成立.
> - $m\le n,\;n<0$ のとき, 定理3から $a^{m-n}a^{n} = \dfrac{1}{a^{-n}a^{n-m}} = \dfrac{1}{a^m} = a^m$ より成立.

</details>


> [!LEMMA] Lemma 7:  負の整数乗
> $a$ を0でない実数, $n$ を整数としたとき,
> $$(a^n)^{-1} = (a^{-1})^n = a^{-n}.$$


<details>
<summary>証明 (クリックで展開)</summary>

> [!PROOF]  
> n=0 のときは定義に従って確認すれば良い.
>
> - $n>0$ のとき, $(a^n)^-1=a^{-n}$ は定義4より明らかであり, また定理3から
>   $$(a^{-1})^n=\left(\dfrac{1}{a}\right)^n = \dfrac{1^n}{a^n} = \dfrac{1}{a^n} = a^{-n}$$
>   より成立する.
> - $n<0$ のとき, $n=-m$ とすれば $(a^{-m})^{-1} = (a^{-1})^{-m} = a^m$ を証明することで命題も直ちに示される.
>   $$
>   \begin{align*}
>   (a^{-m})^{-1} &= \left(\dfrac{1}{a^m}\right)^{-1} = \dfrac{1}{\dfrac{1}{a^m}} = a^m, \\
>   (a^{-1})^{-m} &= \left(\dfrac{1}{a}\right)^{-m} = \dfrac{1}{\left(\dfrac{1}{a}\right)^m} = \dfrac{1}{\dfrac{1}{a^m}} = a^m.
>   \end{align*}
>   $$

</details>


> [!THEOREM] Theorem 8:  指数法則
> $a, b$ を0でない実数, $m,n$ を整数としたとき, 次が成立する.
> 1. $$a^ma^n = a^{m+n}.$$
> 2. $$(a^m)^n = a^{mn}.$$
> 3. $$(ab)^n = a^nb^n.$$
> 4. $$\left(\dfrac{a}{b}\right)^n = \dfrac{a^n}{b^n}.$$

<details>
<summary>証明 (クリックで展開)</summary>

> [!PROOF]  
> **1.**  
> 命題5の $m$ を $m+n$ に置換すると, 
> $$
> \dfrac{a^{m+n}}{a^n} = a^m \Longrightarrow a^ma^n = a^{m+n}.
> $$
>
> **2.**  
> 補題7を用いる.
> - $m=0$ または $n=0$ のとき, 系5の法則1より成立する. (各自確認せよ)
> - $m>0,\;n>0$ のときは定理3より明らか.
> - $m>0,\;n<0$ のとき, $(a^m)^n = ((a^m)^{-1}) ^{-n} = ((a^m)^{-n})^{-1} = (a^{-mn})^{-1} = a^{mn}.$
> - $m<0,\;n>0$ のとき, $(a^m)^n = ((a^{-1})^{-m})^n = ((a^{-m})^{-1})^n = ((a^{-m})^{n})^{-1}= (a^{-mn})^{-1} = a^{mn}.$
> - $m<0,\;n<0$ のとき, $(a^m)^n = (((a^{-m})^{-1})^{-n})^{-1} = (((a^{-m})^{-n})^{-1})^{-1} = a^{mn}.$
>
> **3.**  
> $n\ge0$ のときは系3または系6から明らか.  
> $n<0$ のとき, 
> $$(ab)^n = \dfrac{1}{(ab)^{-n}} = \dfrac{1}{a^{-n}b^{-n}} = \dfrac{1}{a^{-n}}\dfrac{1}{b^{-n}} = a^nb^n.$$
>
> **4.**  
> $(ab^{-1})^{n} = a^nb^{-n}$ を示せばよいが, これば法則3より成立する.

</details>

## 有理数のべき乗

整数のべき乗を求めることができたのならば, 

> [!DEFINITION] Definition 9:  べき乗 (有理数)
> $b>0$ を実数, $r\ge0$ を **有理数** とする.  
> $r = \dfrac{m}{n}$ ($m,n$は整数, かつ $n>0$) であるとき, **べき乗 (累乗, exponentiation)** $b^r$ は次のように定義される.
> $$
> \begin{align*}
> b^{1/n} &:= x\quad\text{s.t.}\quad b=x^n\quad\text{where}\quad{x>0},\\
> b^r &:= 
> \begin{cases}
>   1 & \text{if\quad$m=0,$} \\
>   (b^{1/n})^{m-1} \times b & \text{if\quad$m>0,$} \\
>   \dfrac{1}{(b^{1/n})^m} & \text{if\quad$m<0$}. \\
> \end{cases}
> \end{align*}
> $$

> [!PROPOSITION] Proposition 10: &nbsp; $f_n(x)=x^n$
> $f_n(x) = x^n\;(n\in\mathbb{Z^+})$ であるような関数 $f_n:(0,\infty)\to(0,\infty)$ は逆関数を持つ: すなわち $f_n$ は全単射である.

<details>
<summary>証明 (クリックで展開)</summary>

> [!PROOF]
> $f_n(x)=x^n$ は狭義単調増加だから, $a<b \Longrightarrow f_n(x)<f_n(y)$ より単射である.
>
> また, $f$ は $x\in[0,\infty)$ で連続である. 全射でないと仮定すると, 任意の$x>0$ において $f_n(x)\neq c$ であるような $c>0$ が存在するが, $b>c$ であるような $b$ を適当に選ぶと中間値の定理より $f_n(0)<f_n(c)<f(b)$ となるような $c$ が存在するので矛盾.

</details>

> [!PROPOSITION] Proposition 11:  べき乗 (有理数)の定義の well-defined 性
> 定義9は well-defined である. すなわち,
> 
> 1. $b^r$ となる実数を実際に定義に従って取ることができる.
> 2. $r=m/n$ のとき, $m,n$ の選択に依存しない.

<details>
<summary>証明 (クリックで展開)</summary>

> [!PROOF]
> 命題10より, $f_n(x)=x^n$ は逆関数 $f_n^{-1}(x)$ が存在するので
> $$x^{m/n} = (f_n^{-1}(x))^m$$
> から定義に従った実数が定まる.
>
> また, $\dfrac{m}{n} = \dfrac{m'}{n'}$ であるならば, $m'=km,\;n'=kn$ となるような整数 $k$ が 存在するので, $b^{m'/n'}=x$ とすると
> $$
> \begin{align*}
> & b^{m'/n'} = x \\
> \Longrightarrow\;& (b^{1/n'})^{m'} = x \\
> \Longrightarrow\;& f_{n'}^{-1}(b) = f_{m'}^{-1}(x) \\
> \Longrightarrow\;& (f_n \circ f_k)^{-1}(b) = (f_m\circ f_k)^{-1}(x) \quad (f_{mn}(x) = x^{mn} = (x^m)^n = (f_n\circ f_m)(x))\\
> \Longrightarrow\;& (f_k^{-1} \circ f_n^{-1})(b) = (f_k^{-1}\circ f_m^{-1})(x)\\
> \Longrightarrow\;& f_k(f_n^{-1}(b)) = f_k(f_m^{-1}(x))\\
> \Longrightarrow\;& f_n^{-1}(b) = f_m^{-1}(x)\quad(f \text{が単射より})\\
> \Longrightarrow\;& b^{m/n} = x
> \end{align*}
> $$
> でああるから, $r^{m/n} = r^{m'/n'}$ が示せた.

</details>

> [!Remark] Remark.  定義域について
> もし$b\le0$ を許す, あるいは $x$ に負の実数を認めてしまった場合は $b^r$ は well-defined ではなくなってしまう.
> 
> 例えば $(-1)^{1/3}$ を考えると, これは $(-1)^{2/6}$ と値が一致するべきだろう.
> すると $x^3=-1$ となるような実数 $x$ は $-1$ が存在するが, $x^6=-1$ となるような実数 $x$ は存在しないので, これは $r$ の分数の表記方法に依存してしまう.

> [!NOTE]
> 只今執筆中...