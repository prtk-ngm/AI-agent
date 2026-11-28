from datetime import datetime

from fastmcp import FastMCP
import random
import string
import secrets

mcp = FastMCP("Time Server")

@mcp.tool()

def current_time():

    """Return the current date and time."""

    return datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )


if __name__ == "__main__":
    print("I am here")
    print("Starting MCP server..")
    mcp.run()
    print("Starting MCP server started..")
