# CMPS 2200 Assignment 4
## Answers

**Name:**Lily Goldman

Place all written answers from `assignment-04.md` here for easier grading.


**1 Quicksort probabilities**

- **1a. (5 pts)** What is the probability that Quicksort does $\Omega({n^2})$
  comparisons? 

  Let $X$ be the number of comparisons Quicksort does. We know the expected work is $\mathbf{E}[X] = c_1 n \lg n$ for some constant $c_1$. To ask about $\Omega(n^2)$ comparisons, set $\alpha = c_2 n^2$ for some constant $c_2 > 0$. By Markov's inequality:

  $$\mathbf{P}[X \geq c_2 n^2] \leq \frac{c_1 n \lg n}{c_2 n^2} = \frac{c_1}{c_2} \cdot \frac{\lg n}{n} \in O\left(\frac{\lg n}{n}\right)$$

  So the probability is at most $O(\lg n / n)$, which goes to 0 as $n$ gets large. Quicksort doing quadratic work is very unlikely for big inputs.


- **1b. (5 pts)** What is the probability that Quicksort does $10^c n \lg n$
comparisons, for a given $c>0$? What does this say about the
deviation of the actual work from the expected work for Quicksort?

  Again let $X$ be the number of comparisons, and take $\mathbf{E}[X] = n \lg n$ (ignoring the constant factor). Set $\alpha = 10^c n \lg n$. By Markov's inequality:

  $$\mathbf{P}[X \geq 10^c n \lg n] \leq \frac{n \lg n}{10^c n \lg n} = \frac{1}{10^c}$$

  (If we keep the constant, $\mathbf{E}[X] = k\, n \lg n$, the bound is $k / 10^c$, which behaves the same way.)

  This means the chance that Quicksort does much more work than expected drops off very quickly. Every time we increase $c$ by 1, the probability of doing that much work gets at least 10 times smaller. For example, the chance of doing 1000 times the expected work is at most $1/1000$. So the actual work of Quicksort usually stays close to its expected $O(n \lg n)$ work, and large deviations are rare. (Markov's inequality is a loose bound, so the real probability is even smaller.)


**2 From "Maybe" to "Definitely"**

- **2a. (10 pts)** Give an algorithm to improve the guaranteed success probability and state its work.

  **Algorithm $\mathcal{A}'(\mathcal{I}, \delta)$:**
  1. Compute $k = \left\lceil \dfrac{\ln(1-\delta)}{\ln(1-\epsilon)} \right\rceil$.
  2. Repeat up to $k$ times:
     - Run $\mathcal{A}(\mathcal{I})$ to get an answer.
     - Check it with $\mathcal{C}(\mathcal{A}(\mathcal{I}))$. If the check says it is correct, return that answer.
  3. If none of the $k$ runs passed the check, return the last answer (failure).

  **Why it works:** Each run is independent and fails with probability $1-\epsilon$. $\mathcal{A}'$ only fails if all $k$ runs fail, which happens with probability $(1-\epsilon)^k$. We want this to be at most $1-\delta$:

  $$(1-\epsilon)^k \leq 1-\delta \quad\Longrightarrow\quad k \geq \frac{\ln(1-\delta)}{\ln(1-\epsilon)}$$

  (Both logs are negative, so dividing flips the sign back and $k$ is positive.) With this $k$, $\mathcal{A}'$ is correct with probability at least $\delta$.

  **Work:** Each round costs $O(w(n) + v(n)) = O(w(n))$ since $v(n) \in O(w(n))$. There are at most $k$ rounds, so the work is

  $$O\left(w(n) \cdot \frac{\ln(1-\delta)}{\ln(1-\epsilon)}\right)$$

  (Roughly, this is about $O\left(\frac{w(n)}{\epsilon} \ln \frac{1}{1-\delta}\right)$ when $\epsilon$ is small.)


- **2b. (6 pts)** Show how to convert $\mathcal{A}$ into an
  algorithm that always produces the correct result, but has an
  expected runtime that depends on $w(n)$ and a success probability
  $\epsilon$.

  **Algorithm $\mathcal{A}''(\mathcal{I})$:** Keep running $\mathcal{A}(\mathcal{I})$ and checking the answer with $\mathcal{C}$ until the check passes. Then return that answer. There is no limit on the number of tries.

  Because we only return an answer after it passes the check, $\mathcal{A}''$ **always returns the correct result**.

  **Expected work:** Each try succeeds with probability $\epsilon$, independently. The number of tries until the first success is a geometric random variable, whose expected value is $1/\epsilon$. Each try costs $O(w(n) + v(n)) = O(w(n))$. So the expected work is

  $$O\left(\frac{w(n)}{\epsilon}\right)$$

  (This turns a "Monte Carlo" algorithm, which may be wrong, into a "Las Vegas" algorithm, which is always right but has a random running time.)


**3 Determinism versus Randomization in Quicksort**


- **3b. (8 pts)** Compare running times using `compare-qsort` between variants of
Quicksort and the provided implementation of selection sort (`ssort`).

  All times are in milliseconds.

  **Random permutations** (`compare_sort(shuffle=True)`):

  |   n |   ssort |   qsort-fixed-pivot |   qsort-random-pivot |
  |-----|---------|---------------------|----------------------|
  | 100 |   0.196 |               0.114 |                0.128 |
  | 200 |   0.500 |               0.233 |                0.220 |
  | 400 |   2.325 |               0.508 |                0.601 |
  | 800 |   8.801 |               1.306 |                1.187 |

  **Already sorted lists** (`compare_sort(shuffle=False)`):

  |   n |   ssort |   qsort-fixed-pivot |   qsort-random-pivot |
  |-----|---------|---------------------|----------------------|
  | 100 |   0.094 |               0.646 |                0.085 |
  | 200 |   0.342 |               1.302 |                0.175 |
  | 400 |   1.271 |               5.047 |                0.435 |
  | 800 |   5.409 |              21.235 |                0.893 |

  **Comparison to asymptotic bounds:**
  - **Selection sort** is $O(n^2)$ on every input, since it always scans the rest of the list to find the minimum. In both tables, doubling $n$ makes its time grow by roughly 4 times (for example 2.3 ms to 8.8 ms on random lists), which matches $O(n^2)$.
  - **Quicksort on random lists** (both pivot choices) is expected $O(n \lg n)$. Doubling $n$ makes the time grow by a little more than 2 times, which matches $n \lg n$. Both quicksorts are much faster than selection sort, and the gap grows as $n$ grows.
  - **Fixed-pivot Quicksort on sorted lists** hits its worst case, $O(n^2)$. When the first element is the pivot on a sorted list, it is always the smallest value, so one side of the split is empty and the other has $n-1$ elements. The time grows about 4 times each time $n$ doubles (5.0 ms to 21.2 ms), which matches $O(n^2)$.
  - **Random-pivot Quicksort on sorted lists** is still expected $O(n \lg n)$ and its times look just like the random-list case.

  **Effect of the input type:** On random lists, the two quicksorts perform about the same, and both beat selection sort. On sorted lists, fixed-pivot Quicksort becomes the slowest of the three, even slower than selection sort, because it does $O(n^2)$ work plus the extra cost of recursion and building new lists. Random-pivot Quicksort is not affected by the order of the input, because no particular input can force bad pivots. This shows why choosing a random pivot is useful: it avoids the worst case on common inputs like sorted lists. Selection sort's time barely changes with input type since it always does the same scanning. (Times on very small inputs are a little noisy.)


- **3c. (8 pts)** Compare the fastest of your sorting implementations to the Python sorting function `sorted`, conducting the tests in 3b above. 

  The fastest of my implementations is random-pivot Quicksort. All times are in milliseconds.

  **Random permutations** (`compare_timsort(shuffle=True)`):

  |       n |   qsort-random-pivot |   timsort |
  |---------|----------------------|-----------|
  |    1000 |                1.264 |     0.100 |
  |   10000 |               15.350 |     1.250 |
  |  100000 |              248.090 |    24.508 |
  | 1000000 |             3000.401 |   285.629 |

  **Already sorted lists** (`compare_timsort(shuffle=False)`):

  |       n |   qsort-random-pivot |   timsort |
  |---------|----------------------|-----------|
  |    1000 |                1.249 |     0.008 |
  |   10000 |               14.555 |     0.058 |
  |  100000 |              175.330 |     0.933 |
  | 1000000 |             2032.424 |     9.253 |

  **On random lists**, both algorithms grow like $O(n \lg n)$: when $n$ grows 10 times, both times grow a bit more than 10 times. Timsort is about **10 times faster** at every size. The growth rate is the same, so the difference is a constant factor. Timsort is written in C inside Python, while my Quicksort is written in Python and creates new lists at every recursive call, which adds a lot of overhead.

  **On sorted lists**, Timsort is about **200 times faster**. Random-pivot Quicksort still takes $O(n \lg n)$ time, but Timsort's time only grows about 10 times when $n$ grows 10 times, which is $O(n)$. This is because Timsort looks for runs of values that are already in order and merges them. A sorted list is one long run, so Timsort just checks it in one pass and is done.

  Overall, `sorted` (Timsort) is faster than my best Quicksort on both kinds of input, and it is especially fast on input that is already sorted or partly sorted.