import pandas as pd

def editFAM(fam_df):
    fam_df.drop(["Aufbrauch_KS_Einheit\n", "Aufbrauch_KS_Zahl\n", "Aufbrauch_RT_Einheit\n", "Aufbrauch_RT_Zahl\n", "Dat_Ausbietung\n", "Dat_Ersterfassung\n",
                 "Dat_Zusammensetzung\n", "EMA_Zulassung\n", "Sofortiger_Verbrauch\n", "Therapierichtung_AM\n"], axis=1, inplace=True)

    fam_df = fam_df.replace('\n', '', regex=True)

    fam_df.columns = ["Index", "Key_FAM", "Abgabebestimmung", "Einmalige_Anwendung", "Feuchtigkeitsschutz", "Info_Aufbewahrung", "Key_ADR_Anbieter", "Key_ADR_Mitvertrieb", "Key_ATC", "Key_DAR", "Key_FAT"
        , "Key_IND_Haupt", "Key_IND_Neben", "Lichtschutz", "Monopraeparat", "Produktgruppe", "Produktname", "Verkehrsstatus", "Veterinaerpraeparat", "Key_ATCA", "Zusaetz_Ueberwachung"]
    fam_df.drop(["Index"], axis=1, inplace=True)

    fam_df.loc[fam_df['Abgabebestimmung'] == "0", 'Abgabebestimmung'] = "nicht verschreibungspflichtig"
    fam_df.loc[fam_df['Abgabebestimmung'] == "1", 'Abgabebestimmung'] = "verschreibungspflichtig"
    fam_df.loc[fam_df['Abgabebestimmung'] == "3", 'Abgabebestimmung'] = "Betäubungsmittel"
    fam_df.loc[fam_df['Einmalige_Anwendung'] == "1", 'Einmalige_Anwendung'] = "Zur einmaligen Anwendung nach Anbruch/Zubereitung"
    fam_df.loc[fam_df['Feuchtigkeitsschutz'] == "1", 'Feuchtigkeitsschutz'] = "Vor Feuchtigkeit schützen"
    fam_df.loc[fam_df['Lichtschutz'] == "1", 'Lichtschutz'] = "Vor Licht schützen"
    fam_df.loc[fam_df['Monopraeparat'] == 0, 'Monopraeparat'] = "Kombipräparat"
    fam_df.loc[fam_df['Monopraeparat'] == 1, 'Monopraeparat'] = "Monopräparat"
    fam_df.loc[fam_df['Produktgruppe'] == 1, 'Produktgruppe'] = "Arzneimittel"
    fam_df.loc[fam_df['Produktgruppe'] == 2, 'Produktgruppe'] = "Medizinprodukt"
    fam_df.loc[fam_df['Produktgruppe'] == 3, 'Produktgruppe'] = "Diätetikum"
    fam_df.loc[fam_df['Produktgruppe'] == 4, 'Produktgruppe'] = "Rezepturgrundstoff"
    fam_df.loc[fam_df['Produktgruppe'] == 5, 'Produktgruppe'] = "Nahrungsergänzungsmittel"
    fam_df.loc[fam_df['Produktgruppe'] == 6, 'Produktgruppe'] = "Körperpflegemittel"
    fam_df.loc[fam_df['Produktgruppe'] == 7, 'Produktgruppe'] = "Desinfektionsmittel"
    fam_df.loc[fam_df['Produktgruppe'] == 8, 'Produktgruppe'] = "Sonstiges Nichtarzneimittel"
    fam_df.loc[fam_df['Verkehrsstatus'] == 1, 'Verkehrsstatus'] = "im Handel"
    fam_df.loc[fam_df['Verkehrsstatus'] == 2, 'Verkehrsstatus'] = "außer Vertrieb"
    fam_df.loc[fam_df['Verkehrsstatus'] == 4, 'Verkehrsstatus'] = "vor Markteinführung"
    fam_df.loc[fam_df['Verkehrsstatus'] == 5, 'Verkehrsstatus'] = "nicht verkehrsfähig"
    fam_df.loc[fam_df['Veterinaerpraeparat'] == 0, 'Veterinaerpraeparat'] = "Humanpräparat"
    fam_df.loc[fam_df['Veterinaerpraeparat'] == 1, 'Veterinaerpraeparat'] = "Veterinärpräparat"
    fam_df.loc[fam_df['Zusaetz_Ueberwachung'] == 0, 'Zusaetz_Ueberwachung'] = "Arzneimittel unterliegt keiner zusätzlichen Überwachung"
    fam_df.loc[fam_df['Zusaetz_Ueberwachung'] == 1, 'Zusaetz_Ueberwachung'] = "Arzneimittel unterliegt einer zusätzlichen Überwachung"
    return fam_df

