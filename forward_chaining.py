from basegraph import graph as grafo

'''
ainda to trabalhando em cima de como resolver isso aqui
mas minha ideia basica é sempre chamar o metodo forward_chaining nas regras
'''

def forward_chaining(regra):
    for item in grafo:
        print("%s %s" % (item,  grafo[item]))
    pass

def check_if_is_bastard_kid(person1, person2):
    relations = grafo[person2]
    print(relations)


def check_if_is_lover_of_henryVIII(person):
    pass


def check_if_is_is_granchild_of_henryVII(person):
    pass

def check_if_can_claim_throne(person):
    pass

'''
achei legal criar um dicionário de métodos pra facilitar na hora de chamar as regras
'''
relations = {"bastard": check_if_is_bastard_kid,
             "lover": check_if_is_lover_of_henryVIII,
             "granchild": check_if_is_is_granchild_of_henryVII,
             "claim": check_if_can_claim_throne
             }
