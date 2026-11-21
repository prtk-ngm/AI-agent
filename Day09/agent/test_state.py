from state import *

state = create_state("Generate the password and tell me current time")
add_action(state, "generate_password")

record_observation(state, "generate_password", "Password: #@kedgh")
print("\nIntial state : " , state)
next_step(state)

print("\nState after one iteration : " , state)

finish(state, "Password: #@kedgh\nCurrent Time: 10:35 AM")

print("\n Finish state:", state)