import random
acclimation_queue = []#tracks windows
sub_policies = [[0, 1],[2, 3, 4],[5, 6, 7, 8]] #mock set of policies

# pick a policy
# get the first score
# if queue is not window size, add to queue
# if queue is window size, pop and push
# if all scores in queue are consistent, change policy


# QUESTIONS:
# Do we want to check within a variance for each score?
# How do we want to determine which policy is chosen?
#     - Have 2 or 3 subpolicies in 3 difficulty levels
#     - If score is consistent and high, pick policy from one level harder (unless they are already on the difficult level??)
#     - If score is medium, pick same level
#     - If score is low, pick lower level (unless they are already on the easy level??)


# How their score changes after changing policy
# How quickly they die
# Table of starting and ending policy --> track ave scores right before and after switch
# Map of tuples (policy, performance)

#pick a random policy
def pick_policy():
    print('picking policy')
    difficulty_level = 0
    if len(acclimation_queue) == 0:
        current_policy = random.choice(sub_policies[difficulty_level])
    elif acclimation_queue[0] >= 0.8:
        print('difficult')
        difficulty_level = 2
    elif acclimation_queue[0] >= 0.5 and acclimation_queue[0] < 0.7:
        print('medium')
        difficulty_level = 1
    elif acclimation_queue[0] < 0.5:
        print('easy')
        difficulty_level = 0
    current_policy = random.choice(sub_policies[difficulty_level])
    print('policy: ', current_policy)
    return current_policy

pick_policy() #pick starting policy

# track moving window
def store_score(c, p, w):
    if len(acclimation_queue) is w :
        acclimation_queue.pop(0)
    acclimation_queue.append(p/c)
    return acclimation_queue
    
# check if acclimated
def is_acclimated(q):
    acclimated = True
    if len(q) == 1:
        acclimated = False
        return acclimated
    for i in range(len(q)-1):
        if q[i] != q[i+1]:
            acclimated = False
            return acclimated     
    current_policy = pick_policy()  
    return acclimated



print(store_score(10, 9, 5))
print(is_acclimated(acclimation_queue))
print('\n')

print(store_score(10, 4, 5))
print(is_acclimated(acclimation_queue))
print('\n')

print(store_score(10, 3, 5))
print(is_acclimated(acclimation_queue))
print('\n')

print(store_score(10, 6, 5))
print(is_acclimated(acclimation_queue))
print('\n')

print(store_score(10, 8, 5))
print(is_acclimated(acclimation_queue))
print('\n')


print(store_score(10, 9, 5))
print(is_acclimated(acclimation_queue))
print('\n')

print(store_score(10, 9, 5))
print(is_acclimated(acclimation_queue))
print('\n')


print(store_score(10, 9, 5))
print(is_acclimated(acclimation_queue))
print('\n')


print(store_score(10, 9, 5))
print(is_acclimated(acclimation_queue))
print('\n')


print(store_score(10, 9, 5))
print(is_acclimated(acclimation_queue))
print('\n')


print(store_score(10, 4, 5))
print(is_acclimated(acclimation_queue))
print('\n')

print(store_score(10, 3, 5))
print(is_acclimated(acclimation_queue))
print('\n')

print(store_score(10, 2, 5))
print(is_acclimated(acclimation_queue))
print('\n')

print(store_score(10, 3, 5))
print(is_acclimated(acclimation_queue))
print('\n')

print(store_score(10, 3, 5))
print(is_acclimated(acclimation_queue))
print('\n')


print(store_score(10, 3, 5))
print(is_acclimated(acclimation_queue))
print('\n')


print(store_score(10, 3, 5))
print(is_acclimated(acclimation_queue))
print('\n')


print(store_score(10, 3, 5))
print(is_acclimated(acclimation_queue))
print('\n')