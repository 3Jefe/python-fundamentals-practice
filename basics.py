"""
Python fundamentals practice script.
Demonstrates basic data structures, control flow, functions,
file handling and simple object-oriented programming.
"""


def greet_user(name: str) -> str:
    """Return a simple greeting."""
    return f"Hello, {name}! Welcome to my Python practice script."


def calculate_average(numbers):
    """Return the average of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")
    return sum(numbers) / len(numbers)


def count_word_frequencies(text: str) -> dict:
    """
    Count how often each word appears in a piece of text.
    Very small example of basic text processing.
    """
    frequencies = {}
    for word in text.lower().split():
        word = word.strip(".,!?;:()[]\"'")
        if not word:
            continue
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


class Task:
    """Simple class representing a to-do task."""

    def __init__(self, title: str, completed: bool = False):
        self.title = title
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def __repr__(self):
        status = "✓" if self.completed else "✗"
        return f"<Task {status}: {self.title}>"


def demo_file_handling(filename: str = "example_output.txt") -> None:
    """
    Write a few lines to a text file and then read them back.
    Demonstrates basic file I/O.
    """
    lines_to_write = [
        "This is a demo file.",
        "Created as part of a Python fundamentals practice script.",
        "File handling is a useful skill in many projects.",
    ]

    # Write lines to file
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines_to_write:
            f.write(line + "\n")

    # Read them back
    print(f"\nContents of {filename}:")
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())


def main():
    print(greet_user("Parthiban"))

    numbers = [10, 15, 20, 25]
    avg = calculate_average(numbers)
    print(f"\nAverage of {numbers} is {avg:.2f}")

    sample_text = "Data analysis is fun. Data science builds on analysis."
    freqs = count_word_frequencies(sample_text)
    print("\nWord frequencies:")
    for word, count in freqs.items():
        print(f"  {word}: {count}")

    # Demonstrate simple object-oriented code
    tasks = [
        Task("Review Python basics"),
        Task("Read about data analysis"),
        Task("Prepare GitHub portfolio", completed=True),
    ]
    tasks[0].mark_complete()

    print("\nTasks:")
    for task in tasks:
        print(task)

    # File handling demo
    demo_file_handling()


if __name__ == "__main__":
    main()
