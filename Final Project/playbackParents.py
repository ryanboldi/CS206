from individual import INDIVIDUAL
import pickle
import constants as c

f = open('parents1.p','rb')
parents = pickle.load(f)
f.close()

#parents.Evaluate(False, c.Max_dist)
best = parents.p[0]
best.Start_Evaluation(False, c.Max_dist)
best.Compute_Fitness()
print(best.fitness)