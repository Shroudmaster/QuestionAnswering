%% Ok, a principio estarei listando aqui a base das relacoes do Henrique
%% VII conforme a wikipedia
%% (https://pt.wikipedia.org/wiki/Henrique_VIII_de_Inglaterra). Vou
%% tentar fazer a principio so o grosso das relacoes familiares diretas
%% dele que eu e thiago olhamos na quinta.
%

/** Relacoes familiares diretas e legitimas */

/** Da king */

pai(HenriqueVII,HenriqueVIII). /** Favor manter a forma pai(Pai,Filho) */
mae(IsabeldeIorque, HenriqueVIII). /** Mesmo role */


/** Da Kings Children */

/** Catarina de Aragao */

pai(HenriqueVIII, Henrique).
pai(HenriqueVIII, Maria).
pai(HenriqueVIII, Henrique).  /** Tiveram dois henriques */
mae(CatarinadeAragao, Henrique).
mae(CatarinadeAragao, Maria).
mae(CatarinadeAragao, Henrique).

/** Ana Bolena */
pai(HenriqueVIII, Isabel).
pai(HenriqueVIII, Henrique).
mae(AnaBolena, Isabel).
mae(AnaBolena, Henrique).

/** Joana Seymour */

pai(HenriqueVIII, Eduardo).
mae(JoanaSeymour, Eduardo).



/** Isabel Blount */

pai(HenriqueVIII, Henrique).












