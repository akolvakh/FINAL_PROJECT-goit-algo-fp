import heapq
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def dijkstra(graph: dict, start):
    """
    Реалізація алгоритму Дейкстри для пошуку найкоротших шляхів у графі.

    Args:
        graph: Граф у форматі словника з вагами ребер.
        start: Початкова вершина для обчислення найкоротших шляхів.

    Returns:
        distances: Словник, що містить найкоротші відстані до всіх вершин від заданої початкової вершини.
    """

    # Ініціалізуємо всі вершини як нескінченно віддалені
    distances = {vertex: float("infinity") for vertex in graph}

    # Відстань до початкової вершини дорівнює 0
    distances[start] = 0

    # Використовуємо пріоритетну чергу для ефективного вибору наступної вершини для розгляду
    # Початкове значення відстані та вершини
    priority_queue = [(0, start)]

    while priority_queue:
        # Вибираємо вершину з мінімальною відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо поточна відстань більша за раніше обчислену, пропускаємо вершину
        if current_distance > distances[current_vertex]:
            continue

        # Розглядаємо всіх сусідів поточної вершини та оновлюємо їх відстані, якщо знайдено коротший шлях
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Додаємо вершину у чергу для подальшого розгляду
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def visualize_graph(graph, shortest_distances, start_node):
    """
    Функція для візуалізації направленого графа з позначенням найкоротших шляхів від заданої початкової вершини.

    Args:
        graph: Граф у форматі словника з вагами ребер.
        shortest_distances: Словник, що містить найкоротші відстані до всіх вершин від заданої початкової вершини.
        start_node: Початкова вершина, від якої розраховані найкоротші шляхи.

    Returns:
        None
    """
        
    # Створюємо направлений граф
    G = nx.DiGraph()

    # Додаємо вершини та ребра графу
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    # Визначаємо розташування вершин на колі
    pos = nx.circular_layout(G)
    # pos = nx.random_layout(G)

    # Малюємо граф
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="yellow", font_size=12, font_weight="bold")

    # Підписуємо вершини з відстанями від початкової вершини
    labels = {node: f"({start_node} -> {node}: {shortest_distances[node]})" for node in graph}
    
    # Зміщуємо підписи від вершин
    label_pos = {k: v + np.array([0, 0.08]) for k, v in pos.items()}
    nx.draw_networkx_labels(G, label_pos, labels=labels, font_color='red')

    # Відмічаємо початкову вершину
    nx.draw_networkx_nodes(G, pos, nodelist=[start_node], node_color='green', node_size=1000)

    # Додаємо ваги на ребрах
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')

    plt.title("Граф з найкоротшими шляхами від вершини " + start_node)
    plt.show()

if __name__ == "__main__":
    graph = {
        "A": {"B": 5, "C": 10},
        "B": {"A": 5, "D": 3},
        "C": {"A": 10, "D": 2},
        "D": {"B": 3, "C": 2, "E": 4},
        "E": {"D": 4, "F": 2},
        "F": {"E": 2},
    }

    start_node = "A"
    shortest_distances = dijkstra(graph, start_node)
    print("Найкоротша відстань від ноди", start_node + ":", shortest_distances)
    visualize_graph(graph, shortest_distances, start_node)
