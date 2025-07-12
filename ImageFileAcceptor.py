class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions
    def __call__(self, name, *args, **kwargs):
        start = name.rfind('.')
        ext = "" if start == -1 else name[start+1:]
        return ext in self.extensions
