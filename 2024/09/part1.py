# Made by ChatGPT - 2024-12-09
import argparse

def parse_disk_map(disk_map):
    """Parses the dense disk map into files and free space segments."""
    segments = []
    i = 0
    while i < len(disk_map):
        file_length = int(disk_map[i])
        free_length = int(disk_map[i+1]) if i + 1 < len(disk_map) else 0  # Handle odd-length input
        segments.append((file_length, free_length))
        i += 2
    return segments

def compact_disk(segments):
    """Compacts the disk by moving file blocks to the leftmost free spaces."""
    result = []
    file_id = 0
    for file_length, free_length in segments:
        result.extend([file_id] * file_length)
        result.extend(['.'] * free_length)
        if file_length > 0:
            file_id += 1
    
    # Perform the compacting operation
    compacted = [block for block in result if block != '.']
    compacted.extend(['.'] * result.count('.'))
    return compacted

def calculate_checksum(disk_blocks):
    """Calculates the checksum based on the compacted disk state."""
    checksum = sum(pos * int(block) for pos, block in enumerate(disk_blocks) if block != '.')
    return checksum

def main():
    parser = argparse.ArgumentParser(description="Solve Day 9: Disk Fragmenter")
    parser.add_argument("-f", "--file", required=True, help="Input file containing the disk map")
    args = parser.parse_args()

    # Read input file
    with open(args.file, 'r') as f:
        disk_map = f.read().strip()
    
    # Process disk map
    segments = parse_disk_map(disk_map)
    compacted_blocks = compact_disk(segments)
    checksum = calculate_checksum(compacted_blocks)
    
    # Display results
    print("Compacted Disk Blocks:")
    print("".join(str(x) for x in compacted_blocks))
    print(f"Checksum: {checksum}")

if __name__ == "__main__":
    main()
