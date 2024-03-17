import heapq
import matplotlib.pyplot as plt

def build_max_heap(nodes):
    """
    Функція для побудови максимальної бінарної купи з заданих вузлів.

    Args:
        nodes: Список вузлів, з яких будується купа.

    Returns:
        max_heap: Список, що представляє максимальну бінарну купу.
    """
    max_heap = []
    for item in nodes:
        heapq.heappush(max_heap, -item)
    return [-i for i in max_heap]

def draw_node(ax, node, pos, node_radius=0.5):
    """
    Функція для малювання вузла бінарного дерева.

    Args:
        ax: Вісь для малювання.
        node: Значення вузла.
        pos: Позиція вузла (координати).
        node_radius: Радіус вузла.

    Returns:
        None
    """
    circle = plt.Circle(pos, node_radius, color="yellow", ec="black", lw=1.5, zorder=4)
    ax.add_patch(circle)
    plt.text(*pos, int(node), ha="center", va="center", zorder=5)

def draw_line(ax, pos1, pos2):
    """
    Функція для малювання лінії між двома вузлами.

    Args:
        ax: Вісь для малювання.
        pos1: Початкова позиція лінії (координати першого вузла).
        pos2: Кінцева позиція лінії (координати другого вузла).

    Returns:
        None
    """
    line = plt.Line2D(
        [pos1[0], pos2[0]], [pos1[1], pos2[1]], color="green", lw=1.5, zorder=3
    )
    ax.add_line(line)

def plot_binary_tree(heap, ax, node_idx=0, pos=(0, 0), level=0, width=4):
    """
    Функція для малювання бінарного дерева.

    Args:
        heap: Бінарне дерево у вигляді списку.
        ax: Вісь для малювання.
        node_idx: Індекс поточного вузла у списку.
        pos: Початкова позиція поточного вузла.
        level: Рівень поточного вузла у дереві.
        width: Ширина дерева на поточному рівні.

    Returns:
        None
    """
    if node_idx >= len(heap):
        return

    # обчислення горизонтальної позиції, щоб зберегти баланс дерева
    x_offset = width / 2 ** (level + 0.5)
    left_child_idx = 2 * node_idx + 1
    right_child_idx = 2 * node_idx + 2

    draw_node(ax, heap[node_idx], pos)

    if left_child_idx < len(heap):
        # рухаємося вниз та вліво
        left_pos = (pos[0] - x_offset, pos[1] - 2)
        draw_line(ax, pos, left_pos)
        plot_binary_tree(heap, ax, left_child_idx, left_pos, level + 1, width)

    if right_child_idx < len(heap):
        # рухаємося вниз та вправо
        right_pos = (pos[0] + x_offset, pos[1] - 2)
        draw_line(ax, pos, right_pos)
        plot_binary_tree(heap, ax, right_child_idx, right_pos, level + 1, width)

if __name__ == "__main__":
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis("off")
    plt.xlim(-10, 10)
    plt.ylim(-10, 2)

    data = [20, 18, 15, 30, 10, 5, 7, 9, 8, 2, 1, 4, 6, 66]
    max_heap = build_max_heap(data)
    plot_binary_tree(max_heap, ax)
    plt.show()
