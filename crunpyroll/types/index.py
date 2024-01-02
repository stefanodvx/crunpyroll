from .cms import CMS
from .obj import Object

class Index(Object):
    def __init__(self, data: dict):
        self.cms: CMS = CMS(data.get("cms"))
        self.cms_beta: CMS = CMS(data.get("cms_beta"))
        self.cms_web: CMS = CMS(data.get("cms_web"))