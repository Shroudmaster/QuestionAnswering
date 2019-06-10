class Forward_chaining():
    def __init__(self, graph):
        self.graph = graph

    def bastard(child):
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
        'sex': 'male',
        'relationships': [
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
        'sex': 'male',
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
        'sex': 'female',
        'issue': [
            'maryI'
        ]
    },
    'anneboleyn': {
        'parent': [
            'elizabethI'
        ],
        'sex': 'female',
        'issue': [
            'elizabethI'
        ]
    },
    'janeseymour': {
        'parent': [
            'edwardVI'
        ],
        'sex': 'female',
        'issue': [
            'edwardVI'
        ]
    },
    'elizabethofyork': {
        'parent': [
            'henryVIII'
        ],
        'sex': 'female',
        'issue': [
            'henryVIII'
        ]
    },
    'maryI': {
        'sucessor': [
            'elizabethI'
        ],
        'sex': 'female'
    },
    'edwardVI': {
        'sex': 'male'
    }
}
