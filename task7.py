import numpy as np
import pandas as pd

num_rolls = 10000000

# Генерація випадкових кидків для двох кубиків
dice1_rolls = np.random.randint(1, 7, num_rolls)
dice2_rolls = np.random.randint(1, 7, num_rolls)

# Обчислення суми кидків
sums = dice1_rolls + dice2_rolls

# Підрахунок кількості випадків для кожної суми
sum_counts = pd.Series(sums).value_counts().sort_index()

# Обчислення ймовірностей для кожної суми
probabilities = sum_counts / num_rolls

# Створення DataFrame з результатами
results_df = pd.DataFrame(
    {
        "Сума": probabilities.index,
        "Кількість": sum_counts.values,
        "Вірогідність (%)": probabilities.values * 100,
    }
)

print(results_df)
