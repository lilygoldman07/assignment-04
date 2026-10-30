
# CMPS 2200 Assignment 4
## Answers

**Name:** Lily Goldman

**1 Quicksort probabilities**

- **1a. (5 pts)** What is the probability that Quicksort does $\Omega({n^2})$ comparisons?

  Let $X$ be the number of comparisons Quicksort does. We know the expected work is $\mathbf{E}[X] = c_1 n \lg n$ for some constant $c_1$. To ask about $\Omega(n^2)$ comparisons, set $\alpha = c_2 n^2$ for some constant $c_2 > 0$. By Markov's inequality:

  $$\mathbf{P}[X \geq c_2 n^2] \leq \frac{c_1 n \lg n}{c_2 n^2} = \frac{c_1}{c_2} \cdot \frac{\lg n}{n} \in O\left(\frac{\lg n}{n}\right)$$

  This gives an upper bound of $O(\lg n / n)$, which goes toward 0 as $n$ gets bigger. So quadratic work becomes less likely for large inputs.

- **1b. (5 pts)** What is the probability that Quicksort does $10^c n \lg n$ comparisons, for a given $c>0$? What does this say about the deviation of the actual work from the expected work for Quicksort?

  Again let $X$ be the number of comparisons, and take $\mathbf{E}[X] = n \lg n$ (ignoring the constant factor). Set $\alpha = 10^c n \lg n$. By Markov's inequality:

  $$\mathbf{P}[X \geq 10^c n \lg n] \leq \frac{n \lg n}{10^c n \lg n} = \frac{1}{10^c}$$

  (If we keep the constant, $\mathbf{E}[X] = k\, n \lg n$, the bound is $k / 10^c$, which behaves the same way.)

  The bound gets 10 times smaller whenever $c$ increases by 1. For example, when $c=3$, the probability is at most $1/1000$ if we ignore the constant. This shows that very large deviations have a small upper bound, although Markov's inequality does not give the exact probability.

**2 From "Maybe" to "Definitely"**

- **2a. (10 pts)** Give an algorithm to improve the guaranteed success probability and state its work.

  **Algorithm $\mathcal{A}'(\mathcal{I}, \delta)$:**

  1. Compute $k = \left\lceil \dfrac{\ln(1-\delta)}{\ln(1-\epsilon)} \right\rceil$.
  2. Repeat up to $k$ times:
     - Run $\mathcal{A}(\mathcal{I})$ to get an answer.
     - Check it with $\mathcal{C}(\mathcal{A}(\mathcal{I}))$. If the check says it is correct, return that answer.
  3. If none of the $k$ runs passed the check, return the last answer (failure).

  **Why it works:** Each run has a $1-\epsilon$ chance of failing, and the runs are independent. The new algorithm fails only if all $k$ tries fail, so we need:

  $$(1-\epsilon)^k \leq 1-\delta \quad\Longrightarrow\quad k \geq \frac{\ln(1-\delta)}{\ln(1-\epsilon)}$$

  Choosing $k$ this way gives a success probability of at least $\delta$.

  **Work:** Each round costs $O(w(n) + v(n)) = O(w(n))$ since $v(n) \in O(w(n))$. There are at most $k$ rounds, so the work is

  $$O\left(w(n) \cdot \frac{\ln(1-\delta)}{\ln(1-\epsilon)}\right)$$

- **2b. (6 pts)** Show how to convert $\mathcal{A}$ into an algorithm that always produces the correct result, but has an expected runtime that depends on $w(n)$ and a success probability $\epsilon$.

  **Algorithm $\mathcal{A}''(\mathcal{I})$:** Keep running $\mathcal{A}(\mathcal{I})$ and checking the answer with $\mathcal{C}$ until the check passes. Then return that answer. There is no limit on the number of tries.

  Since the algorithm only returns an answer after it passes the check, it will not return an incorrect answer. It terminates with probability 1 when $\epsilon > 0$.

  **Expected work:** Each try succeeds with probability $\epsilon$, independently. The number of tries until the first success is a geometric random variable, whose expected value is $1/\epsilon$. Each try costs $O(w(n) + v(n)) = O(w(n))$. So the expected work is

  $$O\left(\frac{w(n)}{\epsilon}\right)$$

**3 Determinism versus Randomization in Quicksort**

- **3b. (8 pts)** Compare running times using `compare-qsort` between variants of Quicksort and the provided implementation of selection sort (`ssort`).

  All times are in milliseconds.

  **Random permutations** (`compare_sort(shuffle=True)`):

  | n | ssort | qsort-fixed-pivot | qsort-random-pivot |
  |---|---|---|---|
  | 100 | 0.196 | 0.114 | 0.128 |
  | 200 | 0.500 | 0.233 | 0.220 |
  | 400 | 2.325 | 0.508 | 0.601 |
  | 800 | 8.801 | 1.306 | 1.187 |

  **Already sorted lists** (`compare_sort(shuffle=False)`):

  | n | ssort | qsort-fixed-pivot | qsort-random-pivot |
  |---|---|---|---|
  | 100 | 0.094 | 0.646 | 0.085 |
  | 200 | 0.342 | 1.302 | 0.175 |
  | 400 | 1.271 | 5.047 | 0.435 |
  | 800 | 5.409 | 21.235 | 0.893 |

  **Comparison to asymptotic bounds:**

  - **Selection sort** takes $O(n^2)$ time because it keeps searching for the smallest remaining item. Its time grows a lot when $n$ doubles, which matches this bound.
  - **Quicksort on random lists** is expected $O(n \lg n)$ with either pivot method. Both versions were faster than selection sort in my tests.
  - **Fixed-pivot Quicksort on sorted lists** reaches its $O(n^2)$ worst case. Since the first item is always the smallest, the partitions are very uneven. Its time goes from about 5.0 ms to 21.2 ms between 400 and 800 elements.
  - **Random-pivot Quicksort on sorted lists** still has expected $O(n \lg n)$ time, and its results were much better than the fixed-pivot version.

  **Effect of the input type:** With random inputs, the two Quicksort versions were pretty similar. On sorted inputs, the fixed-pivot version became the slowest because it kept choosing a bad pivot. Choosing a random pivot helped avoid that pattern. Selection sort was slow for both types of input because it still has to scan the remaining elements each time.

- **3c. (8 pts)** Compare the fastest of your sorting implementations to the Python sorting function `sorted`, conducting the tests in 3b above.

  The fastest of my implementations is random-pivot Quicksort. All times are in milliseconds.

  **Random permutations** (`compare_timsort(shuffle=True)`):

  | n | qsort-random-pivot | timsort |
  |---|---|---|
  | 1000 | 1.264 | 0.100 |
  | 10000 | 15.350 | 1.250 |
  | 100000 | 248.090 | 24.508 |
  | 1000000 | 3000.401 | 285.629 |

  **Already sorted lists** (`compare_timsort(shuffle=False)`):

  | n | qsort-random-pivot | timsort |
  |---|---|---|
  | 1000 | 1.249 | 0.008 |
  | 10000 | 14.555 | 0.058 |
  | 100000 | 175.330 | 0.933 |
  | 1000000 | 2032.424 | 9.253 |

  **On random lists**, Python's `sorted` was around 10 times faster than my random-pivot Quicksort. They both follow roughly $O(n \lg n)$ growth, but Python's built-in sorting has much less overhead than my recursive Python code.

  **On sorted lists**, `sorted` was even faster. Timsort can recognize that the list is already in order, so it can handle this input in $O(n)$ time. My random-pivot Quicksort still has expected $O(n \lg n)$ work.

  Overall, `sorted` was faster in both tests, especially when the input was already sorted.
