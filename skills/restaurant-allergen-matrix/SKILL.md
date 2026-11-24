---
name: restaurant-allergen-matrix
description: Build a per-dish allergen matrix from a recipe sheet, marking each of the 14 EU-declared allergens present, absent, or unknown. Use for menu allergen tables, staff briefings, and guest questions; not for confirming a dish is safe to eat, which needs the kitchen to check the current recipe and suppliers.
license: MIT
metadata:
  author: Heep
  version: "0.1.0"
---

# Build the allergen table you can defend

Turn a recipe sheet into a per-dish allergen matrix, with every cell either
present, absent, or unknown. Use the venue's language and its current recipes.
The output is a starting point for the kitchen to confirm, never a guarantee
for a guest.

## Work from recipes, not from dish names

An allergen comes from an ingredient, and only the recipe knows the ingredients.
A dish called "risotto" tells you nothing: the stock may carry celery and the
finishing butter milk. Ask for the recipe sheet, one ingredient per row, with
the allergens each ingredient declares.

The 14 allergens here are those of Regulation (EU) No 1169/2011, Annex II:
celery, crustaceans, eggs, fish, gluten, lupin, milk, molluscs, mustard, nuts,
peanuts, sesame, soybeans, and sulphites. Other markets list different ones, and
some ingredients carry more than a list covers — check the requirement that
applies where the venue trades rather than reusing this set.

Keep the allergens an ingredient declares separate from what it is. "Modified
starch" is not a validated allergen statement, and an ingredient nobody checked
is unknown, not free of anything. Declared "may contain" traces are a different
question from an ingredient, and they belong in the guest-facing note.

## Build the matrix

For a suitable CSV, use the bundled standard-library Python 3 helper:

```bash
python3 scripts/check_matrix.py /path/to/recipes.csv
```

Paths to bundled resources are relative to this skill directory. See the
[field contract and worked example](references/example.md), and the fictional
[sample recipe sheet](references/recipes.csv). The helper writes JSON to stdout
and never sends data or changes a recipe.

Each cell follows from the ingredients:

- **present** when any ingredient declares the allergen.
- **absent** only when every ingredient in the dish was checked and none
  declares it.
- **unknown** when an ingredient has no allergen data. A declared allergen stays
  present even then; the unknown only removes the claims of absence.

The order matters. One unchecked ingredient makes the dish unknown for
everything it did not settle, so a dish with a declared allergen and an
unchecked ingredient is still present for that allergen.

## Turn the matrix into action

Report the matrix, the dishes left incomplete, and the ingredients to check
first. Prioritize ingredients used in many dishes and dishes a guest would
reasonably assume are free of a common allergen. For the kitchen, the useful
output is a short list: which dishes are ready to publish, which need one
ingredient checked, and which need the recipe itself.

Absent is a claim about a recipe at a moment, not about a kitchen. Shared fryers,
shared utensils, and substitutions change what reaches the plate, and only the
kitchen can confirm those. Say so wherever the matrix is published.

The matrix is not medical advice and cannot confirm a dish is safe for a guest
with an allergy. Direct the guest to the venue's allergen process and a person
who can answer. Publishing a menu allergen table, changing a recipe, or
answering a guest on the venue's behalf requires the user's instruction for that
action.
