% Facts
has_wings.
cannot_fly.

can_fly :-
    has_wings.

bird(penguin) :-
    cannot_fly.

bird(eagle) :-
    can_fly.

% Forward chaining rule
infer(X) :-
    bird(X).