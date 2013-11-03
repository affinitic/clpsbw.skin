# -*- coding: utf-8 -*-
"""
clpsbw.skin

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl

$Id: viewlets.py 2141 2008-04-26 17:25:10Z laz $
"""
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import GlobalSectionsViewlet
from zope.component import getMultiAdapter

class ClpsbwSectionsViewlet(GlobalSectionsViewlet):
    render = ViewPageTemplateFile('templates/header_footer/headerClpsbw.pt')

    def logo_tag(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                        name=u'plone_portal_state')
        portal = portal_state.portal()
        logoName = portal.restrictedTraverse('base_properties').logoName
        return portal.restrictedTraverse(logoName).tag()


class ClpsbwFooterViewlet(GlobalSectionsViewlet):
    render = ViewPageTemplateFile('templates/header_footer/footerClpsbw.pt')
