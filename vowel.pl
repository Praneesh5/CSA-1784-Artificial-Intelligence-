% Base case: Empty list has 0 vowels
count_vowels([], 0).

% If the head is a vowel
count_vowels([H|T], Count) :-
    member(H, [a, e, i, o, u]),
    count_vowels(T, Count1),
    Count is Count1 + 1.

% If the head is not a vowel
count_vowels([H|T], Count) :-
    \+ member(H, [a, e, i, o, u]),
    count_vowels(T, Count).