%% Ok, a principio estarei listando aqui os fatos, dados como as
%% relacoes do grafo de conhecimento obtido a partir de
%% http://lodmilla.sztaki.hu/lodmilla/?url=http%3A%2F%2Fdbpedia.org%2Fresource%2FHenry_VIII_of_England
%% e seus predicados e pa
%
spouse(X,Y):-
    spouse(Y,X).
sucessor(X,Y):-
    predecessor(Y,X).

spouse(henryVIII,catherineOfAragon).
spouse(henryVIII,anneBoleyn).
spouse(henryVIII,janeSeymour).
spouse(henryVIII,catherineParr).
spouse(henryVIII,catherineHoward).
spouse(henryVIII,anneOfCleves).
spouse(henryVII,elizabethOfYork).

successor(henryVII,henryVIII).
successor(henryVIII,edwardVI).

religion(catholic).
religion(anglican).

parent(henryVIII,maryI).
parent(catherineOfAragon,maryI).
parent(henryVIII,elizabethI).
parent(anneBoleyn,elizabethI).
parent(henryVIII,edwardVI).
parent(janeSeymour,edwardVI).
parent(henryVIII,henryFitzRoy).
