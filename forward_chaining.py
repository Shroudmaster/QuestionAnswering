from basegraph import graph as grafo

def check_if_is_spouse(person1, person2):
    return person2 in grafo[person1]["spouse"]


def check_if_has_relationship(person1, person2):
    return person2 in grafo[person1]["relationships"]


def check_if_is_child(person, parent):
    return person in grafo[parent]["parent"]


def check_if_is_bastard_kid(person1, person2):
    for spouse in grafo[person2]["spouse"]:
        '''
        catherineparr não é um nó no dicionário, então, quando eu quero verificar os filhos dela, não encontra a chave
        '''
        if not check_if_is_child(person1, spouse):
            print(True)
            return True
        print(False)
    return False


def check_if_is_lover_of_henryVIII(person):
    clauseHasRelationship = check_if_has_relationship("henryVIII", person)
    clauseIsSpouse = check_if_is_spouse("henryVIII", person)
    print(clauseHasRelationship and not clauseIsSpouse)


def check_if_is_is_granchild_of_henryVII(person):
    for child in grafo["henryVII"]["parent"]:
        if check_if_is_child(person, child):
            print(True)
            return True
    print(False)


def check_if_can_claim_throne(person):
    print("claim %s" % person)


relations = {"bastard": check_if_is_bastard_kid,
             "lover": check_if_is_lover_of_henryVIII,
             "granchild": check_if_is_is_granchild_of_henryVII,
             "claim": check_if_can_claim_throne
             }
