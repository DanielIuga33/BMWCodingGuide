import os
import sys


def get_bmw_years_intervals(model):
    model_data = bmw_years.get(model)

    if not model_data:
        return f"Modelul {model} nu este în baza de date."

    intervals = []
    for key, (start, end) in model_data.items():
        if end is None:
            end = 2025  # presupunem anul curent sau un an mare pentru 'prezent'
        intervals.append(f"{start}-{end}")
    return intervals


def get_modules_by_model_and_year(model, year):
    if model not in bmw_modules_db:
        return f"Modelul {model} nu există în baza de date."

    modules_for_year = bmw_modules_db[model].get(year)
    if not modules_for_year:
        return f"Nu există date pentru anul {year} la modelul {model}."

    return modules_for_year


def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


bmw_models = [
    # Seria 1
    "E81", "E82", "E87", "E88", "F20", "F21", "F40",

    # Seria 2
    "F22", "F23", "F45", "F46", "G42",

    # Seria 3
    "E36", "E46", "E90", "E91", "E92", "E93",
    "F30", "F31", "F34", "G20",

    # Seria 4
    "F32", "F33", "F36", "G22",

    # Seria 5
    "E39", "E60", "E61", "F10", "F11", "G30",

    # Seria 6
    "E63", "E64", "F06", "F12", "F13",

    # Seria 7
    "E65", "E66", "F01", "F02", "G11",

    # Seria 8
    "G14", "G15", "G16",

    # X Series (SUV-uri)
    "E84 (X1)", "F48 (X1)", "F39 (X2)",
    "E83 (X3)", "F25 (X3)", "G01 (X3)",
    "F26 (X4)", "G02 (X4)",
    "E70 (X5)", "F15 (X5)", "G05 (X5)",
    "E71 (X6)", "F16 (X6)", "G06 (X6)",
    "G07 (X7)",

    # Z Series (Roadsters/Coupes)
    "Z1", "Z3", "E85 (Z4)", "E89 (Z4)", "G29 (Z4)",

    # i Series (Electrice / hibride)
    "I01 (i3)", "G26 (i4)", "I12 (i8)", ]

bmw_modules = [
    # --- Generația E (anii '90 - început 2010) ---
    "CAS",  # Car Access System - imobilizator și recunoașterea cheii
    "FRM",  # Footwell Module - control lumini și confort interior
    "EWS",  # Elektronische Wegfahrsperre - imobilizator clasic
    "DME",  # Digital Motor Electronics - unitate de control motor
    "EGS",  # Electronic Gearbox System - control cutie automată
    "KOMBI",  # Kombiinstrument - bord analogic/digital
    "CCC",  # Car Communication Computer - sistem navigație vechi
    "SRS",  # Supplemental Restraint System - airbag-uri și siguranță pasageri

    # --- Generația F (2010 - 2018) ---
    "FEM_BODY",  # Front Electronic Module - control caroserie și funcții confort
    "BDC",  # Body Domain Controller - centralizare, confort, unele funcții caroserie
    "NFRM",  # New Footwell Module - versiune nouă FRM pentru lumini și confort
    "CIC",  # Car Information Computer - sistem navigație modern
    "NBT",  # Navigation Business Technology - navigație și iDrive îmbunătățite
    "ZGW",  # Zentral Gateway - poartă centrală pentru CAN bus și comunicații între module
    "HUD",  # Head-Up Display - modul pentru afișaj în parbriz
    "BMB",  # Battery Management Box - management baterie și curent
    "FZD",  # Roof Control Module - control decapotabilă (modele cabrio)
    "RDC",  # Tire Pressure Monitoring System - monitorizare presiune roți
    "LMA",  # Light Module Advanced - control avansat al luminilor
    "TMS",  # Tire Monitoring System - sistem pentru monitorizare anvelope

    # --- Generația G (2018 - prezent) ---
    "BMC",  # Battery Management Controller - control baterie îmbunătățit (mai ales hibride și electrice)
    "EHC",  # Electronic Height Control - control electronic suspensie adaptivă
    "RCM2",  # Radar Cruise Control Module 2 - modul avansat pentru cruise control radar
    "IAM",  # Integrated Access Module - acces și securitate integrată
    "CAS4",  # Car Access System versiunea 4 - sistem avansat de acces și imobilizare
    "RDC2",  # Tire Pressure Monitoring System versiunea 2 - sistem modern TPMS
    "ZBE",  # Zentralsteuergerät Bordnetz - Central Electric Module - control electric central al caroseriei
    "TPMA",  # TPMS Advanced - sistem avansat de monitorizare a presiunii în roți
    "EHV",  # Electronic High Voltage Control - control sisteme înalte tensiuni (modele electrice/hibride)
    "IHKA2",  # Interior Heating and Air Conditioning versiunea 2 - climatizare avansată
    "NBT EVO",  # Navigație iDrive evoluată - sistem multimedia și navigație modern
    "GWS2",  # Gear Selector Switch versiunea 2 - selector cutie îmbunătățit
    "SJS",  # Safety Junction Box - modul de siguranță și protecție electrică
    "MRS",  # Multiple Restraint System - sistem avansat airbag-uri și protecție pasageri
]

