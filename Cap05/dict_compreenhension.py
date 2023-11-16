dict_alunos = {"Bob": 68, "Michel": 84, "Pedro": 25, "Ana": 93}
dict_alunos_status = {
    k: ("Aprovado" if v > 70 else "Reprovado") for (k, v)
    in dict_alunos.items()
}
print(dict_alunos_status)
