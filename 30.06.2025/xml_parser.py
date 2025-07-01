# Filename:  xml_parser.py
import xml.etree.ElementTree as ET
def parse_xml_file(filepath):
    """Parses an XML file and returns its root element."""
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        return root
    except FileNotFoundError:
        return None