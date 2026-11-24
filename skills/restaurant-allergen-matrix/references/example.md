# Example: three dishes, one ingredient nobody checked

## Try this request

> Build an allergen matrix from our three recipes. We publish the menu table next
> week. Do not change the recipes.

All data in [recipes.csv](recipes.csv) is fictional. One venue, EUR, no market
outside the EU is involved. The sheet has one ingredient per row and states the
allergens each ingredient declares. `none` means the ingredient was checked and
declares no allergen from the annex. `unknown` means nobody supplied a statement
for it.

## Recipe contract

The columns are `dish`, `ingredient`, `allergens`. `dish` and `ingredient` are
both required. `allergens` is `none`, `unknown`, a blank cell, or a
semicolon-separated subset of the 14 names in Regulation (EU) No 1169/2011,
Annex II, written in lower case:

`celery`, `crustaceans`, `eggs`, `fish`, `gluten`, `lupin`, `milk`, `molluscs`,
`mustard`, `nuts`, `peanuts`, `sesame`, `soybeans`, `sulphites`.

A name outside that list fails the run with its line number, because a typo in
an allergen cell is a wrong answer about a guest's safety rather than a cosmetic
problem. A blank cell is treated as unknown: an empty field is not a statement
that the ingredient is free of everything.

## Expected outcome

| Dish | Present | Unknown | Absent |
| --- | --- | --- | --- |
| Mushroom risotto | celery, milk | — | the other 12 |
| Lemon tart | eggs, gluten, milk | — | the other 11 |
| Fish and chips | eggs, fish, gluten, mustard | the other 10 | — |

Fish and chips is the case worth reading twice. Its seasoning blend has no
allergen statement, so the dish is unknown for everything that was not already
settled — but fish, gluten, eggs, and mustard stay **present**, because the cod,
the batter, the tartare sauce, and the mustard in it are ingredient facts that an
unchecked blend cannot undo. The risotto is complete only because its stock
declares celery and its parmesan and butter declare milk.

`dishes_incomplete` lists fish and chips, and `unknown_ingredients` names the
seasoning blend. The useful next step is one question to the supplier, not a
guess on the menu.

## What the matrix does not settle

Absent is a claim about the recipe supplied, not about the kitchen. The shared
fryer, the bread knife, and a substitution during service all change what reaches
the plate. The matrix also cannot answer a guest with an allergy: it says what the
recipe contains, and the venue's process decides what the kitchen can promise.
