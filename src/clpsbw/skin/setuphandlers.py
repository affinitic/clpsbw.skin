# -*- coding: utf-8 -*-

from zope.component import getUtility
from zope.component import getMultiAdapter
#from zope.interface import alsoProvides
from plone.portlets.constants import CONTEXT_CATEGORY
from plone.portlets.interfaces import IPortletManager, \
                                      IPortletAssignmentMapping, \
                                      ILocalPortletAssignmentManager
from plone.app.portlets.portlets import classic
from plone.app.portlets.portlets import navigation
from Products.CMFCore.utils import getToolByName


def setupClpsbw(context):
    if context.readDataFile('clpsbw.skin_various.txt') is None:
        return
    portal = context.getSite()
    #clearPortlets(portal)
    deleteFolder(portal, 'Members')
    setupNavigationPortlet(portal)
    setupClassicPortlet(portal, 'portlet_projet_partage', 'left')
    setupClassicPortlet(portal, 'portlet_plate_forme', 'left')
    updateSecurity(portal)


def setupNewFolder(portal, folder, idFolder, titleFolder, descriptionFolder, indexFolder):
    newFolder = createFolder(folder, idFolder, titleFolder, descriptionFolder)
    changeFolderView(portal, newFolder, indexFolder)
    return newFolder


def createFolder(parentFolder, folderId, folderTitle, folderDescription=''):
    if folderId not in parentFolder.objectIds():
        parentFolder.invokeFactory('Folder', folderId, title=folderTitle,
                                   description=folderDescription)
    createdFolder = getattr(parentFolder, folderId)
    publishObject(createdFolder)
    createdFolder.reindexObject()
    return createdFolder


def deleteFolder(portal, folderId):
    folder = getattr(portal, folderId, None)
    if folder is not None:
        portal.manage_delObjects(folderId)


def changeFolderView(portal, newFolder, viewname):
    addViewToType(portal, 'Folder', viewname)
    if newFolder.getLayout() != viewname:
        newFolder.setLayout(viewname)


def addViewToType(portal, typename, templatename):
    pt = getToolByName(portal, 'portal_types')
    foldertype = getattr(pt, typename)
    available_views = list(foldertype.getAvailableViewMethods(portal))
    if not templatename in available_views:
        available_views.append(templatename)
        foldertype.manage_changeProperties(view_methods=available_views)


def publishObject(obj):
    portal_workflow = getToolByName(obj, 'portal_workflow')
    if portal_workflow.getInfoFor(obj, 'review_state') in ['visible', 'private']:
        portal_workflow.doActionFor(obj, 'publish')
    return


def clearPortlets(folder):
    clearColumnPortlets(folder, 'left')
    clearColumnPortlets(folder, 'right')


def clearColumnPortlets(folder, column):
    manager = getManager(folder, column)
    assignments = getMultiAdapter((folder, manager), IPortletAssignmentMapping)
    for portlet in assignments:
        del assignments[portlet]
    assignable = getMultiAdapter((folder, manager), ILocalPortletAssignmentManager)
    assignable.setBlacklistStatus(CONTEXT_CATEGORY, True)

def setupClassicPortlet(folder, template, column):
    #Add classic portlet (using template) to folder
    manager = getManager(folder, column)
    assignments = getMultiAdapter((folder, manager,), IPortletAssignmentMapping)

    assignment = classic.Assignment(template=template, macro='portlet')
    if assignments.has_key(template):
        del assignments[template]
    assignments[template] = assignment

def setupNavigationPortlet(folder):
    manager = getManager(folder, 'left')
    assignments = getMultiAdapter((folder, manager, ), IPortletAssignmentMapping)

    assignment = navigation.Assignment(name=u"Navigation",
                                       root=None,
                                       currentFolderOnly=False,
                                       includeTop=False,
                                       topLevel=0,
                                       bottomLevel=0)
    assignments['navtree'] = assignment


def getManager(folder, column):
    if column == 'left':
        manager = getUtility(IPortletManager, name=u'plone.leftcolumn', context=folder)
    else:
        manager = getUtility(IPortletManager, name=u'plone.rightcolumn', context=folder)
    return manager


def updateSecurity(portal):
    wfTool = getToolByName(portal, 'portal_workflow')
    wfTool.updateRoleMappings()
