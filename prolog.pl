% Example

% 1. Student Facts
student(rohan).
student(amit).
student(neha).


% 2. Family Relationships
parent(ram, shyam).
parent(shyam, mohan).
parent(ram, sita).
parent(sita, gita).

grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).


% 3. Male, Female, Father and Mother
male(ram).
male(shyam).
female(sita).
female(gita).

father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).


% 4. Sibling Relationship
sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.


% 5. Maximum of Two Numbers
maximum(X, Y, X) :-
    X >= Y.

maximum(X, Y, Y) :-
    Y > X.


% 6. Factorial Using Recursion
factorial(0, 1).

factorial(N, F) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, F1),
    F is N * F1.


% 7. Even and Odd
even(N) :-
    N mod 2 =:= 0.

odd(N) :-
    N mod 2 =:= 1.


% 8. List Membership
list_member(X, [X|_]).

list_member(X, [_|T]) :-
    list_member(X, T).


% 9. Animal Classification
animal(dog).
animal(cat).
animal(cow).

mammal(dog).
mammal(cat).
mammal(cow).

pet(dog).
pet(cat).

domestic(X) :-
    animal(X),
    mammal(X).


% 10. Student Result
marks(rohan, 85).
marks(amit, 72).
marks(neha, 91).

pass(X) :-
    marks(X, M),
    M >= 40.

distinction(X) :-
    marks(X, M),
    M >= 75.
