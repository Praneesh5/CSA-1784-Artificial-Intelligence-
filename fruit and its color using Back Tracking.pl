fruit(apple, red).
fruit(banana, yellow).
fruit(grape, purple).
fruit(orange, orange).
fruit(watermelon, green).

match_fruit_color(Fruit, Color) :-
    fruit(Fruit, Color).

fruits_with_color(FruitList, Color) :-
    findall(F, match_fruit_color(F, Color), FruitList).