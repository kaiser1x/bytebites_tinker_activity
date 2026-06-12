+---------------------------+
|        Customer           |
+---------------------------+
| - name: String            |
| - purchaseHistory: Transaction[] |
+---------------------------+

+---------------------------+
|        FoodItem           |
+---------------------------+
| - name: String            |
| - price: Decimal          |
| - category: String        |
| - popularityRating: Int   |
+---------------------------+

+---------------------------+
|          Menu             |
+---------------------------+
| - items: FoodItem[]       |
+---------------------------+
| + filterByCategory(category: String): FoodItem[] |
+---------------------------+

+---------------------------+
|       Transaction         |
+---------------------------+
| - selectedItems: FoodItem[] |
+---------------------------+
| + computeTotal(): Decimal |
+---------------------------+