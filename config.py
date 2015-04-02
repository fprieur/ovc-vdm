# -*- coding: utf-8 -*-
import os


class Config(object):
    DEBUG = False
    TESTING = False
    SENDMAIL = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

    if 'EMAIL_CREDENTIALS' in os.environ:
        EMAIL_CREDENTIALS = tuple(os.environ['EMAIL_CREDENTIALS'].split('@'))
    
    SMTP_SERVER = 'smtp.sendgrid.net'
    EMAIL_SENDER = 'ovc@opennorth.ca'
    ADMINS = ['stephane@opennorth.ca']

    URL_ROOT = 'http//localhost'
    OCID_PREFIX = 'ocds-a1234567-mt-'

    CACHE_DURATION = 86400
    STATS_LOG = 'stats/log.out'

    START_HIGHLIGHT = "<em>"
    END_HIGHLIGHT = "</em>"

    DATA_SOURCES = [
        {
            'name': 'Conseil Muncipal',
            'mapper': 'field_mapper_pol_mtl',
            'url': 'http://donnees.ville.montreal.qc.ca/dataset/6df93670-af44-492e-a644-72643bf58bc0/resource/a6869244-1a4d-4080-9577-b73e09d95ed5/download/contratsconseilmunicipal.csv',
            'type': 'contract'
        },
        {
            'name': 'Comité éxecutif',
            'mapper': 'field_mapper_pol_mtl',
            'url': 'http://donnees.ville.montreal.qc.ca/dataset/505f2f9e-8cec-43f9-a83a-465717ef73a5/resource/87a6e535-3a6e-4964-91f5-836cd31099f7/download/contratscomiteexecutif.csv',
            'type': 'contract'
        },        
        {
            'name': 'Conseil d\'agglomeration',
            'mapper': 'field_mapper_pol_mtl',
            'url': 'http://donnees.ville.montreal.qc.ca/dataset/6df93670-af44-492e-a644-72643bf58bc0/resource/35e636c1-9f99-4adf-8898-67c2ea4f8c47/download/contratsconseilagglomeration.csv',
            'type': 'contract'
        },
        {
            'name': 'Conseil Muncipal',
            'mapper': 'field_mapper_subvention_mtl',
            'url': 'http://donnees.ville.montreal.qc.ca/dataset/067c3bf6-0ec0-4159-a582-b0d58b44491f/resource/3abb3596-45fb-4c80-8d6f-1633db5427d4/download/subventionsconseilmunicipal.csv',
            'type': 'subvention'
        }          
    ]

    SUPPLIER_SIZE = [0, 100000, 10000000]

    SERVICE_TO_ACTIVITY = {
        # NO SEMI_COLUMN - PAS DE POINT-VIRGULE
        "ARRONDISSEMENT DE MONTRÉAL-NORD": ["Arrondissements"],
        "ARRONDISSEMENT DE RIVIÈRE-DES-PRAIRIES–POINTE-AUX-TREMBLES": ["Arrondissements"],
        "ARRONDISSEMENT DE LASALLE" : ["Arrondissements"],
        "ARRONDISSEMENT DE PIERREFONDS-ROXBORO" : ["Arrondissements"],
        "ARRONDISSEMENT DE VERDUN": ["Arrondissements"],
        "ARRONDISSEMENT DE SAINT-LAURENT": ["Arrondissements"],
        "ARRONDISSEMENT LE SUD-OUEST": ["Arrondissements"],
        "ARRONDISSEMENT DE ROSEMONT-LA PETITE-PATRIE": ["Arrondissements"],
        "ARRONDISSEMENT DE SAINT-LÉONARD": ["Arrondissements"],
        "ARRONDISSEMENT DE VILLE-MARIE": ["Arrondissements"],
        "ARRONDISSEMENT DE LACHINE" : ["Arrondissements"],
        "ARRONDISSEMENT D'AHUNTSIC-CARTIERVILLE" : ["Arrondissements"],
        "ARRONDISSEMENT DE MERCIER-HOCHELAGA-MAISONNEUVE" : ["Arrondissements"],
        "ARRONDISSEMENT DE CÔTE-DES-NEIGES-NOTRE-DAME-DE-GRÂCE" : ["Arrondissements"],
        "ARRONDISSEMENT DE VILLERAY-SAINT-MICHEL-PARC-EXTENSION" : ["Arrondissements"],
        "SERVICE DES TECHNOLOGIES DE L'INFORMATION" : ["Gestion de l'information"],
        "SERVICE DE LA GESTION ET DE LA PLANIFICATION IMMOBILIÈRE": ["Organisation et administration"],
        "SERVICE DE POLICE DE MONTRÉAL": ["Sécurité publique"],
        "SERVICE DES INFRASTRUCTURES, DU TRANSPORT ET DE L'ENVIRONNEMENT" : ["Transport","Environnement"],
        "SERVICE DE CONCERTATION DES ARRONDISSEMENTS ET DES RESSOURCES MATÉRIELLES": ["Organisation et administration"],
        "SERVICE DE LA MISE EN VALEUR DU TERRITOIRE": ["Urbanisme et habitation"],
        "SERVICE DE LA QUALITÉ DE VIE" : ["Sports, loisirs, culture et développement social"],
        "SERVICE DE L'EAU" : ["Infrastructures"],
        "SERVICE DES AFFAIRES INSTITUTIONNELLES": ["Organisation et administration"],
        "SERVICE DES INFRASTRUCTURES, DE LA VOIRIE ET DES TRANSPORTS" : ["Infrastructures"],
        "DIRECTION GÉNÉRALE" : ["Organisation et administration"],
        "SERVICE DE L'ESPACE POUR LA VIE": ["Sports, loisirs, culture et développement social"],
        "SERVICE DE L'APPROVISIONNEMENT": ["Ressources matérielles et services"],
        "SERVICE DE LA DIVERSITÉ SOCIALE ET DES SPORTS" : ["Sports, loisirs, culture et développement social"],
        "SERVICE DES GRANDS PARCS, DU VERDISSEMENT ET DU MONT ROYAL": ["Sports, loisirs, culture et développement social"],
        "SOCIÉTÉ DU PARC JEAN-DRAPEAU": ["Sports, loisirs, culture et développement social"],
        "SERVICE DE SÉCURITÉ INCENDIE DE MONTRÉAL" : ["Sécurité publique"],
        "SERVICE DES FINANCES" : ["Ressources financières"],
        "SERVICE DU CAPITAL HUMAIN ET DES COMMUNICATIONS" : ["Ressources humaines", "Communications et relations publiques"],
        "SERVICE DES AFFAIRES JURIDIQUES ET DE L’ÉVALUATION FONCIÈRE" : ["Juridique", "Foncier"],
        "BUREAU DU VÉRIFICATEUR GÉNÉRAL" : ["Organisation et administration"],
        "SERVICE DU MATÉRIEL ROULANT ET DES ATELIERS" : ["Ressources matérielles et services"],
        "SERVICE DES RESSOURCES HUMAINES": ["Ressources humaines"]

    }


class ProductionConfig(Config):
    DEBUG = False
    SENDMAIL = True

    ADMINS = ['stephane@opennorth.ca', 'daniel.drouet@ville.montreal.qc.ca']

class StagingConfig(Config):
    URL_ROOT = 'https://ovc-stage.herokuapp.com'
    SENDMAIL = True
    DEVELOPMENT = False
    DEBUG = False

class DevelopmentConfig(Config):
    URL_ROOT = 'http://localhost:5000'
    DEVELOPMENT = True
    DEBUG = True
    

class TestingConfig(Config):
    TESTING = True
    SUPPLIER_SIZE = [0, 100000, 10000000]

    DATA_SOURCES = [
        {
            'name': 'Conseil Municipal',
            'mapper': 'field_mapper_pol_mtl',
            'url': 'fixtures/contracts.csv',
            'type': 'contract'
        },
         {
            'name': 'Conseil Municipal',
            'mapper': 'field_mapper_subvention_mtl',
            'url': 'fixtures/subventions.csv',
            'type': 'subvention'
        },       
    ]
