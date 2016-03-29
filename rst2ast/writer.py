# -*- coding: utf-8 -*-

from docutils import writers, nodes
import json

__docformat__ = 'reStructuredText'


class ASTWriter(writers.Writer):
    supported = ('ast',)
    """Formats this writer supports."""

    config_section = 'docutils_ast writer'
    config_section_dependencies = ('writers',)

    output = None
    """Final translated form of `document`."""

    def __init__(self):
        writers.Writer.__init__(self)
        self.translator_class = ASTTranslator
        self.visitor = None

    def translate(self):
        self.visitor = visitor = self.translator_class(self.document)
        self.document.walkabout(visitor)
        self.output = ''.join(visitor.output)


class ASTTranslator(nodes.GenericNodeVisitor):
    def __init__(self, document):
        nodes.NodeVisitor.__init__(self, document)
        result, line = self.walk(document)
        self.output = [json.dumps(result)]

    def walk(self, node, line=1):
        if not isinstance(node, nodes.Node):
            return None, None
        result = {}
        # Line Start
        if not node.line:
            node.line = line
        else:
            line = node.line
        # Attributes
        for k, v in node.__dict__.items():
            if not k.startswith('__') and isinstance(v, (str, unicode, int, long, float, bool)):
                result[k] = v
        # Tag Name (type)
        if 'tagname' not in result:
            result['tagname'] = None
        # Text
        if isinstance(node, (nodes.Element, nodes.Text)):
            result['text'] = node.astext()
        # Children
        children = getattr(node, 'children', [])
        if len(children) > 0:
            result['children'] = []
            for child_node in children:
                res, _line = self.walk(child_node, line)
                if not res:
                    continue
                result['children'].append(res)
                if line < _line:
                    line = _line
        # Line End
        result['line'] = {
            'start': node.line,
            'end': line,
        }
        return result, line

    # GenericNodeVisitor methods
    def default_visit(self, node):
        """Default node visit method."""
        pass

    def default_departure(self, node):
        """Default node depart method."""
        pass

    # NodeVisitor methods
    def unknown_departure(self, node):
        pass

    def unknown_visit(self, node):
        pass
