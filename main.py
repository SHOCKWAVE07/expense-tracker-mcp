import random
from fastmcp import FastMCP

mcp = FastMCP(name="Demo Server")

@mcp.tool
def roll_dice(n_dice: int = 1) -> list[int]:
    """Roll a dice with the specified number of sides."""
    return [random.randint(1, 6) for _ in range(n_dice)]

@mcp.tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

if __name__ == "__main__":
    mcp.run()