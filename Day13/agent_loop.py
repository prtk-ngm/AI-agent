from state import (create_state, add_action, record_observation, next_step, finish, can_continue)

async def run_agent_loop(
    user_request,
    planner,
    execute_action,
    format_answer,
    tools,
    tool_registry
):
    # initialized state
    state = create_state(user_request)

    while can_continue(state):
        action = planner(state, tools)
        print( "Planner selected next action:", action )
        if action["tool"] == "FINISH":
            answer = format_answer(state)
            finish(state, answer)
            print("Final state : ", state)
            break
        #execute the action
        observation = await execute_action(action, state, tool_registry)
        #add action
        add_action(state, action)
        record_observation(state, action, observation)
        next_step(state)
        print("Non final state : ", state)

    return state