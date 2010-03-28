from transaction import commit
from Products.Five import zcml
from Products.Five import fiveconfigure
from Testing.ZopeTestCase import app, close, installPackage
from Products.CMFCore.utils import getToolByName
from Products.PloneTestCase.layer import PloneSite

class JHelpdeskLayer(PloneSite):
    @classmethod
    def setUp(cls):
        fiveconfigure.debug_mode = True
        import qi.jabberHelpdesk
        zcml.load_config('configure.zcml', qi.jabberHelpdesk)
        zcml.load_config('overrides.zcml', qi.jabberHelpdesk.tests)
        fiveconfigure.debug_mode = False    
        installPackage('qi.jabberHelpdesk',quiet=True)
        # import the default profile
        root = app()
        portal = root.plone
        tool = getToolByName(portal, 'portal_setup')
        profile = 'profile-qi.jabberHelpdesk:default'
        tool.runAllImportStepsFromProfile(profile, purge_old=False)
        # and commit the changes
        commit()
        close(root)
        
    @classmethod
    def tearDown(cls):
        pass