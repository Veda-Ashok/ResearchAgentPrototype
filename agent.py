import random
import statistics
acclimation_queue = []#tracks windows
performance_list = []
trajectory = []
sub_policies = [0, 1, 2, 3, 4] #mock set of policies

# How their score changes after changing policy
# How quickly they die
# Table of starting and ending policy --> track ave scores right before and after switch
# Map of tuples (policy, performance)

#pick a random policy
def pick_policy():
    if len(performance_list):
        current_policy = random.choice(sub_policies) 
    else:
        current_policy = 
    # print('policy: ', policy)
    return current_policy

current_policy = pick_policy() #pick_policy() #pick starting policy



# track moving window
def store_score(c, p, w):
    score = p/c
    trajectory.append(score)
    if len(acclimation_queue) is w:
        acclimation_queue.pop(0)
    acclimation_queue.append(score)
    return acclimation_queue

def calculate_standard_deviation(q):
    average = sum(q)/len(q)
    variance = sum([((x-average) ** 2) for x in q])/ len(q)
    return statistics.pstdev(q)

    
# check if acclimated
def is_acclimated(q, w):
    global current_policy 
    acclimated = False
    print('dev is: ', statistics.pstdev(q))
    if len(q) < w:
        return acclimated
    for i in range(len(q)):
        if q[i] <= q[0] + calculate_standard_deviation(q) and q[i] >= q[0] - calculate_standard_deviation(q):
            acclimated = True 
        else:
            acclimated = False
            return acclimated
    if acclimated == True:
        performance_list.append((current_policy, trajectory.copy()))  
        trajectory.clear()
        current_policy = pick_policy() 
    return acclimated


print('trajectory: ', trajectory)
print(store_score(10, 9, 5))
print(is_acclimated(acclimation_queue, 5))
print('performance: ', performance_list)
print('\n')


print('trajectory: ', trajectory)
print(store_score(10, 4, 5))
print(is_acclimated(acclimation_queue, 5))
print('performance: ', performance_list)
print('\n')


print('trajectory: ', trajectory)
print(store_score(10, 3, 5))
print(is_acclimated(acclimation_queue, 5))
print('performance: ', performance_list)
print('\n')


print('trajectory: ', trajectory)
print(store_score(10, 6, 5))
print(is_acclimated(acclimation_queue, 5))
print('performance: ', performance_list)
print('\n')


print('trajectory: ', trajectory)
print(store_score(10, 8, 5))
print(is_acclimated(acclimation_queue, 5))
print('performance: ', performance_list)
print('\n')


print('trajectory: ', trajectory)
print(store_score(10, 9, 5))
print(is_acclimated(acclimation_queue, 5))
print('performance: ', performance_list)
print('\n')


print('trajectory: ', trajectory)
print(store_score(10, 9, 5))
print(is_acclimated(acclimation_queue, 5))
print('performance: ', performance_list)
print('\n')


print('trajectory: ', trajectory)
print(store_score(10, 9, 5))
print(is_acclimated(acclimation_queue, 5))
print('performance: ', performance_list)
print('\n')


print('trajectory: ', trajectory)
print(store_score(10, 9, 5))
print(is_acclimated(acclimation_queue, 5))
print('performance: ', performance_list)
print('\n')


print('trajectory: ', trajectory)
print(store_score(10, 9, 5))
print(is_acclimated(acclimation_queue, 5))
print('performance: ', performance_list)
print('\n')


print('trajectory: ', trajectory)
print(store_score(10, 4, 5))
print(is_acclimated(acclimation_queue, 5))
print('performance: ', performance_list)
print('\n')


print('trajectory: ', trajectory)
print(store_score(10, 3, 5))
print(is_acclimated(acclimation_queue, 5))
print('performance: ', performance_list)
print('\n')


print('trajectory: ', trajectory)
print(store_score(10, 2, 5))
print(is_acclimated(acclimation_queue, 5))
print('performance: ', performance_list)
print('\n')


print('trajectory: ', trajectory)
print(store_score(10, 3, 5))
print(is_acclimated(acclimation_queue, 5))
print('performance: ', performance_list)
print('\n')


print('trajectory: ', trajectory)
print(store_score(10, 3, 5))
print(is_acclimated(acclimation_queue, 5))
print('performance: ', performance_list)
print('\n')

print('trajectory: ', trajectory)
print(store_score(10, 3, 5))
print(is_acclimated(acclimation_queue, 5))
print('performance: ', performance_list)
print('\n')


print('trajectory: ', trajectory)
print(store_score(10, 3, 5))
print(is_acclimated(acclimation_queue, 5))
print('performance: ', performance_list)
print('\n')


print('trajectory: ', trajectory)
print(store_score(10, 3, 5))
print(is_acclimated(acclimation_queue, 5))
print('performance: ', performance_list)
print('\n')