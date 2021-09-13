# Algorithm E
## Euclid's algorithm

E1. [Find remainder.] Divide _m_ by _n_ and let _r_ be the remainder. (We
    will have 0 ≤ _r_ < _n_.)

E2. [Is it zero?] If _r_ = 0, the algorithm terminates; _n_ is the answer.

E3. [Reduce.] Set _m_ <= _n_, _n_ <= _r_, and go back to step E1.
