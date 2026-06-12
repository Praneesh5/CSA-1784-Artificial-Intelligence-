% Check if N is prime
prime(2).

prime(N) :-
    N > 2,
    \+ has_factor(N, 2).

% Check for factors
has_factor(N, F) :-
    N mod F =:= 0.

has_factor(N, F) :-
    F * F < N,
    F1 is F + 1,
    has_factor(N, F1).