from cli import get_matrix_from_user, display_results
from dijkstra import dijkstra
 
if __name__ == "__main__":
    matrix, size, source, destination = get_matrix_from_user()
    costs, previous = dijkstra(matrix, size, source)
    display_results(costs, previous, source, destination, matrix)