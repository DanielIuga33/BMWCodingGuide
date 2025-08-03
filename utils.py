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
            "X1 E84", "X1 F48", "X2 F39",
            "X3 E83", "X3 F25", "X3 G01",
            "X4 F26", "X4 G02",
            "X5 E53", "X5 E70", "X5 F15", "X5 G05",
            "X6 E71", "X6 F16", "X6 G06",
            "X7 G07",

            # Z Series (Roadsters/Coupes)
            "Z1", "Z3", "Z4 E85", "Z4 E89", "Z4 G29",

            # i Series (Electrice / hibride)
            "i3", "i4", "i8",]

bmw_modules = [
    # --- Generația E (anii '90 - început 2010) ---
    "CAS",        # Car Access System - imobilizator și recunoașterea cheii
    "FRM",        # Footwell Module - control lumini și confort interior
    "EWS",        # Elektronische Wegfahrsperre - imobilizator clasic
    "DME",        # Digital Motor Electronics - unitate de control motor
    "EGS",        # Electronic Gearbox System - control cutie automată
    "KOMBI",      # Kombiinstrument - bord analogic/digital
    "CCC",        # Car Communication Computer - sistem navigație vechi
    "SRS",        # Supplemental Restraint System - airbag-uri și siguranță pasageri

    # --- Generația F (2010 - 2018) ---
    "FEM_BODY",   # Front Electronic Module - control caroserie și funcții confort
    "BDC",        # Body Domain Controller - centralizare, confort, unele funcții caroserie
    "NFRM",       # New Footwell Module - versiune nouă FRM pentru lumini și confort
    "CIC",        # Car Information Computer - sistem navigație modern
    "NBT",        # Navigation Business Technology - navigație și iDrive îmbunătățite
    "ZGW",        # Zentral Gateway - poartă centrală pentru CAN bus și comunicații între module
    "HUD",        # Head-Up Display - modul pentru afișaj în parbriz
    "BMB",        # Battery Management Box - management baterie și curent
    "FZD",        # Roof Control Module - control decapotabilă (modele cabrio)
    "RDC",        # Tire Pressure Monitoring System - monitorizare presiune roți
    "LMA",        # Light Module Advanced - control avansat al luminilor
    "TMS",        # Tire Monitoring System - sistem pentru monitorizare anvelope

    # --- Generația G (2018 - prezent) ---
    "BMC",        # Battery Management Controller - control baterie îmbunătățit (mai ales hibride și electrice)
    "EHC",        # Electronic Height Control - control electronic suspensie adaptivă
    "RCM2",       # Radar Cruise Control Module 2 - modul avansat pentru cruise control radar
    "IAM",        # Integrated Access Module - acces și securitate integrată
    "CAS4",       # Car Access System versiunea 4 - sistem avansat de acces și imobilizare
    "RDC2",       # Tire Pressure Monitoring System versiunea 2 - sistem modern TPMS
    "ZBE",        # Zentralsteuergerät Bordnetz - Central Electric Module - control electric central al caroseriei
    "TPMA",       # TPMS Advanced - sistem avansat de monitorizare a presiunii în roți
    "EHV",        # Electronic High Voltage Control - control sisteme înalte tensiuni (modele electrice/hibride)
    "IHKA2",      # Interior Heating and Air Conditioning versiunea 2 - climatizare avansată
    "NBT EVO",    # Navigație iDrive evoluată - sistem multimedia și navigație modern
    "GWS2",       # Gear Selector Switch versiunea 2 - selector cutie îmbunătățit
    "SJS",        # Safety Junction Box - modul de siguranță și protecție electrică
    "MRS",        # Multiple Restraint System - sistem avansat airbag-uri și protecție pasageri
]

def get_modules_for_model(model):
    if model[0] == "E":
        return [ # --- Generația E (anii '90 - început 2010) ---
            "CAS",        # Car Access System - imobilizator și recunoașterea cheii
            "FRM",        # Footwell Module - control lumini și confort interior
            "EWS",        # Elektronische Wegfahrsperre - imobilizator clasic
            "DME",        # Digital Motor Electronics - unitate de control motor
            "EGS",        # Electronic Gearbox System - control cutie automată
            "KOMBI",      # Kombiinstrument - bord analogic/digital
            "CCC",        # Car Communication Computer - sistem navigație vechi
            "SRS",        # Supplemental Restraint System - airbag-uri și siguranță pasageri
            "NFRM",  # New Footwell Module - versiune nouă FRM pentru lumini și confort
            "CIC",  # Car Information Computer - sistem navigație modern
            "HUD",  # Head-Up Display - modul pentru afișaj în parbriz
            "CVM",
        ]
    elif model[0] == "F":
        return [
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
        ]
    else:
        return [
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

def get_bmw_years_intervals(model):
    bmw_years = {
         # Seria 3
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
    "X1_E84": {"non_LCI": (2009, 2015), "LCI": (2016, 2019)},
    "X1_F48": {"non_LCI": (2015, None)},
    "X2_F39": {"non_LCI": (2018, None)},
    "X3_E83": {"non_LCI": (2003, 2010), "LCI": (2011, 2010)},
    "X3_F25": {"non_LCI": (2010, 2017), "LCI": (2017, 2018)},
    "X3_G01": {"non_LCI": (2017, None)},
    "X4_F26": {"non_LCI": (2014, 2018), "LCI": (2018, 2019)},
    "X4_G02": {"non_LCI": (2018, None)},
    "X5_E53": {"non_LCI": (1999, 2006)},
    "X5_E70": {"non_LCI": (2007, 2013), "LCI": (2014, 2013)},
    "X5_F15": {"non_LCI": (2013, 2018), "LCI": (2018, 2019)},
    "X5_G05": {"non_LCI": (2018, None)},
    "X6_E71": {"non_LCI": (2008, 2013), "LCI": (2014, 2014)},
    "X6_F16": {"non_LCI": (2014, 2019), "LCI": (2019, None)},
    "X6_G06": {"non_LCI": (2019, None)},
    "X7_G07": {"non_LCI": (2018, None)},

    # Z Series (Roadsters)
    "Z3": {"non_LCI": (1995, 2002)},
    "Z4_E85": {"non_LCI": (2002, 2006), "LCI": (2007, 2008)},
    "Z4_E89": {"non_LCI": (2009, 2015)},
    "Z4_G29": {"non_LCI": (2018, None)},

    # i Series (Electrice/Hibride)
    "i3": {"non_LCI": (2013, 2019)},
    "i4": {"non_LCI": (2021, None)},
    "i8": {"non_LCI": (2014, 2020)},
    }

    model_data = bmw_years.get(model)

    if not model_data:
        return f"Modelul {model} nu este în baza de date."

    intervals = []
    for key, (start, end) in model_data.items():
        if end is None:
            end = 2025  # presupunem anul curent sau un an mare pentru 'prezent'
        intervals.append(f"{start}-{end}")

    return intervals

