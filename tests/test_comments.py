from utils import ComposedDocument
from utils import FixtureDocument


def test_comments():
    '''Append doc with comments to a document without them'''
    doc = FixtureDocument("comments.docx")
    composed = ComposedDocument(
        "master.docx", "comments.docx")
    assert composed == doc



    
