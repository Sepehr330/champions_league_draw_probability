import pandas as pd
import csv
import numpy as np
import random
class Team :
    def __init__(self , name , country , number):
        self.name = name
        self.country = country
        self.number = number
def prob_calc(S1,S2):
    global prob_table
    global total
    random.shuffle(S2)
    for i in range(8):
        if S1[i].number == S2[i].number or S1[i].country == S2[i].country :
            return 0
    total += 1
    for j in range(8):
        a = S1[j].number
        b = S2[j].number
        prob_table[a][b] += 1
    if total == 1:
        for i in range(8):
            print(f'{S1[i].name} vs {S2[i].name}')
def champ16(seed):
    Arr = list()
    for i in range(len(seed)):
        Arr.append(Team(seed.values[i][0] , seed.values[i][1] , i))
    return Arr
prob_table = np.zeros([8,8])
total = 0
df = pd.read_excel('teams.xlsx')
seed1 = df[["seed1","country1"]]
seed2 = df[["seed2" , "country2"]]
S1 = champ16(seed1)
S2 = champ16(seed2)
while total < 100000 :
    prob_calc(S1,S2)
prob_table = prob_table/1000
print(prob_table)
with open("prob_table.csv" , "w" , newline="") as File :
    writer = csv.writer(File)
    seed1_val = pd.DataFrame(seed1).T.values.tolist()
    seed2_val = pd.DataFrame(seed2).T.values.tolist()
    SS1 = list(seed1_val[0])
    SS2 = list(seed2_val[0])
    SS2.insert(0,'x')
    writer.writerow(SS2)
    for i in range(8):
        arr_prob = list(prob_table[i])
        arr_prob.insert(0,SS1[i])
        writer.writerow(arr_prob)
File.close()