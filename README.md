# ByteBites

A campus food-ordering system built from scratch as a spec-first OOP design exercise. See [bytebites_spec.md](bytebites_spec.md) for the feature request and [bytebites_design.md](bytebites_design.md) for the class diagram.

## Reflection Summary

The main idea is composition over inheritance: a Menu has FoodItems and a Transaction has selected items, so these should be “has-a” relationships, not “is-a.” Students usually get stuck on figuring out which class should do what, like totals vs filtering. AI is useful for setting up basic class structures and diagrams, but it can overcomplicate things by adding extra classes or wrong inheritance. A good way to help students is to have them explain a full order step by step to see where their design is unclear.
