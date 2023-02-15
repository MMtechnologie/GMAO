# GMAO

## Les Modeles

- Machines
	- id
	- names
	- etat de la machine
	- nb heure de maintenance

- Panne
	- id
	- description
	- machine (foreignkey)
	- type de panne
	- etat de la demande
	- date/heure

- Intervention Currative
	- id
	- description
	- nb heure d'arret
	- panne (foreignkey)
	- technicien en charge

### -----V2-------


- Interventions Préventive
	- id
	- description
	- occurence
	- machine (foreignkey)

- Taches
	- id
	- description
	- intervention (foreignkey)
	- ? prorité ?

- Technicien
	- id
	- name
	- disponibiliter
	- skill

- Site
  - id
  - mame
  - kbis

- Machine
  - ajout de site (foreignkey)



## Fonctionalités

[x] Création de machine

[x] Déclaration de panne

[x] Affichage des panne

[x] Suppression de panne

[x] Prise en charge de panne

[] Affichage des panne non traité

[] Affichage des panne en cours 

[] Affichage des panne traité

[] Affichage des panne traité par machine

[] Crée une intervention currative

[] Affichage de l'intervention currative assigné a une panne

[] Intégration d'un chat bot :
	[] Déclaration d'une panne
	[] Proposition de maintenace niveau 1 aprés déclaration.
	[] Création d'une panne si maintenance niv 1 inefficace ou pas de mainteanance niv 1

[] Mise en place d'un portail d'authentification :
	[] Si pas d'authentification page chat bot
	[] Si authentification maintenance accées a tout les volets du menu
	[] Si authentification opérateur accées a la liste des pannes en cours

[] Envoie de mail a la création de panne

[] Création d'un pdf a la cloture d'une panne et a l'édition du curatif

### -----V2-------

[] Création de tache

[] Création d'intervention préventive

[] Ajout de tache dans une intervention préventive

[] Planification d'une intervention préventive

[] Affichage des interventions plannifiées sur un temps donné

[] Affichage des interventions plannifiées sur une machine 

[] Affichage des taches a réaliser sur une intervention préventive

[] Assigné une intervention préventive a un tech

[] Affichage des interventions préventive assigné a 1 tech

[] Assigné une panne a un tech
