class Rule():
    def applicable():
        pass
    def __init__(self, name):
        self.name = name


class Bastard(Rule):
    def applicable(child):
        global graph
        aux = graph.get('henryVIII')
        esposas = aux.get('spouse')
        mae = ''
        if(child in aux.get('parent')):
            for keys in graph.keys():
                if key != 'henryVIII' and child in key.get('parent'):
                    mae = key
        else:
            print("child not found")
            return
        if(mae in esposas):
            return False
        else:
            return True




graph = {
    'henryVIII': {
        'spouse': [
            'catherineparr', 'janeseymour', 'catherineofaragon', 'anneboleyn', 'catherinehoward', 'anneofcleves'
        ],
        'relationships' : [
            'catherineparr', 'janeseymour', 'catherineofaragon', 'anneboleyn', 'catherinehoward', 'anneofcleves',
            'isabelblount'
        ],
        'parent': [
            'henryfitzroy', 'elizabethI', 'maryI', 'edwardVI'
        ],
        'successor': [
            'edwardVI'
        ],
        'issue': [
            'henryfitzroy', 'elizabethI', 'maryI', 'edwardVI'
        ]
    },
    'henryVII': {
        'spouse': [
            'elizabethofyork'
        ],
        'parent': [
            'henryVIII'
        ],
        'sucessor': [
            'henryVIII'
        ]
    },
    'catherineofaragon': {
        'parent': [
            'maryI'
        ],
        'issue': [
            'maryI'
        ]
    },
    'anneboleyn': {
        'parent': [
            'elizabethI'
        ],
        'issue': [
            'elizabethI'
        ]
    },
    'janeseymour': {
        'parent': [
            'edwardVI'
        ],
        'issue': [
            'edwardVI'
        ]
    },
    'elizabethofyork': {
        'parent': [
            'henryVIII'
        ],
        'issue': [
            'henryVIII'
        ]
    },
    'maryI': {
        'sucessor': [
            'elizabethI'
        ]
    }
}
