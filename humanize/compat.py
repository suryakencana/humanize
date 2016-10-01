import sys

if sys.version_info < (3,):
    string_types = (basestring,)
    text_type = unicode
else:
    string_types = (str,)
    text_type = str

