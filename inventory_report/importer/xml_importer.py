from xml.etree import ElementTree as ET
from .importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(caminho):
        if ".xml" not in caminho:
            raise ValueError("Arquivo inválido")

        tree = ET.parse(caminho)
        root = list(tree.getroot())
        arquivo_xml = []
        info_dict = {}

        for i in range(len(root)):
            for info in root[i]:
                info_dict[info.tag] = info.text
            arquivo_xml.append(info_dict)
            info_dict = {}

        return arquivo_xml