def editDAR(dar_df):
    dar_df.columns = ["Index", "Key_DAR", "Darreichungsform"]
    dar_df.drop(["Index"], axis=1, inplace=True)

    return dar_df

def editFAI(fai_df, sna_df):
    fai_df.drop(["Komponentennr\n", "Rang\n", "Einheit\n", "Entsprichtstoff\n", "Stofftyp\n", "Suffix\n", "Zahl\n", "Vergleich\n", "Verwendung_intern\n"], axis=1, inplace=True)

    fai_df = fai_df.replace('\n', '', regex=True)
    sna_df = sna_df.replace('\n', '', regex=True)

    fai_df.columns = ["Index", "Key_FAM", "Key_STO"]
    sna_df.columns = ["Index", "Key_STO", "Zaehler", "Herkunft", "Stoffname", "Sortierbegriff", "Suchbegriff", "Vorzugsbezeichnung"]
    fai_df.drop(["Index"], axis=1, inplace=True)
    sna_df.drop(["Index"], axis=1, inplace=True)

    fai_df = fai_df.merge(sna_df, left_on="Key_STO", right_on="Key_STO", how="left")
    fai_df.drop(["Zaehler", "Herkunft", "Sortierbegriff", "Suchbegriff", "Vorzugsbezeichnung", "Key_STO"], axis=1, inplace=True)
    fai_df = fai_df.groupby("Key_FAM", as_index=False)["Stoffname"].agg({"Stoffname":lambda x: "%s" % ', '.join(x)})
    return fai_df

def editFAK(fak_df):
    fak_df.drop(["Komponentennr\n", "Absolutbezug_Zahl\n", "Brennwert\n", "Broteinheiten\n", "Ethanolgehalt\n", "Galenische_Grundform\n",
                 "Relativbezug_Einheit\n", "Relativbezug_Zahl\n", "Status_Hilfsstoffe\n"], axis=1, inplace=True)

    fak_df = fak_df.replace('\n', '', regex=True)

    fak_df.columns = ["Index", "Key_FAM", "Abgabeform", "Absolutbezug_Einheit", "Freisetzung", "Komponentenname", "Relativbezug_Form"]
    fak_df.drop(["Index"], axis=1, inplace=True)

    fak_df.loc[fak_df['Abgabeform'] == 0, 'Abgabeform'] = "k.A."
    fak_df.loc[fak_df['Abgabeform'] == 1, 'Abgabeform'] = "fest"
    fak_df.loc[fak_df['Abgabeform'] == 2, 'Abgabeform'] = "flüssig"
    fak_df.loc[fak_df['Abgabeform'] == 3, 'Abgabeform'] = "gasförmig"
    fak_df.loc[fak_df['Abgabeform'] == 4, 'Abgabeform'] = "halbfest"
    fak_df.loc[fak_df['Freisetzung'] == 0, 'Freisetzung'] = "k.A."
    fak_df.loc[fak_df['Freisetzung'] == 1, 'Freisetzung'] = "schnell"
    fak_df.loc[fak_df['Freisetzung'] == 2, 'Freisetzung'] = "normal"
    fak_df.loc[fak_df['Freisetzung'] == 3, 'Freisetzung'] = "pH-abhängig"
    fak_df.loc[fak_df['Freisetzung'] == 4, 'Freisetzung'] = "verzögert"
    fak_df.loc[fak_df['Freisetzung'] == 5, 'Freisetzung'] = "differenziert"
    fak_df.loc[fak_df['Freisetzung'] == 6, 'Freisetzung'] = "konstant"
    fak_df.loc[fak_df['Freisetzung'] == 7, 'Freisetzung'] = "ohne"

    fak_df = fak_df.groupby("Key_FAM", as_index=False).agg({"Abgabeform":lambda x: "%s" % ', '.join(x),
                                             "Absolutbezug_Einheit":lambda x: "%s" % ', '.join(x),
                                             "Relativbezug_Form":lambda x: "%s" % ', '.join(x)
                                              })
    return fak_df

