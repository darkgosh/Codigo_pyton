'''Exercise with json strings ' loads ',' dumps  '
'''
import json
#import os
#print(os.getcwd())
#with open(r"g:\My Drive\Software_Projects\PROYECTOS\Curso_Python\RandomWebExcesices\JsonExercise\data.json", "r") as f:
with open("data.json","r") as f:
    data = json.load(f) 
print(data)