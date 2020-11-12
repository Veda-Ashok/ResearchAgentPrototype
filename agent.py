import random
acclimation_queue = []#tracks windows
sub_policies = [0, 1, 2, 3 ,4] #mock set of policies

# pick a policy
# get the first score
# if queue is not window size, add to queue
# if queue is window size, pop and push

#pick a random policy
def pick_policy():
    current_policy = random.choice(sub_policies)
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