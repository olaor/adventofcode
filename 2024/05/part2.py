# Made by ChatGPT on 2024-12-05

import argparse
from collections import defaultdict, deque

def parse_input(file_path):
    """
    Parse the input file into ordering rules and updates.
    :param file_path: Path to the input file.
    :return: A tuple (rules, updates)
    """
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')
    
    rules = []
    updates = []
    parsing_updates = False

    for line in lines:
        if not line.strip():
            parsing_updates = True
            continue
        if parsing_updates:
            updates.append(list(map(int, line.split(','))))
        else:
            x, y = map(int, line.split('|'))
            rules.append((x, y))
    
    return rules, updates

def is_update_correct(update, rules):
    """
    Check if the update satisfies the given ordering rules.
    :param update: List of pages in the update.
    :param rules: List of (X, Y) tuples representing X|Y rules.
    :return: True if the update is in the correct order, False otherwise.
    """
    index_map = {page: i for i, page in enumerate(update)}
    
    for x, y in rules:
        if x in index_map and y in index_map:
            if index_map[x] > index_map[y]:
                return False
    return True

def reorder_update(update, rules):
    """
    Reorder an update according to the ordering rules.
    :param update: List of pages in the update.
    :param rules: List of (X, Y) tuples representing X|Y rules.
    :return: A reordered update as a list.
    """
    # Build a directed graph based on the rules
    graph = defaultdict(list)
    in_degree = {page: 0 for page in update}

    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            in_degree[y] += 1

    # Perform a topological sort
    sorted_order = []
    queue = deque([page for page in update if in_degree[page] == 0])

    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order

def find_middle_page(update):
    """
    Find the middle page number of the update.
    :param update: List of pages in the update.
    :return: The middle page number.
    """
    return update[len(update) // 2]

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Solve the Day 5 Print Queue puzzle.")
    parser.add_argument('-f', '--file', required=True, help="Input file containing the rules and updates.")
    args = parser.parse_args()

    # Parse the input file
    rules, updates = parse_input(args.file)

    # Handle incorrectly-ordered updates
    total_middle_sum = 0
    for update in updates:
        if not is_update_correct(update, rules):
            corrected_update = reorder_update(update, rules)
            total_middle_sum += find_middle_page(corrected_update)
    
    print(f"The sum of middle pages from correctly reordered updates is: {total_middle_sum}")

if __name__ == "__main__":
    main()
