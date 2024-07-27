'''Exercise with json strings ' loads ',' dumps  '
'''
import json

with open("g:/My Drive/Software_Projects/PROYECTOS/Curso_Python/RandomWebExcesices/JsonExercise/data.json","r") as f:
    data = json.load(f) 
print(data.items())

with open("g:/My Drive/Software_Projects/PROYECTOS/Curso_Python/RandomWebExcesices/JsonExercise/data2.json","w") as f:
    json.dump(data,f) 