bmw_modules_db = {
    #Seria 1
    "E81": {
        "2007-2009": ["FRM1", "JBBF", "CAS", "KOMBI", "DME", "EGS", "IHKA"],
        "2009-2012": ["FRM2", "JBBF", "CAS", "KOMBI", "DME", "EGS", "IHKA"]
    },
    "E82": {
        "2007-2010": ["FRM1", "JBBF", "CAS", "KOMBI", "DME", "EGS", "IHKA"],
        "2011-2013": ["FRM2", "NFRM", "CAS", "KOMBI", "DME", "EGS", "IHKA"]
    },
    "E87": {
        "2004-2006": ["LCM", "JBBF", "CAS", "KOMBI", "DME", "EGS", "IHKA"],
        "2007-2011": ["FRM2", "JBBF", "CAS", "KOMBI", "DME", "EGS", "IHKA"]
    },
    "E88": {
        "2008-2010": ["FRM1", "JBBF", "CAS", "KOMBI", "DME", "EGS", "IHKA"],
        "2011-2013": ["FRM2", "NFRM", "CAS", "KOMBI", "DME", "EGS", "IHKA"]
    },
    "F20": {
        "2011-2014": ["FEM", "BDC", "KOMBI", "DME", "EGS", "DSC"],
        "2015-2019": ["FEM", "BDC", "HU_ENTRYNAV", "ZBE2", "DME", "EGS", "DSC"]
    },
    "F21": {
        "2012-2014": ["FEM", "BDC", "KOMBI", "DME", "EGS", "DSC"],
        "2015-2019": ["FEM", "BDC", "HU_ENTRYNAV", "ZBE2", "DME", "EGS", "DSC"]
    },
    "F40": {
        "2019-2025": ["BDC3", "HU_H3", "KOMBI", "EGS", "DME", "DSC", "SAS", "ZBE3"]
    },
    #Seria 2
    "F22": {
        "2014-2017": ["FEM", "BDC", "HU_ENTRYNAV", "KOMBI", "DME", "EGS", "DSC"],
        "2018-2021": ["FEM", "BDC", "HU_NBT_EVO", "KOMBI", "DME", "EGS", "DSC"]
    },
    "F23": {
        "2014-2017": ["FEM", "BDC", "HU_ENTRYNAV", "KOMBI", "DME", "EGS", "DSC"],
        "2018-2021": ["FEM", "BDC", "HU_NBT_EVO", "KOMBI", "DME", "EGS", "DSC"]
    },
    "F45": {
        "2014-2017": ["BDC", "HU_ENTRYNAV", "ZBE2", "KOMBI", "DME", "EGS", "DSC"],
        "2018-2021": ["BDC", "HU_NBT_EVO", "ZBE2", "KOMBI", "DME", "EGS", "DSC"]
    },
    "F46": {
        "2015-2017": ["BDC", "HU_ENTRYNAV", "ZBE2", "KOMBI", "DME", "EGS", "DSC"],
        "2018-2021": ["BDC", "HU_NBT_EVO", "ZBE2", "KOMBI", "DME", "EGS", "DSC"]
    },
    "G42": {
        "2021-2025": ["BDC3", "HU_H3", "KOMBI", "DME", "EGS", "DSC", "SAS", "ZBE3"]
    },
    #Seria 3
    "E36": {
        "1990-1995": ["DME", "EGS", "ABS/ASC", "KOMBI", "ZKE", "IHKA", "AIRBAG"],
        "1996-2000": ["DME", "EGS", "ABS/ASC", "KOMBI", "ZKE", "IHKA", "AIRBAG", "EWS II", "LKM", "GM"]
    },
    "E46": {
        "1998-2001": ["LCM", "IKE", "DME", "EGS", "ZKE", "GM5"],
        "2002-2006": ["LCM", "IKE", "DME", "EGS", "ZKE", "GM5"]
    },
    "E90": {
        "2005-2008": ["FRM2", "CCC", "JBBF", "CAS", "KOMBI", "DME", "EGS"],
        "2009-2011": ["FRM2", "NFRM", "CAS", "KOMBI", "DME", "EGS", "CIC"]
    },
    "E91": {
        "2005-2008": ["FRM1", "JBBF", "CAS", "KOMBI", "DME", "EGS", "CCC"],
        "2009-2012": ["FRM2", "NFRM", "CAS", "KOMBI", "DME", "EGS", "CIC"]
    },
    "E92": {
        "2006-2008": ["FRM1", "JBBF", "CAS", "KOMBI", "DME", "EGS", "CIC"],
        "2009-2013": ["FRM2", "NFRM", "CAS", "KOMBI", "DME", "EGS", "CIC"]
    },
    "E93": {
        "2007-2008": ["FRM1", "JBBF", "CAS", "KOMBI", "DME", "EGS", "CIC"],
        "2009-2013": ["FRM2", "NFRM", "CAS", "KOMBI", "DME", "EGS", "CIC"]
    },
    "F30": {
        "2011-2015": ["FEM", "BDC", "HU_ENTRY", "KOMBI", "DME", "EGS", "DSC", "CIC"],
        "2015-2019": ["FEM", "BDC", "HU_NBT_EVO", "KOMBI", "DME", "EGS", "DSC"]
    },
    "F31": {
        "2012-2015": ["FEM", "BDC", "HU_ENTRY", "KOMBI", "DME", "EGS", "DSC"],
        "2015-2019": ["FEM", "BDC", "HU_NBT_EVO", "KOMBI", "DME", "EGS", "DSC"]
    },
    "F34": {
        "2013-2015": ["FEM", "BDC", "HU_ENTRY", "KOMBI", "DME", "EGS", "DSC"],
        "2015-2019": ["FEM", "BDC", "HU_NBT_EVO", "KOMBI", "DME", "EGS", "DSC"]
    },
    "G20": {
        "2018-2022": ["BDC3", "HU_H3", "KOMBI", "DME", "EGS", "DSC", "SAS", "ZBE3"],
        "2022-2025": ["BDC3", "HU_H3", "KOMBI", "DME", "EGS", "DSC", "SAS", "ZBE3", "MGU22"]
    },
    "G21": {
        "2019-2022": ["BDC3", "HU_H3", "KOMBI", "DME", "EGS", "DSC", "ZBE3", "SAS"],
        "2022-2025": ["BDC3", "HU_H3", "KOMBI", "DME", "EGS", "DSC", "ZBE3", "MGU22", "SAS"]
    },
    "G28": {
        "2019-2025": ["BDC3", "HU_H3", "KOMBI", "DME", "EGS", "DSC", "ZBE3", "SAS", "MGU22"]
    },
    #Seria 4
    "F32": {
        "2013-2016": ["HU_CIC", "DME", "EGS", "KOMBI", "IHKA", "DSC", "FEM", "BDC", "REM", "ZBE"],
        "2017-2020": ["HU_NBT", "DME", "EGS", "KOMBI", "IHKA", "DSC", "FEM", "BDC", "REM", "ZBE"]
    },
    "F33": {
        "2013-2016": ["HU_CIC", "DME", "EGS", "KOMBI", "IHKA", "DSC", "FEM", "REM", "ZBE"],
        "2017-2020": ["HU_NBT", "DME", "EGS", "KOMBI", "IHKA", "DSC", "FEM", "REM", "ZBE"]
    },
    "F36": {
        "2014-2016": ["HU_CIC", "DME", "EGS", "KOMBI", "IHKA", "DSC", "FEM", "REM", "ZBE"],
        "2017-2020": ["HU_NBT", "DME", "EGS", "KOMBI", "IHKA", "DSC", "FEM", "REM", "ZBE"]
    },
    "G22": {
        "2020-2025": ["MGU", "DME", "EGS", "KOMBI", "IHKA", "DSC", "BDC", "ZBE", "REM"]
    },
    #Seria 5
    "E39": {
        "1995-2000": ["IKE", "DME", "EGS", "ABS", "ZKE", "LCM", "MID", "RAD", "IHKA"],
        "2001-2003": ["IKE", "DME", "EGS", "ABS", "LCM", "NAV", "IHKA", "ZKE"]
    },
    "E60": {
        "2003-2007": ["CCC", "ASK", "DME", "EGS", "SZL", "ABS", "LMA", "JBBF", "KMBI", "IHKA"],
        "2007-2010": ["CIC", "DME", "EGS", "SZL", "ABS", "LMA", "JBBF", "KOMBI", "IHKA"]
    },
    "E61": {
        "2004-2007": ["CCC", "ASK", "DME", "EGS", "SZL", "ABS", "LMA", "JBBF", "KMBI", "IHKA", "AHL"],
        "2007-2010": ["CIC", "DME", "EGS", "SZL", "ABS", "LMA", "JBBF", "KOMBI", "IHKA", "AHL"]
    },
    "F10": {
        "2010-2013": ["HU_CIC", "DME", "EGS", "KOMBI", "IHKA", "ZBE", "JBBF", "DSC", "BDC1"],
        "2014-2016": ["HU_NBT", "DME", "EGS", "KOMBI", "IHKA", "ZBE", "DSC", "BDC1", "FEM"]
    },
    "F11": {
        "2010-2013": ["HU_CIC", "DME", "EGS", "KOMBI", "IHKA", "ZBE", "DSC", "BDC1", "FEM"],
        "2014-2016": ["HU_NBT", "DME", "EGS", "KOMBI", "IHKA", "ZBE", "DSC", "BDC1", "FEM"]
    },
    "G30": {
        "2017-2020": ["HU_NBT_EVO", "DME", "EGS", "KOMBI", "IHKA", "ZBE3", "DSC", "BDC3"],
        "2020-2025": ["MGU", "DME", "EGS", "KOMBI", "IHKA", "ZBE3", "DSC", "BDC3", "MGU22"]
    },
    "E63": {
        "2003-2007": ["CCC", "ASK", "DME", "EGS", "KOMBI", "IHKA", "LMA", "SZL", "DSC"],
        "2007-2010": ["CIC", "DME", "EGS", "KOMBI", "IHKA", "LMA", "SZL", "DSC"]
    },
    "E64": {
        "2004-2007": ["CCC", "ASK", "DME", "EGS", "KOMBI", "IHKA", "LMA", "SZL", "DSC"],
        "2007-2010": ["CIC", "DME", "EGS", "KOMBI", "IHKA", "LMA", "SZL", "DSC"]
    },
    "F06": {
        "2012-2015": ["HU_CIC", "DME", "EGS", "IHKA", "DSC", "KOMBI", "ZBE", "FEM"],
        "2016-2018": ["HU_NBT", "DME", "EGS", "IHKA", "DSC", "KOMBI", "ZBE", "BDC1"]
    },
    "F12": {
        "2011-2015": ["HU_CIC", "DME", "EGS", "IHKA", "DSC", "KOMBI", "ZBE", "FEM"],
        "2016-2018": ["HU_NBT", "DME", "EGS", "IHKA", "DSC", "KOMBI", "ZBE", "BDC1"]
    },
    "F13": {
        "2011-2015": ["HU_CIC", "DME", "EGS", "IHKA", "DSC", "KOMBI", "ZBE", "FEM"],
        "2016-2018": ["HU_NBT", "DME", "EGS", "IHKA", "DSC", "KOMBI", "ZBE", "BDC1"]
    },
    #Seria 7
    "E65": {
        "2001-2005": ["ASK", "DME", "EGS", "LMA", "KOMBI", "IHKA", "SZL", "PDC", "ZBE"],
        "2006-2008": ["CCC", "DME", "EGS", "LMA", "KOMBI", "IHKA", "SZL", "PDC", "ZBE"]
    },
    "E66": {
        "2002-2005": ["ASK", "DME", "EGS", "LMA", "KOMBI", "IHKA", "SZL", "PDC", "ZBE"],
        "2006-2008": ["CCC", "DME", "EGS", "LMA", "KOMBI", "IHKA", "SZL", "PDC", "ZBE"]
    },
    "F01": {
        "2008-2012": ["HU_CIC", "DME", "EGS", "KOMBI", "IHKA", "LMA", "JBBF", "DSC", "ZBE"],
        "2013-2015": ["HU_NBT", "DME", "EGS", "KOMBI", "IHKA", "LMA", "JBBF", "DSC", "ZBE"]
    },
    "F02": {
        "2009-2012": ["HU_CIC", "DME", "EGS", "KOMBI", "IHKA", "LMA", "JBBF", "DSC", "ZBE"],
        "2013-2015": ["HU_NBT", "DME", "EGS", "KOMBI", "IHKA", "LMA", "JBBF", "DSC", "ZBE"]
    },
    "G11": {
        "2015-2019": ["HU_NBT_EVO", "DME", "EGS", "KOMBI", "IHKA", "ZBE", "DSC", "BDC"],
        "2020-2025": ["MGU", "DME", "EGS", "KOMBI", "IHKA", "ZBE", "DSC", "BDC", "MGU22"]
    },
    #Seria 8
    "G14": {
        "2018-2025": ["MGU", "DME", "EGS", "KOMBI", "IHKA", "ZBE", "DSC", "BDC", "REM"]
    },
    "G15": {
        "2018-2025": ["MGU", "DME", "EGS", "KOMBI", "IHKA", "ZBE", "DSC", "BDC", "REM"]
    },
    "G16": {
        "2018-2025": ["MGU", "DME", "EGS", "KOMBI", "IHKA", "ZBE", "DSC", "BDC", "REM"]
    },
    # Seria X (SUV)
    "E84 (X1)": {
        "2009-2012": ["FRM2", "CAS", "KOMBI", "DME", "EGS", "IHKA"],
        "2013-2015": ["FRM2", "CAS", "KOMBI", "DME", "EGS", "DSC", "IHKA"]
    },
    "F48 (X1)": {
        "2016-2018": ["BDC3", "HU_H3", "KOMBI", "DME", "EGS", "DSC"],
        "2019-2022": ["BDC3", "HU_H3", "KOMBI", "DME", "EGS", "DSC", "SAS", "ZBE3"]
    },
    "F39 (X2)": {
        "2018-2022": ["BDC3", "HU_H3", "KOMBI", "DME", "EGS", "DSC", "SAS", "ZBE3"]
    },
    "E83 (X3)": {
        "2003-2006": ["FRM2", "CAS", "KOMBI", "DME", "EGS", "IHKA"],
        "2007-2010": ["FRM2", "CAS", "KOMBI", "DME", "EGS", "DSC", "IHKA"]
    },
    "F25 (X3)": {
        "2011-2014": ["FEM", "BDC", "KOMBI", "DME", "EGS", "DSC"],
        "2015-2017": ["FEM", "BDC", "KOMBI", "DME", "EGS", "DSC", "SAS"]
    },
    "F26 (X4)": {
        "2014-2017": ["FEM", "BDC", "KOMBI", "DME", "EGS", "DSC"],
        "2018-2025": ["FEM", "BDC", "KOMBI", "DME", "EGS", "DSC", "SAS"]
    },
    "E70 (X5)": {
        "2007-2010": ["FRM2", "NFRM", "CAS", "KOMBI", "DME", "EGS", "CIC"],
        "2011-2013": ["FRM2", "NFRM", "CAS", "KOMBI", "DME", "EGS", "CIC", "DSC"]
    },
    "E71 (X6)": {
        "2008-2013": ["FRM2", "NFRM", "CAS", "KOMBI", "DME", "EGS", "CIC"],
        "2014-2014": ["FRM2", "NFRM", "CAS", "KOMBI", "DME", "EGS", "CIC", "DSC"]
    },
    "F15 (X5)": {
        "2014-2017": ["FEM", "BDC", "KOMBI", "DME", "EGS", "DSC"],
        "2018-2020": ["BDC3", "HU_H3", "KOMBI", "DME", "EGS", "DSC", "SAS", "ZBE3"]
    },
    "F16 (X6)": {
        "2015-2017": ["FEM", "BDC", "KOMBI", "DME", "EGS", "DSC"],
        "2018-2019": ["BDC3", "HU_H3", "KOMBI", "DME", "EGS", "DSC", "SAS", "ZBE3"]
    },
    "G07 (X7)": {
        "2019-2022": ["BDC3", "HU_H3", "KOMBI", "DME", "EGS", "DSC", "SAS", "ZBE3"],
        "2023-2025": ["BDC3", "HU_H3", "KOMBI", "DME", "EGS", "DSC", "SAS", "ZBE4"]
    },

    # Seria i (electric / hybrid)
    "I01 (i3)": {
        "2013-2016": ["EVCU", "KOMBI", "DME", "BDC", "HU_H3", "DSC"],
        "2017-2021": ["EVCU", "KOMBI", "DME", "BDC", "HU_H3", "DSC", "SAS"]
    },
    "G26 (i4)": {
        "2021-2023": ["BDC3", "HU_H3", "KOMBI", "DME", "EGS", "DSC", "SAS", "ZBE3"],
        "2024-2025": ["BDC3", "HU_H3", "KOMBI", "DME", "EGS", "DSC", "SAS", "ZBE4"]
    },
    "I20 (iX)": {
        "2021-2023": ["BDC3", "HU_H3", "KOMBI", "DME", "EGS", "DSC", "SAS", "ZBE3"],
        "2024-2025": ["BDC3", "HU_H3", "KOMBI", "DME", "EGS", "DSC", "SAS", "ZBE4"]
    },
    "E89 (Z4)": {
        "2009-2015": ["FRM2", "CAS", "KOMBI", "DME", "EGS", "DSC"]
    },
    "E85 (Z4)": {
        "2002-2006": ["FRM2", "CAS", "KOMBI", "DME", "EGS", "DSC"],
        "2007-2008": ["FRM2", "CAS", "KOMBI", "DME", "EGS", "DSC", "SAS"]
    },
    "I12 (i8)": {
        "2014-2017": ["BDC", "HU_H3", "KOMBI", "DME", "EGS", "DSC"],
        "2018-2020": ["BDC3", "HU_H3", "KOMBI", "DME", "EGS", "DSC", "SAS"]
    }
}

bmw_years = {
    # Seria 1
    "E81": {"non_LCI": (2007, 2009), "LCI": (2009, 2012)},
    "E82": {"non_LCI": (2007, 2010), "LCI": (2011, 2013)},
    "E87": {"non_LCI": (2004, 2006), "LCI": (2007, 2011)},
    "E88": {"non_LCI": (2008, 2010), "LCI": (2011, 2013)},
    "F20": {"non_LCI": (2011, 2014), "LCI": (2015, 2019)},
    "F21": {"non_LCI": (2012, 2014), "LCI": (2015, 2019)},
    "F40": {"non_LCI": (2019, None)},

    # Seria 3
    "E36": {"non_LCI": (1990, 1995), "LCI": (1996, 2000)},
    "E46": {"non_LCI": (1998, 2001), "LCI": (2002, 2006)},
    "E90": {"non_LCI": (2005, 2008), "LCI": (2009, 2011)},
    "E91": {"non_LCI": (2005, 2008), "LCI": (2009, 2012)},
    "E92": {"non_LCI": (2006, 2008), "LCI": (2009, 2013)},
    "E93": {"non_LCI": (2007, 2008), "LCI": (2009, 2013)},
    "F30": {"non_LCI": (2011, 2015), "LCI": (2015, 2019)},
    "F31": {"non_LCI": (2012, 2015), "LCI": (2015, 2019)},
    "F34": {"non_LCI": (2013, 2015), "LCI": (2015, 2019)},
    "G20": {"non_LCI": (2018, 2022), "LCI": (2022, None)},

    # Seria 4 (coupes și cabrio)
    "F32": {"non_LCI": (2013, 2016), "LCI": (2017, 2020)},
    "F33": {"non_LCI": (2013, 2016), "LCI": (2017, 2020)},
    "F36": {"non_LCI": (2014, 2016), "LCI": (2017, 2020)},
    "G22": {"non_LCI": (2020, None)},

    # Seria 5
    "E39": {"non_LCI": (1995, 2000), "LCI": (2001, 2003)},
    "E60": {"non_LCI": (2003, 2007), "LCI": (2007, 2010)},
    "E61": {"non_LCI": (2004, 2007), "LCI": (2007, 2010)},
    "F10": {"non_LCI": (2010, 2013), "LCI": (2014, 2016)},
    "F11": {"non_LCI": (2010, 2013), "LCI": (2014, 2016)},
    "G30": {"non_LCI": (2017, None)},

    # Seria 6
    "E63": {"non_LCI": (2003, 2007), "LCI": (2007, 2010)},
    "E64": {"non_LCI": (2004, 2007), "LCI": (2007, 2010)},
    "F06": {"non_LCI": (2012, 2015), "LCI": (2016, 2018)},
    "F12": {"non_LCI": (2011, 2015), "LCI": (2016, 2018)},
    "F13": {"non_LCI": (2011, 2015), "LCI": (2016, 2018)},

    # Seria 7
    "E65": {"non_LCI": (2001, 2005), "LCI": (2006, 2008)},
    "E66": {"non_LCI": (2002, 2005), "LCI": (2006, 2008)},
    "F01": {"non_LCI": (2008, 2012), "LCI": (2013, 2015)},
    "F02": {"non_LCI": (2009, 2012), "LCI": (2013, 2015)},
    "G11": {"non_LCI": (2015, None)},

    # Seria 8
    "E31": {"non_LCI": (1989, 1994)},  # fără LCI
    "G14": {"non_LCI": (2018, None)},  # cabrio
    "G15": {"non_LCI": (2018, None)},  # coupe
    "G16": {"non_LCI": (2018, None)},  # gran coupe


    # X Series SUV
    "E84 (X1)": {"non_LCI": (2009, 2012), "LCI": (2013, 2015)},
    "F48 (X1)": {"non_LCI": (2015, None)},  # încă în producție
    "F39 (X2)": {"non_LCI": (2018, None)},
    "E83 (X3)": {"non_LCI": (2003, 2006), "LCI": (2007, 2010)},
    "F25 (X3)": {"non_LCI": (2010, 2014), "LCI": (2015, 2017)},
    "G01 (X3)": {"non_LCI": (2018, None)},
    "F26 (X4)": {"non_LCI": (2014, 2017), "LCI": (2018, 2018)},
    "G02 (X4)": {"non_LCI": (2019, None)},
    "E53 (X5)": {"non_LCI": (1999, 2006)},
    "E70 (X5)": {"non_LCI": (2007, 2010), "LCI": (2011, 2013)},
    "F15 (X5)": {"non_LCI": (2013, 2017), "LCI": (2018, 2020)},
    "G05 (X5)": {"non_LCI": (2021, None)},
    "E71 (X6)": {"non_LCI": (2008, 2013), "LCI": (2014, 2014)},
    "F16 (X6)": {"non_LCI": (2015, 2018), "LCI": (2019, None)},
    "G06 (X6)": {"non_LCI": (2020, None)},
    "G07 (X7)": {"non_LCI": (2019, None)},

    # Z Series (Roadsters)
    "Z3": {"non_LCI": (1995, 2002)},
    "E85 (Z4)": {"non_LCI": (2002, 2006), "LCI": (2007, 2008)},
    "E89 (Z4)": {"non_LCI": (2009, 2015)},
    "G29 (Z4)": {"non_LCI": (2018, None)},

    # i Series (Electrice/Hibride)
    "I01 (i3)": {"non_LCI": (2013, 2016), "LCI": (2017, 2019)},
    "G26 (i4)": {"non_LCI": (2021, 2023), "LCI": (2024, None)},
    "I12 (i8)": {"non_LCI": (2014, 2017), "LCI": (2018, 2020)},
    "I20 (iX)": {"non_LCI": (2021, 2023), "LCI": (2024, None)}
}
