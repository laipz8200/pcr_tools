from app.utils.priconne_data import _PriconneData


NAME2ID = {}

def gen_name2id():
    NAME2ID.clear()
    for k, v in _PriconneData.CHARA.items():
        for s in v:
            if s not in NAME2ID:
                NAME2ID[normname(s)] = k


def normname(name:str) -> str:
    name = name.lower().replace('（', '(').replace('）', ')')
    return name


def name2id(name):
    name = normname(name)
    if not NAME2ID:
        gen_name2id()
    return NAME2ID[name] if name in NAME2ID else 1000


def id2name(c_id):
    return _PriconneData.CHARA[c_id][0]
