# CMPS 2200: Assignment 04

In this assignment we'll look at randomness in computation, both in theory and in practice.

To complete this assignment, follow the instructions in [assignment-04.md](assignment-04.md) ([PDF version](assignment-04.pdf)). Below you'll find important and useful information about submitting your work, using git, and testing your code. 

## Turning in your work
- Assignment are to be completed individually
- Put your name at the top of `main.py` and `answers.md`.
- Submit your completed assignment files to gradescope.
  - You only need to submit files you edited to complete this assignment.

## Running and testing your code
- You can run the tests using `pytest`. If you need to, install `pytest`. On your terminal:
  + `$ pip3 install pytest`
  + You may also have to install other python modules such as `tabulate` or other imported modules as you work through these recitations.
- It's usually best to run only one test at a time. To run tests, on a terminal, navigate into the directory holding your source, then execute:
  + `$ pytest main.py` to run all tests
  + `$ pytest main.py::test_one` to run `test_one`
  + If your computer can't find pytest after you've installed it, you can run pytest as follows:
    + `$ python -m pytest main.py`
    + `$ python -m pytest main.py::test_one`
  + Gradescope will test your implementation using the same `pytest`s that are written in `test_main`.

## Using Git
We **strongly** recommend using git for all recitations and assignments for this course.

To use git:
- [Clone] your Assignment repository to your local device.
- As you complete your work, `add`, `commit`, and `push` your changes to GitHub.
  + You can do this through your IDE, or if you're old school, through the terminal.
  + We recommend that you `add`, `commit`, and `push` your work often in order to regularly save your work to GitHub (this is a remote backup!).

## About Markdown

We use Markdown extensively in these assignments. Here is a [cheatsheet] for markdown syntax.

You can format mathematical expressions in markdown. To do so, wrap them in dollar signs and use [latex syntax] within the dollar signs. 

For example, the run time of our first example, linear search, this semester is $c_1n + c_2n + c_4 \in O(n)$. 

More generally, the runtime of any program can be expressed as:

$$\sum_i c_i * n_i$$

for every instruction $n_i$ and its cost $c_i$.

It's easy to do powers too. Euler's identity states: $e^{ix} + 1 = 0$

Pretty cool, huh?

You can convert from markdown to pdf. `convert.sh` is provided for you to convert your `answers.md` to `answers.pdf`. As the comment in the script says, you will need to install pandoc and latex, but its worth it! You do not need to submit your answers in PDF format, but you may if you like.

[Clone]: https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository
[cheatsheet]: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
[latex syntax]: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions
