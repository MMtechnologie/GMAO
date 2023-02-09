# GMAO

## Les Modeles

- Machines
	- id
	- names
	- etat de la machine
	- nb heure de maintenance

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
	-

- Technicien
	- id
	- name
	- disponibiliter
	- skill

## Fonctionalités

[x] Création de machine

[] Déclaration de panne

[] Affichage des panne

[] Affichage des panne non traité

[] Affichage des panne en cours 

[] Affichage des panne traité

[] Affichage des panne traité par machine

[] Crée une intervention currative

[] Affichage de l'intervention currative assigné a une panne


--------V2------------

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
