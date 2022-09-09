"""L'acronyme CVE, pour Common Vulnerabilities and Exposures en anglais, désigne une liste publique de failles de sécurité informatique.
Lorsque l'on parle d'une CVE, on fait généralement référence à une faille de sécurité à laquelle un identifiant CVE a été attribué.

Le but de ce projet est d'analyser avec un programme qui se lance une fois par jour l'ensemble de vulnerabilités des librairies
utilisées par un projet IT (java, python etc.), selon un seuil de tolerance definit par les équipe de sécurité.

Lorsque le programme detecte une vulnerabilité supérieur au seuil de tolerence recommandé une alerte sous forme de mail est envoyé
à l'équipe IT en charge du projet
"""

import services.vulnerability_services as vulnerability_services
import models.db_persistence as persistence
import schedule
import time
if __name__ == '__main__':

    persistence.create_table()
    schedule.every(10).seconds.do(vulnerability_services.get_all_lib_vulnerability('log4j'))
    schedule.every(10).minutes.do(vulnerability_services.get_all_lib_vulnerability('numpy'))
    schedule.every().hour.do(vulnerability_services.get_all_lib_vulnerability('pandas'))
    schedule.every().day.at("10:30").do(vulnerability_services.get_all_lib_vulnerability('pip'))

    while True:
        schedule.run_pending()
        time.sleep(1)
