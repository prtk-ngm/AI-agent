from mcp_client import (
    connect,
    disconnect,
    discover_tools,
    execute_tool)


## Manager manages to get Tool ->Correct MCP Client -> Correct MCP Server

async def create_tool_registry(servers):
    print(servers)
    clients = []
    tool_registry = {}
    for server in servers:
        client = await connect(server)
        clients.append(client)
      
        tools = await discover_tools(client)
        ###Tool registry will have client and tool name and other information
        ### tool_registry = {"get_weather": { "client": client_for_weather_server, "tool":weather_tool_object }
    

        for tool in tools:
            tool_registry[tool.name] = {"client":client, "tool" : tool}

    return clients, tool_registry

async def close_servers(clients):
    for client in clients:
        await disconnect(client)



async def run_tool(
    tool_registry,
    tool_name,
    arguments
):

    entry = tool_registry.get(
        tool_name
    )

    if entry is None:

        raise ValueError(
            f"Unknown tool: {tool_name}"
        )

    return await execute_tool(
        entry["client"],
        tool_name,
        arguments
    )
