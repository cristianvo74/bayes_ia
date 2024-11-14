from modelo import modelo

# Calculemos la probabilidad para una observacion dada
probabilidad1 = modelo.probability([["ninguna", "no", "a tiempo", "atendida"]])
print(f"Probabilidad de la primera observación: {probabilidad1}")

# Calcular la probabilidad para 3 diferentes observaciones
observaciones = [
    ["suave", "si", "retrasada", "no atendida"],
    ["fuerte", "no", "a tiempo", "atendida"],
    ["ninguna", "si", "a tiempo", "no atendida"]
]

for i, observacion in enumerate(observaciones, start=2):
    probabilidad = modelo.probability([observacion])
    print(f"Probabilidad de la observación {i}: {probabilidad}")