+------------------------------+
|          Customer            |
+------------------------------+
| - name: String               |
| - purchase_history: Transaction[] |
+------------------------------+

+------------------------------+
|          FoodItem            |
+------------------------------+
| - name: String               |
| - price: Decimal             |
| - category: String           |
| - popularity_rating: Int     |
+------------------------------+

+------------------------------+
|            Menu              |
+------------------------------+
| - items: FoodItem[]          |
+------------------------------+
| + filter_by_category(category: String): FoodItem[] |
| + sort_by_popularity(): FoodItem[] |
+------------------------------+

+------------------------------+
|         Transaction          |
+------------------------------+
| - selected_items: FoodItem[] |
+------------------------------+
| + calculate_total(): Decimal |
+------------------------------+

Relationships:
Customer "1" --> "*" Transaction
Menu "1" --> "*" FoodItem
Transaction "*" --> "*" FoodItem