from utils import bmw_modules


class DataValidator:
    @staticmethod
    def validate(language: str, functie: str, tool: str, pasi_ro: list, pasi_en: list):
        if language == "ro":
            if functie == "":
                raise Exception("Trebuie sa completezi functia adaugata! \n")
            if tool == "":
                raise Exception("Trebuie sa completezi Tool-ul folosit ! \n")
            if len(pasi_ro) == 0:
                raise Exception("Trebuie sa completezi pasii pe care i-ai folosit in romana ! \n")
            if len(pasi_en) == 0:
                raise Exception("Trebuie sa completezi pasii pe care i-ai folosit in engleza ! \n")
        else:
            if functie == "":
                raise Exception("You must complete the added Tool! \n")
            if tool == "":
                raise Exception("You must complete the used Tool ! \n")
            if len(pasi_ro) == 0:
                raise Exception("You must complete the used steps in romanian ! \n")
            if len(pasi_en) == 0:
                raise Exception("You must complete the used steps in english ! \n")

        return True


