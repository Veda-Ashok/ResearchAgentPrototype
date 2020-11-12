import random
acclimation_queue = [] #tracks windows
sub_policies = [0, 1, 2, 3 ,4] #mock set of policies

#pick a random policy
def pick_policy():
    current_policy = random.choice(sub_policies)
    print('policy: ', current_policy)
    return current_policy

pick_policy() #pick starting policy

#Function to get score
def get_score(c, p, t): #c is total coins, p is collected coins
    score = p/c
    return score

# consistency, not threshold
# Window size
# implement queue (do not clear)

#check score against threshold and add to queue is it passes. Clear queue if it does not pass
def check_acclimation(c, p, t): #c is total coins, p is collected coins, t is threshold
    acclimated = False
    if len(acclimation_queue) < :

    print('length: ', len(acclimation_queue))
    return acclimation_queue

#check queue to decide of policy should be switched
def is_acclimated(q, w): #q is the queue (surprise), w is number of windows
    change_policy = False
    if len(q) == w:
        change_policy = True
        current_policy = pick_policy() #if acclimated, change policy (this uses random selection, but we can pick a different measure to decide policy)
                      #Example: we can have 3 sets of classification for level of difficulty of policy, and based on the score, or time it took to acclimate, we can
                      #pick a policy at a different level

        print('changing policy to: ', current_policy)
        acclimation_queue.clear()
    #return change_policy
    #print('change_policy: ', change_policy)
    return change_policy


print('is_acclimated: ', is_acclimated(acclimation_queue, 3))
print('\n')

check_acclimation(10, 3, 0.8)
print(acclimation_queue)
print('is_acclimated: ', is_acclimated(acclimation_queue, 3))
print('\n')


check_acclimation(10, 5, 0.8)
print(acclimation_queue)
print('is_acclimated: ', is_acclimated(acclimation_queue, 3))
print('\n')


check_acclimation(10, 9, 0.8)
print(acclimation_queue)
print('is_acclimated: ', is_acclimated(acclimation_queue, 3))
print('\n')

check_acclimation(10, 5, 0.8)
print(acclimation_queue)
print('is_acclimated: ', is_acclimated(acclimation_queue, 3))
print('\n')


check_acclimation(10, 8, 0.8)
print(acclimation_queue)
print('is_acclimated: ', is_acclimated(acclimation_queue, 3))
print('\n')

check_acclimation(10, 9, 0.8)
print(acclimation_queue)
print('is_acclimated: ', is_acclimated(acclimation_queue, 3))
print('\n')

check_acclimation(10, 9, 0.8)
print(acclimation_queue)
print('is_acclimated: ', is_acclimated(acclimation_queue, 3))
print('\n')

check_acclimation(12, 2, 0.8)
print(acclimation_queue)
print('is_acclimated: ', is_acclimated(acclimation_queue, 3))
print('\n')