import matplotlib.pyplot as plt
import numpy as np

def draw_branch(ax, origin, angle, length, depth):
    """
    Функція для малювання гілок дерева Піфагора.

    Args:
        ax: Вісь для малювання.
        origin: Початкова точка гілки.
        angle: Кут, під яким відхиляється гілка.
        length: Довжина гілки.
        depth: Глибина рекурсії.

    Returns:
        None
    """
    if depth == 0:
        return None

    # обчислення кінцевої точки гілки
    end = (
        origin[0] + length * np.cos(np.radians(angle)),
        origin[1] + length * np.sin(np.radians(angle)),
    )

    ax.plot([origin[0], end[0]], [origin[1], end[1]], "k-", lw=2)

    new_length = length * 0.8

    # рекурсивні виклики для двох нових гілок
    draw_branch(ax, end, angle - 45, new_length, depth - 1)
    draw_branch(ax, end, angle + 45, new_length, depth - 1)

def pythagoras_tree(depth=5):
    """
    Функція для створення дерева Піфагора за допомогою рекурсії.

    Args:
        depth: Глибина рекурсії (кількість рівнів гілок).

    Returns:
        None
    """
    _, ax = plt.subplots()

    # встановлення відповідності сторін для коректного відображення кутів
    ax.set_aspect("equal")
    ax.axis("off")
    origin = (0.0, 0.0)  # початкова точка дерева

    # початковий кут
    angle = 90

    # початкова довжина гілки
    length = 40
    draw_branch(ax, origin, angle, length, depth)

    ax.set_xlim(-100, 100)
    ax.set_ylim(0, 150)

    plt.show()

if __name__ == "__main__":
    depth = int(input("Введіть глибину рекурсії: "))
    pythagoras_tree(depth)
