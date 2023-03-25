<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a>
    <img src="https://forgemia.inra.fr/uploads/-/system/project/avatar/4253/kisspng-django-web-development-web-framework-python-softwa-django-5b45d914274e46.055745571531304212161.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Application Django - projet python avancée</h3>

  <p align="center">
    (URCA - Université de Reims Champagne Ardennes)
  </p>
</div>

<!-- Table des matières -->
<details>
  <summary>Table des matières</summary>
  <ol>
    <li>
      <a href="#a-savoir">A savoir</a>
      <ul>
        <li><a href="#dependance">Dépendances</a></li>
      </ul>
    </li>
    <li>
      <a href="#premier-demarrage">Premier démarrage</a>
      <ul>
        <li><a href="#prerequis">Prerequis</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#equipe-projet">Equipe projet</a></li>
    <li><a href="#cadre">Cadre</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## A savoir

Il s'agit ici d'un projet de python avancée correspondant à la description suivante :

<strong>Projet 8 : Création d’un site web de traitement de données ( Django + Scikitlearn + Bokeh) - 3 étudiants</strong>
Le but de ce projet est de créer un site web avec la librairie Django. Des méthodes de réduction
de dimensions et des méthodes de clustering seront implémentées avec la librairie Scikitlearn. L’utilisateur pourra charger le ou les fichiers de données, sélectionner le traitement
désiré. Les méthodes de la librairie Scikit-learn seront appliquées aux données. Les résultats
seront affichés sous le format adéquat en utilisant la librairie Bokeh sur le site. D’autres
fonctionnalités peuvent être ajoutées selon les besoins. 

Site démonstration : <a href="http://www.alexandre-emery.fr/">Lien</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Dependance
Dans cette section, voici les dépendances utilisés par l'outil, à noter que certaines dépendances pourront être installées directement après le clonage à l'aide d'un fichier de dépendances qui vous est fournis.

Necessaire avant installation
* Python3
* Pip

Présent dans le fichier de configuration requirement.sh
* Django
* Libmysqlclient-dev
* Mysqlclient
* Bokeh
* Scikit-learn

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Premier Demarrage

Lancer le projet pour la premiere fois, voici les quelques règles à respecter pour que l'installation se passe bien.

### Prerequis

* python3 et pip
  ```sh
  sudo apt install python3 python3-pip
  ```
  
* Vérifier l'installation
  ```sh
  sudo python3 --version
  ```

### Installation

<strong>Comment installer l'application</strong>

1. Créer le dossier dans lequel vous voulez placer l'application
2. Cloner le repo GitHub
   ```sh
   sudo git init
   sudo git clone [https://github.com/your_username_/Project-Name.git](https://github.com/Alexouilleuuuh/my-django-app.git)
   ```
3. Placer vous dans le dossier my-django-app
4. Installer les packages necessaires
   ```sh
   sudo sh requirements.sh
   ```
5. Lancer l'application en localhost
   ```sh
   sudo sh run.sh
   ```
    ou
   ```sh
   sudo python3 manage.py runserver
   ```
   
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Vous pouvez maintenant tester le bon fonctionnement de l'application à l'adresse <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Equipe -->
## Equipe projet

Les membres de l'équipe projet :
<strong>Interface Django</strong>
* EMERY Alexandre

<strong>Version 1 - application</strong>
* COTTIGNY Thomas (Scikit-learn)
* CAILLAUX Antoine (Bokeh)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CADRE -->
## Cadre

(URCA) Université de Reims Champagne Ardennes
Module python avancée - année 2022/2023

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Mail : alexandre.emery@etudiant.univ-reims.fr

<p align="right">(<a href="#readme-top">back to top</a>)</p>
