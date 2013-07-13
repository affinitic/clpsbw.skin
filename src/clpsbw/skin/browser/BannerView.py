from Products.Five import BrowserView
from zope.interface import implements
from zope.security.interfaces import Unauthorized
from interfaces import IBannerView

class BannerView(BrowserView):
    """
    Gestion des banners
    """
    implements(IBannerView)

    def safe_getattr(self, obj, attr, default):
        """Attempts to read the attr, returning default if Unauthorized."""
        try:
            return getattr(obj, attr, default)
        except Unauthorized:
            return default

    def getBanner(self):
        """
        return the banner regarding folder
        """
        banner = self.safe_getattr(self.context, 'banner.png', None)
        if banner:
            return banner.tag()
        else:
            return None
