from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class ClpsbwskinLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import clpsbw.skin
        xmlconfig.file(
            'configure.zcml',
            clpsbw.skin,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')


CLPSBW_SKIN_FIXTURE = ClpsbwskinLayer()
CLPSBW_SKIN_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CLPSBW_SKIN_FIXTURE,),
    name="ClpsbwskinLayer:Integration"
)
CLPSBW_SKIN_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CLPSBW_SKIN_FIXTURE, z2.ZSERVER_FIXTURE),
    name="ClpsbwskinLayer:Functional"
)
