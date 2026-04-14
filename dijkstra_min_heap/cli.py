import sys

import rich.box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console(highlight=False)

# User input graph in the form of an adjency matrix
def get_matrix_from_user():
    console.print(Panel(
        "Dijkstra-Min-Heap\n",
        box=rich.box.ASCII2,
    ))

    console.print("\nDefine your graph\n")

    # Input adjency matrix size
    while True:
        try:
            size = int(console.input("Enter the number of nodes in your graph: "))
            if size <= 0:
                console.print("Size must be a positive number. Try again.")
            else:
                break
        except ValueError:
            console.print("Invalid input. Please enter a whole number.")

    console.print(f"\nFill the adjacency matrix")
    console.print(f"Enter each row as {size} values separated by a space.")
    console.print(f"[white]Use 0 for no connection, any positive number for weight.[/white]\n")

    # Input adjency matrix values
    matrix = []
    for i in range(size):
        while True:
            try:
                row_input = console.input(f"Row {i} : ")
                row = list(map(int, row_input.split()))

                if len(row) != size:
                    console.print(f"Expected {size} values, got {len(row)}. Try again.")
                    continue

                if any(value < 0 for value in row):
                    console.print("Negative weights are not allowed. Try again.")
                    continue

                if row[i] != 0:
                    console.print(f"Diagonal value at position {i} must be 0. Try again.")
                    continue

                matrix.append(row)
                break

            except ValueError:
                console.print("Invalid input. Use whole numbers separated by spaces.")

    console.print(f"\nGraph defined successfully.\n")

    # display the table
    table = Table(
        title="Adjacency Matrix",
        box=rich.box.ASCII2,
        show_header=True
    )

    table.add_column("Node", justify="center")
    for i in range(size):
        table.add_column(str(i), justify="center")

    for i in range(size):
        row_values = []
        for value in matrix[i]:
            row_values.append("_" if value == 0 else str(value))
        table.add_row(str(i), *row_values)
 
    console.print(table)

    # picking source node
    while True:
        try:
            source = int(console.input(f"\nEnter source node (0 to {size - 1}): "))
            if source < 0 or source >= size:
                console.print(f"Source must be between 0 and {size - 1}. Try again.")
            else:
                break
        except ValueError:
            console.print("Invalid input. Try again.")

    console.print(f"\nSource node set to {source}.\n")

    # Choose destination node
    while True:
        try:
            destination = int(console.input(f"Enter destination node (0 to {size - 1}): "))
            if destination < 0 or destination >= size:
                console.print(f"Must be between 0 and {size - 1}. Try again.")
            elif destination == source:
                console.print("Destination must be different from source. Try again.")
            else:
                break
        except ValueError:
            console.print("Invalid input. Try again.")

    console.print(f"node {source} to node {destination}\n")

    return matrix, size, source, destination


def display_results(costs, previous, source, destination, matrix):
    console.print(Panel(
        f" Shortest path from node {source} to node {destination}",
        box=rich.box.ASCII2
    ))

    if costs[destination] == sys.maxsize:
        console.print(f"\nNo path found from node {source} to node {destination}.\n")
        return

    # Reconstruct the path by walking backwards
    path = []
    current = destination
    while current != -1:
        path.append(current)
        current = previous[current]

    path.reverse()

    console.print("\nPath:\n")
 
    table = Table(
        box=rich.box.ASCII2,
        show_header=True
    )

    table.add_column("Hop", justify="center")
    table.add_column("From", justify="center")
    table.add_column("To", justify="center")
    table.add_column("Weight", justify="center")
    table.add_column("Cumulative Cost", justify="center")

    # Walk through the path and display each hop
    for i in range(len(path) - 1):
        from_node = path[i]
        to_node   = path[i + 1]
 
        edge_weight     = matrix[from_node][to_node]
        cumulative_cost = costs[to_node]
 
        table.add_row(
            str(i + 1),
            f"Node {from_node}",
            f"Node {to_node}",
            str(edge_weight),
            str(cumulative_cost)
        )
 
    console.print(table)
    console.print(f"\nTotal cost: {costs[destination]}\n")