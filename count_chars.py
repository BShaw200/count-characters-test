from collections import Counter


def count_non_whitespace_characters(filename):
    """
    Count the number of non-whitespace characters in a file and find the most common character.

    Args:
        filename: Path to the file to read

    Returns:
        Tuple of (total_count, most_common_char, most_common_count) or (None, None, None) on error
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            # Filter only non-whitespace characters
            non_whitespace_chars = [char for char in content if not char.isspace()]
            count = len(non_whitespace_chars)

            # Find the most common character
            if non_whitespace_chars:
                char_frequencies = Counter(non_whitespace_chars)
                most_common_char, most_common_count = char_frequencies.most_common(1)[0]
            else:
                most_common_char, most_common_count = None, 0

            return count, most_common_char, most_common_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None, None, None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None, None, None


if __name__ == "__main__":
    filename = "test.txt"
    char_count, most_common_char, most_common_count = count_non_whitespace_characters(filename)

    if char_count is not None:
        print(f"Number of non-whitespace characters in '{filename}': {char_count}")
        if most_common_char:
            print(f"Most common character: '{most_common_char}' (appears {most_common_count} times)")
