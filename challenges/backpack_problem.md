
# Backpack Problem

**🎯 Optimize the value of a heist.**

![Burglar](../images/burglar.png)

A burglar broke into a villa. There he finds so many valuables that he can't put them all in his backpack. Write a program that makes an optimal selection.

The burglar is an experienced professional who can estimate the market value and size of each item in no time:

| item  | size  | value |
|-------|-------|-------|
| laptop | 2  | 600,- |
| cutlery | 2 | 400,- |
| spotify speakers | 3  | 300,- |
| jewels | 2 | 1100,- |
| vase | 5 | 700,- |
| camera | 2 | 500,- |
| painting | 4 | 900,- |
| cash | 1 | 800,- |

The backpack has a capacity of `8`.

When your program manages to pack items worth `3000`, it can be used as an app for amateur burglars.

## Hints

* the optimal solution uses **dynamic programming**.

Use the following pseudocode:

1. create an empty list that will include the best combination(s) of items for each backpack size
2. insert an empty combination for a size 0 backpack
3. start with a size 1 backpack
4. copy the best combination for the current size from the previous size, store it as `current best`
5. go through all objects
6. create a new combination usign an item plus the best combination for the space remaining
7. if the combination is more valuable than the `current best`, replace `current best` by the new combination
8. if the combination is worth the same amount, save both
8. increase the size of the backpack by 1
9. repeat step 4 until you reach the desired size
10. print the best combination for the desired size


*Translated with [www.DeepL.com](www.DeepL.com/Translator)*
