from state import (create_state, add_action, record_observation, next_step, finish, can_continue)

async def run_agent_loop(
    user_request,
    planner,
    execute_action,
    format_answer,
    tools,
    client
):
    # initialized state
    state = create_state(user_request)

    while can_continue(state):
        action = planner(state, tools)
        if action == "FINISH":
            answer = format_answer(state)
            finish(state, answer)
            print("Final state : ", state)
            break
        #execute the action
        observation = await execute_action(action, client)
        #add action
        add_action(state, action)
        record_observation(state, action, observation)
        next_step(state)
        print("Non final state : ", state)

    return state