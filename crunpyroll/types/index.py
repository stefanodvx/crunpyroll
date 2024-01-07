from .cms import CMS
from .obj import Object

from typing import Dict

class SessionIndex(Object):
    """
    Get session index, including CMS.

    Parameters:
        cms (:obj:`~crunpyroll.types.CMS`)

        cms_beta (:obj:`~crunpyroll.types.CMS`)

        cms_web (:obj:`~crunpyroll.types.CMS`)
    """
    def __init__(self, data: Dict):
        self.cms: CMS = CMS(data.get("cms"))
        self.cms_beta: CMS = CMS(data.get("cms_beta"))
        self.cms_web: CMS = CMS(data.get("cms_web"))