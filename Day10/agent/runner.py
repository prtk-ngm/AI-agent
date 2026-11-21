import asyncio

from mcp_client import (
    connect,
    disconnect,
    discover_tools
)

from planner import planner
from executor import execute_action
from agent_loop import run_agent_loop
from answer import format_answer


async def main():

    client = await connect()

    tools = await discover_tools(
        client
    )

    print("\nAvailable Tools")
    for tool in tools:
        print("\n * ", tool.name)

    user_request = input(
        "\nUser : "
    )

    state = await run_agent_loop(
        user_request,
        planner,
        execute_action,
        format_answer,
        tools,
        client
    )

    print("\nFinal Answer:")
    print(
        state["final_answer"]
    )
    await disconnect(client)


if __name__ == "__main__":
    asyncio.run(main())



