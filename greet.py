"""Simple greeting module."""

def greet(name: str) -> None:
    """Print a greeting with the given name."""
    print(f"Hello {name}")


if __name__ == "__main__":
    greet("World")
