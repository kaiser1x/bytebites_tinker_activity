# ByteBites

A campus food-ordering system built from scratch as a spec-first OOP design exercise. See [bytebites_spec.md](bytebites_spec.md) for the feature request and [bytebites_design.md](bytebites_design.md) for the class diagram.

## Reflection Summary

The main idea students needed to understand was composition over inheritance. A Menu contains a list of FoodItem objects, and a Transaction contains a list of selected items, so these are “has-a” relationships rather than “is-a” relationships. Students often struggled with deciding which class should be responsible for different tasks, such as whether calculating a total belongs in Transaction or Menu. AI was helpful for quickly creating class scaffolds, constructors, and UML diagrams from the project requirements. However, AI sometimes made the design more complicated by adding extra classes or using inheritance when it was not needed. The custom agent became more useful once clear constraints were added to keep it focused on the assignment requirements. To help a student who is stuck, I would ask them to explain the steps of a customer placing an order, since that usually makes design problems easier to spot.
