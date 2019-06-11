from basegraph import graph as grafo


def check_if_is_spouse(person1, person2):
    return person2 in grafo[person1]["spouse"]


def check_if_has_relationship(person1, person2):
    return person2 in grafo[person1]["relationships"]


def check_if_is_child(person, parent):
    return person in grafo[parent]["parent"]


def check_if_is_bastard_kid(person1, person2):
    clause_is_child_of_spouse = False
    for spouse in grafo[person2]["spouse"]:
        try:
            clause_is_child_of_spouse = check_if_is_child(person1, spouse)
            if(clause_is_child_of_spouse == True):
                break;
        except KeyError:
            continue
    clause_is_child = check_if_is_child(person1, person2)
    #print(clause_is_child_of_spouse)
    print("Bastard: ",clause_is_child and not clause_is_child_of_spouse)
    return clause_is_child and not clause_is_child_of_spouse


def check_if_is_lover_of_henryVIII(person):
    clause_has_relationship = check_if_has_relationship("henryVIII", person)
    clause_is_spouse = check_if_is_spouse("henryVIII", person)
    print("Lover: ",clause_has_relationship and not clause_is_spouse)
    return clause_has_relationship and not clause_is_spouse


def check_if_is_is_granchild_of_henryVII(person):
    for child in grafo["henryVII"]["parent"]:
        if check_if_is_child(person, child):
            print("Grandchild: ",True)
            return True
    print("Grandchild: ",False)


def check_if_can_claim_throne(person):
    if not check_if_is_child(person, "henryVIII"):
        print(False)
        return False
    clause_is_legit_child = not check_if_is_bastard_kid(person, "henryVIII")
    clause_is_male = False
    if (grafo[person]["sex"] == 'male'):
        clause_is_male = True
    #print("H: ",grafo[person]["sex"])
    print("Can claim throne: ",clause_is_legit_child and clause_is_male)
    return clause_is_legit_child and clause_is_male


relations = {"bastard": check_if_is_bastard_kid,
             "lover": check_if_is_lover_of_henryVIII,
             "granchild": check_if_is_is_granchild_of_henryVII,
             "claim": check_if_can_claim_throne
             }
