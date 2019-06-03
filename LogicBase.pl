%% Ok, a principio estarei listando aqui a base das relacoes do Henrique
%% VII conforme a wikipedia
%% (https://pt.wikipedia.org/wiki/Henrique_VIII_de_Inglaterra). Vou
%% tentar fazer a principio so o grosso das relacoes familiares diretas
%% dele que eu e thiago olhamos na quinta.
%

/** Relacoes familiares diretas e legitimas */

/** Da king */

pai(henriqueVII,henriqueVIII). /** Favor manter a forma pai(Pai,Filho) */
mae(isabeldeIorque, henriqueVIII). /** Mesmo role */


/** Da Kings Children */

/** Catarina de Aragao */

pai(henriqueVIII, henrique).
pai(henriqueVIII, maria).
pai(henriqueVIII, henrique).  /** Tiveram dois henriques */
mae(catarinadeAragao, henrique).
mae(catarinadeAragao, maria).
mae(catarinadeAragao, henrique).

/** Ana Bolena */
pai(henriqueVIII, isabel).
pai(henriqueVIII, henrique).
mae(anaBolena, isabel).
mae(anaBolena, henrique).

/** Joana Seymour */

pai(henriqueVIII, eduardo).
mae(joanaSeymour, eduardo).



/** Isabel Blount */

pai(henriqueVIII, henrique).














