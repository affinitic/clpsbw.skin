# -*- coding: UTF-8 -*-

from zope.component import adapts
from zope.interface import implements
from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField
from Products.ATContentTypes.content.newsitem import ATNewsItem
from Products.Archetypes.public import BooleanField, BooleanWidget


class GlobalField(ExtensionField, BooleanField):
    """
    """


class NewsExtender(object):
    adapts(ATNewsItem)
    implements(ISchemaExtender)

    fields = [
        GlobalField(
            name='isGlobal',
            required=False,
            languageIndependent=True,
            default=False,
            widget=BooleanWidget(
                description=u"Cochez cette case si l'actualite doit apparaitre parmi les actualites globales du site.",
                label=u"Actualité globale")),
        ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields