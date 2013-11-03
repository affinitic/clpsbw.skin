from plone.app.portlets.portlets.navigation import Renderer

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class MyNavRenderer(Renderer):
    
     _template = ViewPageTemplateFile('templates/navigation/navigation.pt')
     recurse = ViewPageTemplateFile('templates/navigation/navigation_recurse.pt')
