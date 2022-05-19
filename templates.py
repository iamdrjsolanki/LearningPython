import os

FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
TEMPLATE_DIR = os.path.join(BASE_DIR)

class Template:

    template = ""
    content = None

    def __init__(self, template="", context=None, *args, **kwargs):
        self.templateName = template
        self.context = context

    def getTemplates(self):
        templatePath = os.path.join(TEMPLATE_DIR, self.template)
        if not os.path.exists(templatePath):
            raise Exception("This path does not exist")
        templateString = ""
        with open(templatePath, 'r') as f:
            templateString = f.read()
            
        return templateString

    def render(self, context=None):
        renderCtx = {}
        if self.context != None:
            renderCtx = self.context
        else:
            renderCtx = context
        if not isinstance(renderCtx, dict):
            renderCtx = dict
        templateString = self.getTemplates()
        return templateString.format(**renderCtx)