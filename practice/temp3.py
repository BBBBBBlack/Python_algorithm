"""
Assingment P3 - CSCI 3482

Author: Swaraj Shrestha

Program to implement value iteration and policy iteration to solve the MDP problem.

"""

import gym as gym
import numpy as np
import gym_examples

# You need this part
# S:Start, F:Frozen, H:Hole, G:Goal
# map = ["SFFF", "FHFH", "FFFF", "HFFG"]
# is_slippery=True means stochastic and is_slippery=False means deterministic
# FrozenLake-v1
# gym_examples/GridWorld-v0
env = gym.make('gym_examples/GridWorld-v0', render_mode="human", map_name="8x8", is_slippery=False)
env.reset()
env.render()

# You need to find the policy using both value iteration and policy iteration
# You may not need this part!
action = ["left", "down", "right", "up"]
ncols = 8
nrows = 8
e = 0.001
# max_iterations = 10000  # maximum iterations if there is an infinite loop

# GIVEN
# A sample policy to make the following while loop works
# policy = [1, 2, 1, 0, 1, 0, 1, 0, 2, 1, 1, 1, 0, 2, 2, 0]

#  Initializing the variables
n_states = env.observation_space.n  # the total number of states in the environment
n_actions = env.action_space.n  # number of possible actions in the environment
gamma_list = [0.8]  # substitute with ('0.5' and '1')

'''
This function implements the value iteration algorithm to compute the optimal policy.

It initializes the state value function (V) for all states to 0 and then iteratively updates the values until they converge to the optimal values.
The loop continues until the maximum change in any value is less than the error threshold (e).

Parameters
----------
env : an object of a Gym environment class
    Given environment

gamma : float
    Discount factor

e : float
    Error threshold

Returns
-------
policy
    1-D NumPy array of integers
    Each element in the array represents the best action to take in the corresponding state to maximize the expected cumulative reward
    The optimal policy

'''


def value_iteration(env, gamma, e):
    V = np.zeros(n_states)

    # check for convergence
    # runs until 'delta' is less than a predefined value 'e'
    while True:
        delta = 0  # the maximum absolute difference between the old value of a state v and the new value V[s] computed in the current iteration
        for s in range(n_states):
            v = V[s]
            q_vals = np.zeros(n_actions)
            for a in range(n_actions):
                for p, s_next, r, done in env.P[s][a]:
                    q_vals[a] += p * (r + gamma * V[s_next])
                V[s] = max(q_vals)
            delta = max(delta, abs(v - V[s]))
        if delta < e:
            break
    policy = np.zeros(n_states, dtype=int)
    for s in range(n_states):
        q_vals = np.zeros(n_actions)
        for a in range(n_actions):
            for p, s_next, r, done in env.P[s][a]:
                q_vals[a] += p * (r + gamma * V[s_next])
            policy[s] = np.argmax(q_vals)
    return policy


'''
This function implements the policy iteration algorithm to compute the optimal policy.

It initializes a random policy for all states, then iteratively evaluates and improves the policy until convergence.
In the evaluation step, it computes the state values for the given policy until they converge to the optimal values.
In the improvement step, it updates the policy for each state by selecting the action that maximizes the expected value of the next state.

Parameters
----------
env : an object of a Gym environment class
    Given environment

gamma : float
    Discount factor

e : float
    Error threshold

Returns
-------
policy
    1-D NumPy array of integers
    Each element in the array represents the best action to take in the corresponding state to maximize the expected cumulative reward.
    The optimal policy.

'''


def policy_iteration(env, gamma, e):
    num = 0  # to check for the iterations
    policy = np.zeros(n_states, dtype=int)
    print()
    print("policy:", policy)  # Add print statement to see policy at each step
    print()
    while True:
        V = np.zeros(n_states)
        while True:
            delta = 0
            # if num > max_iterations:   # stops iteration at 1000 but the GUI hangs
            #    break                
            for s in range(n_states):
                v = V[s]
                a = policy[s]
                q_val = 0
                for p, s_next, r, done in env.P[s][a]:
                    q_val += p * (r + gamma * V[s_next])
                V[s] = q_val
                delta = max(delta, abs(v - V[s]))
            num += 1  # increment to keep count
            print("V: " + str(num))
            print(V.reshape(8, 8))  # Add print statement to see V values at each step
            if delta < e:
                break
        policy_stable = True

        # check for convergence
        # old policy at each state is saved in 'old_action', and then the Q-values for each action at the state are evaluated using the updated 
        # value function 'V'. The policy is then updated to choose the action with the highest Q-value, and if the updated policy at any state 
        # is different from the old policy, then policy_stable is set to False.
        for s in range(n_states):
            old_action = policy[s]
            q_vals = np.zeros(n_actions)
            for a in range(n_actions):
                for p, s_next, r, done in env.P[s][a]:
                    q_vals[a] += p * (r + gamma * V[s_next])
            policy[s] = np.argmax(q_vals)
            if old_action != policy[s]:
                policy_stable = False
        if policy_stable:  # if 'policy_stable' remains True after the loop, then the policy is considered to have converged and the iteration loop is broken
            break
        print()
        print("policy:", policy)  # Add print statement to see policy at each step
        print()
    return policy


# Loop to print out the optimal policies:
# Both policies are represented as arrays of integers, with each index corresponding to a state in the environment and the value at that 
# index representing the action to be taken in that state according to the optimal policy
for gamma in gamma_list:
    print("gamma: ", gamma)
    value_policy = value_iteration(env, gamma,
                                   e)  # the optimal policy obtained by running the value iteration algorithm on the environment
    print("Value iteration policy:", value_policy)
    print()
    policy_policy = policy_iteration(env, gamma,
                                     e)  # the optimal policy obtained by running the policy iteration algorithm on the environmeny
    print()
    print("Policy iteration policy:", policy_policy)
    print()
    print("------------------------")

# GIVEN
# This part uses the found policy to interact with the environment.
# You don't need to change anything here.

s = 0
goal = ncols * nrows - 1
while s != goal:
    a = value_policy[s]
    s, r, t, f, p = env.step(a)
    if t == True and s != goal:
        env.reset()
        s = 0
print("END")
print("------------------------")
