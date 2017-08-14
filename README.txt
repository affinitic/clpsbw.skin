ETAT DES EXPERIENCES
====================
private-by-auteur --> Brouillon auteur                       --> si l'auteur n'a pas fini
pending-by-auteur --> En demande de validation par l'auteur  --> l'auteur à fini et veur une validation par le clps
private-by-clps   --> Brouillon clps                         --> si le clps n'a pas fini
publish           --> Publié                                 --> l'expérience est publiée sur le site

ajout d'une experience par Auteur
      > experience_etat == private-by-auteur (si pas fini-)
      > experience_etat == pending-by-auteur (si fini et veut validation clps)
ou
ajout d'une experience par equipse Clps >
      > experience_etat == au choix de l'equipe
                                |--> private-by-clps
                                |--> private-by-auteur
                                |--> publish




ETAT DES RESSOUCES
==================
private --> Brouillon
pending --> En attente
publish --> Publié




ETAT DES INSTITUTION
==================
private --> Brouillon
publish --> Publié