from fastmcp import Client


async def connect(server):

    """
    Connect to the MCP Server.
    """

    client = Client(server)

    await client.__aenter__()

    print(f"Connected to MCP {server}")

    return client


async def disconnect(client):

    """
    Close the MCP connection.
    """

    await client.__aexit__(
        None,
        None,
        None
    )


async def discover_tools(client):

    """
    Retrieve all tools from the server.
    """

    tools = await client.list_tools()

    return tools


async def execute_tool(
    client,
    tool_name,
    arguments=None
):

    if arguments is None:
        arguments = {}

    return await client.call_tool(
        tool_name,
        arguments
    )

