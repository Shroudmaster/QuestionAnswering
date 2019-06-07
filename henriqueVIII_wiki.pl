casou(henrique_viii,catarina_de_aragao).
casou(henrique_viii,ana_bolena).
casou(henrique_viii,joana_seymour).
casou(henrique_viii,ana_de_cleves).
casou(henrique_viii,catarina_howard).
casou(henrique_viii,catarina_parr).
pai(henrique_vii,henrique_viii).
pai(henrique_viii,henrique_fitzRoy).
pai(henrique_viii,maria_i).
pai(henrique_viii,isabel_i).
pai(henrique_viii,eduardo_i).
mae(isabel_blount,henrique_fitzRoy).
mae(ana_bolena,isabel_i).
mae(catarina_de_aragao,maria_i).
mae(joana_seymour,eduardo_i).
homem(eduardo_i).
homem(henrique_fitzRoy).
homem(henrique_viii).
homem(henrique_vii).
mulher(maria_i).
mulher(isabel_i).
relacionamento_amoroso(henrique_viii,isabel_blount).
relacionamento_amoroso(henrique_viii,catarina_de_aragao).
relacionamento_amoroso(henrique_viii,ana_bolena).
relacionamento_amoroso(henrique_viii,joana_seymour).
relacionamento_amoroso(henrique_viii,ana_de_cleves).
relacionamento_amoroso(henrique_viii,catarina_howard).
relacionamento_amoroso(henrique_viii,catarina_parr).
relacionamento_amoroso(henrique_viii,maria_bolena).


bastardo(X) :- pai(henrique_viii,X), mae(Y,X), \+ casou(henrique_viii,Y).
avo(X,Y) :- pai(X,Z),pai(Z,Y).
amante(X,Y) :- relacionamento_amoroso(Y,X), \+ casou(Y,X).
direito_ao_trono(X) :- homem(X),pai(henrique_viii,X),mae(Y,X),casou(henrique_viii,Y).

