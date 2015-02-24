# -*- coding: utf-8 -*-
import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    URL_ROOT = 'http//localhost'
    LICENSE = 'https://creativecommons.org/licenses/by/4.0/'
    PUBLICATION_POLICY = 'http://donnees.ville.montreal.qc.ca/licence-2014/'
    PUBLISHER_ID_SCHEME = 'CA-CRA_ACR'
    PUBLISHER_ID = 'MTL'
    PUBLISHER_LEGAL_NAME = 'Ville de Montréal'
    PUBLISHER_NAME = 'Ville de Montréal'
    PUBLISHER_ADDRESS = ['275 Rue Notre-Dame Est, Montréal', 'Montréal', 'QC', 'H2Y 1C6', 'Canada']
    PUBLISHER_CONTACT = ['Bureau de la Ville Intelligente', 'villeintelligente@ville.montreal.qc.ca', '', '', 'http://ville.montreal.qc.ca/']

    OCID_PREFIX = 'ocds-a1234567-mt-'

    DATA_SOURCES = [
        {
            'name': 'Conseil Muncipal',
            'mapper': 'field_mapper_pol_mtl',
            'url': 'http://donnees.ville.montreal.qc.ca/dataset/6df93670-af44-492e-a644-72643bf58bc0/resource/a6869244-1a4d-4080-9577-b73e09d95ed5/download/contratsconseilmunicipal.csv'
        },
        {
            'name': 'Conseil d\'agglomeration',
            'mapper': 'field_mapper_pol_mtl',
            'url': 'http://donnees.ville.montreal.qc.ca/dataset/6df93670-af44-492e-a644-72643bf58bc0/resource/35e636c1-9f99-4adf-8898-67c2ea4f8c47/download/contratsconseilagglomeration.csv'
        }

    ]

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    URL_ROOT = 'https://ovc-stage.herokuapp.com'
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    

class TestingConfig(Config):
    TESTING = True
