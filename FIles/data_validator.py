from utils import bmw_modules


class DataValidator:
    @staticmethod
    def validate(language: str, model, fabric, modul, functie: str, tool: str, pasi_ro: list, pasi_en: list):
        if language == "ro":
            if model == "Alege modelul":
                raise Exception("Trebuie sa completezi modelul de adaugat! \n")
            if fabric == "Alege generația":
                raise Exception("Trebuie sa completezi generația! \n")
            if modul == "Alege modulul":
                raise Exception("Trebuie sa completezi modulul de adaugat! \n")
            if functie == "":
                raise Exception("Trebuie sa completezi funcția de adaugat! \n")
            if tool == "":
                raise Exception("Trebuie sa completezi Tool-ul folosit ! \n")
            if len(pasi_ro) == 0:
                raise Exception("Trebuie sa completezi pașii pe care i-ai folosit in romana ! \n")
            if len(pasi_en) == 0:
                raise Exception("Trebuie sa completezi pașii pe care i-ai folosit in engleza ! \n")
        else:
            if model == "Choose model":
                raise Exception("You must complete the added Model! \n")
            if fabric == "Choose generation":
                raise Exception("You must complete the added Generation! \n")
            if modul == "Choose module":
                raise Exception("You must complete the added Module! \n")
            if functie == "":
                raise Exception("You must complete the added Tool! \n")
            if tool == "":
                raise Exception("You must complete the used Tool ! \n")
            if len(pasi_ro) == 0:
                raise Exception("You must complete the used steps in romanian ! \n")
            if len(pasi_en) == 0:
                raise Exception("You must complete the used steps in english ! \n")

        return True


