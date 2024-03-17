def lunch_box_pack(menu: dict, budget: int):
    """
    Функція для упакування обідньої скриньки за допомогою жадібного алгоритму.

    Args:
        menu (dict): Словник предметів меню. Ключ - назва продукту, значення - словник з вартістю та калоріями.
        budget (int): Бюджет для упакування.

    Returns:
        tuple: Кортеж із вибраними предметами та загальними калоріями.
    """
    sorted_items = sorted(
        menu.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    total_items = []
    total_calories = 0
    for item in sorted_items:
        if budget >= item[1]["cost"]:
            total_items.append(item[0])
            budget -= item[1]["cost"]
            total_calories += item[1]["calories"]
    return (
        total_items,
        total_calories,
    )

def lunch_box_pack_dp(items: dict, budget: int):
    """
    Функція для упакування обідньої скриньки за допомогою динамічного програмування.

    Args:
        items (dict): Словник предметів меню. Ключ - назва продукту, значення - словник з вартістю та калоріями.
        budget (int): Бюджет для упакування.

    Returns:
        tuple: Кортеж із вибраними предметами та загальними калоріями.
    """
    n = len(items)
    items_list = list(items.items())

    # таблиця
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # знизу-вверх
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            # ліміт бюджету
            if items_list[i - 1][1]["cost"] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # максимальне значення
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - items_list[i - 1][1]["cost"]]
                    + items_list[i - 1][1]["calories"],
                )

    res = dp[n][budget]
    w = budget
    selected_items = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == dp[i - 1][w]:
            continue
        else:
            selected_items.append(items_list[i - 1][0])
            res -= items_list[i - 1][1]["calories"]
            w -= items_list[i - 1][1]["cost"]

    selected_items.reverse()

    return selected_items, dp[n][budget]

if __name__ == "__main__":
    items = {
        "піца": {"cost": 50, "calories": 300},
        "гамбургер": {"cost": 40, "calories": 250},
        "хот-дог": {"cost": 30, "calories": 200},
        "пепсі": {"cost": 10, "calories": 100},
        "кола": {"cost": 15, "calories": 220},
        "картопля": {"cost": 25, "calories": 350},
    }

    # Жадібний алгоритм
    budget = 50
    selected_items, total_calories = lunch_box_pack(items, budget)
    print(f"\n")
    print("ЖАДІБНИЙ АЛГОРИТМ:")
    print(f"Обрані страви: {selected_items}")
    print(f"Загально калорій: {total_calories}")
    print(f"\n")

    # Динамічне програмування
    budget = 85
    selected_items, total_calories = lunch_box_pack_dp(items, budget)
    print("ДИНАМІЧНЕ ПРОГРАМУВАННЯ:")
    print(f"Обрані страви: {selected_items}")
    print(f"Загально калорій: {total_calories}")
    print(f"\n")
