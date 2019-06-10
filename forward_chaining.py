from basegraph import graph as grafo

'''
ainda to trabalhando em cima de como resolver isso aqui
mas minha ideia basica é sempre chamar o metodo forward_chaining nas regras
'''

def check_if_is_bastard_kid(person1, person2):
    relations = grafo[person2]
    # print(relations)
    print("bastard %s, %s" % (person1, person2))

def check_if_is_lover_of_henryVIII(person):
    clauseHasRelationship = person in grafo["henryVIII"]["relationships"]
    clauseIsSpouse = person in grafo["henryVIII"]["spouse"]
    print(clauseHasRelationship and not clauseIsSpouse)

def check_if_is_is_granchild_of_henryVII(person):
    print("granchild %s" % person)

def check_if_can_claim_throne(person):
    print("claim %s" % person)

'''
achei legal criar um dicionário de métodos pra facilitar na hora de chamar as regras
'''
relations = {"bastard": check_if_is_bastard_kid,
             "lover": check_if_is_lover_of_henryVIII,
             "granchild": check_if_is_is_granchild_of_henryVII,
             "claim": check_if_can_claim_throne
             }
