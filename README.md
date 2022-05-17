# **Minitel**

Minitel est un dossier dont le contenu, en Python, permet de récupérer différentes informations.

## **Installation** 

Allez sur GitLab, cliquez sur la case Clone et cela vous ouvre une petite fenêtre avec Clone with SSH.

A côté du lien, cliquez sur une petite icône qui copie le lien.

Sur votre terminal, vous utilisez git clone pour récupérer le minitel
```bash
git clone "votre lien clone"
```

## **Execution**

Ouvrez le dossier minitel en cliquant dessus ou avec:
```bash
cd minitel
```
Le fichier qui nous intéresse est le main.py.

Faites:
```bash
python3 main.py
```

Ou clic droit sur le fichier main.py et cliquez sur exécuter le script Python dans un terminal.

Cela vous dirige vers une interface avec un menu.
Déplacez vous avec les flèches directionnelles et Entrée pour intéragir.

Dans Infos générales, vous trouverez: 
- le système d'exploitation et sa version
- le Kernel et sa version
- la limite de fichiers ouverts
- la date où le système a été redémarré pour la dernière fois
- le nom de votre CPU
- les capacités de votre mémoire
- les capacités de votre disque dur


Dans Réseaux, il y a votre IP

Dans Processus, il y aura:
- le PID
- le Nom
- le Status
- le Parent ID
- le pourcentage CPU
- le pourcentage MEM