def editFAT(fat_df):
    fat_df.columns = ["Index", "Key_FAT", "Dat_Aktualisierung", "Dosierung", "Eigenschaften", "Haltbarkeit_Lagerung", "Hinweise", "Indikationen", "Kontraindikationen", "Nebenwirkungen", "Patientenhinweise"]
    fat_df.drop(["Index", "Dat_Aktualisierung"], axis=1, inplace=True)

    fat_df = fat_df.replace('\n', '', regex=True)
    fat_df['Key_FAT'] = fat_df['Key_FAT'].astype(str)

    return fat_df

#Pre and ending of files
pre = "Data/Datenbank/Excel/"
ending = "_DB.xlsx"

# Define the path
input_path_FAM = "FAM"
input_path_DAR = "DAR"
input_path_FAI = "FAI"
input_path_FAK = "FAK"
input_path_FAP = "FAP"
input_path_FAS = "FAS"
input_path_FAT = "FAT"
input_path_FZI = "FZI"
input_path_INT = "INT"
input_path_ITX = "ITX"
input_path_SNA = "SNA"
input_path_STO = "STO"
input_path_STX = "STX"
input_path_SZI = "SZI"

# Load the excel files
df_FAM = pd.read_excel(pre+input_path_FAM+ending, skiprows=1)
df_DAR = pd.read_excel(pre+input_path_DAR+ending, skiprows=1)
df_FAI = pd.read_excel(pre+input_path_FAI+ending, skiprows=1)
df_FAK = pd.read_excel(pre+input_path_FAK+ending, skiprows=1)
df_FAT = pd.read_excel(pre+input_path_FAT+ending, skiprows=1)
df_SNA = pd.read_excel(pre+input_path_SNA+ending, skiprows=1)
# FAS Nicht nutzbar, da Key_STA nicht vorhanden
# STO Besteht nur aus 0 und 1. Unnötig?
# FAP Interessant, aber wie Zahlen durch Wörter ersetzen? Key: Key_FAM
# Informationen über Interaktionen: Einbinden über FZI. Informationen beziehen aus INT & ITX. Komisch hier: Attribut: Textfeld in ITX
# Informationen über Stoffe: SNA schon eingebunden: Stoffnamen. STO besteht nur aus 0 & 1. STX: Volltext, aber starke Unterschiede? Einbinden?

# Merge all dataframes
df_merge = pd.DataFrame()

df_FAM = editFAM(df_FAM)
df_DAR = editDAR(df_DAR)
df_merge = df_FAM.merge(df_DAR, left_on="Key_DAR", right_on="Key_DAR", how="left")
#
df_FAI =editFAI(df_FAI, df_SNA)
df_merge = df_merge.merge(df_FAI, left_on="Key_FAM", right_on="Key_FAM", how="left")
#
df_FAK = editFAK(df_FAK)
df_merge = df_merge.merge(df_FAK, left_on="Key_FAM", right_on="Key_FAM", how="left")
#
df_FAT = editFAT(df_FAT)
df_merge = df_merge.merge(df_FAT, left_on="Key_FAT", right_on="Key_FAT", how="left")

df_merge.drop(["Key_ADR_Anbieter", "Key_ADR_Mitvertrieb", "Key_ATC", "Key_DAR", "Key_FAT", "Key_IND_Haupt", "Key_IND_Neben", "Key_ATCA", "Key_FAM"], axis=1, inplace=True)

writer = pd.ExcelWriter("Data/Datenbank/Excel/Merged_DB.xlsx")
df_merge.to_excel(writer, 'Sheet1')
writer.save()