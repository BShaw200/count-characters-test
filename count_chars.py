def count_non_whitespace_characters(filename):
    """
    Count the number of non-whitespace characters in a file.

    Args:
        filename: Path to the file to read

    Returns:
        Number of non-whitespace characters
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            # Count only non-whitespace characters
            count = sum(1 for char in content if not char.isspace())
            return count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


if __name__ == "__main__":
    filename = "test.txt"
    char_count = count_non_whitespace_characters(filename)

    if char_count is not None:
        print(f"Number of non-whitespace characters in '{filename}': {char_count}")
