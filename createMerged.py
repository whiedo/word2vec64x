import pandas as pd

def editFAM(fam_df):
    fam_df.drop(["Aufbrauch_KS_Einheit\n", "Aufbrauch_KS_Zahl\n", "Aufbrauch_RT_Einheit\n", "Aufbrauch_RT_Zahl\n", "Dat_Ausbietung\n", "Dat_Ersterfassung\n",
                 "Dat_Zusammensetzung\n", "EMA_Zulassung\n", "Sofortiger_Verbrauch\n", "Therapierichtung_AM\n"], axis=1, inplace=True)

    fam_df.loc[fam_df['Abgabebestimmung\n'] == "0\n", 'Abgabebestimmung\n'] = "nicht verschreibungspflichtig"
    fam_df.loc[fam_df['Abgabebestimmung\n'] == "1\n", 'Abgabebestimmung\n'] = "verschreibungspflichtig"
    fam_df.loc[fam_df['Abgabebestimmung\n'] == "3\n", 'Abgabebestimmung\n'] = "Betäubungsmittel"
    fam_df.loc[fam_df['Einmalige_Anwendung\n'] == "1\n", 'Einmalige_Anwendung\n'] = "Zur einmaligen Anwendung nach Anbruch/Zubereitung"
    fam_df.loc[fam_df['Feuchtigkeitsschutz\n'] == "1\n", 'Feuchtigkeitsschutz\n'] = "Vor Feuchtigkeit schützen"
    fam_df.loc[fam_df['Lichtschutz\n'] == "1\n", 'Lichtschutz\n'] = "Vor Licht schützen"
    fam_df.loc[fam_df['Monopraeparat\n'] == 0, 'Monopraeparat\n'] = "Kombipräparat"
    fam_df.loc[fam_df['Monopraeparat\n'] == 1, 'Monopraeparat\n'] = "Monopräparat"
    fam_df.loc[fam_df['Produktgruppe\n'] == 1, 'Produktgruppe\n'] = "Arzneimittel"
    fam_df.loc[fam_df['Produktgruppe\n'] == 2, 'Produktgruppe\n'] = "Medizinprodukt"
    fam_df.loc[fam_df['Produktgruppe\n'] == 3, 'Produktgruppe\n'] = "Diätetikum"
    fam_df.loc[fam_df['Produktgruppe\n'] == 4, 'Produktgruppe\n'] = "Rezepturgrundstoff"
    fam_df.loc[fam_df['Produktgruppe\n'] == 5, 'Produktgruppe\n'] = "Nahrungsergänzungsmittel"
    fam_df.loc[fam_df['Produktgruppe\n'] == 6, 'Produktgruppe\n'] = "Körperpflegemittel"
    fam_df.loc[fam_df['Produktgruppe\n'] == 7, 'Produktgruppe\n'] = "Desinfektionsmittel"
    fam_df.loc[fam_df['Produktgruppe\n'] == 8, 'Produktgruppe\n'] = "Sonstiges Nichtarzneimittel"
    fam_df.loc[fam_df['Verkehrsstatus\n'] == 1, 'Verkehrsstatus\n'] = "im Handel"
    fam_df.loc[fam_df['Verkehrsstatus\n'] == 2, 'Verkehrsstatus\n'] = "außer Vertrieb"
    fam_df.loc[fam_df['Verkehrsstatus\n'] == 4, 'Verkehrsstatus\n'] = "vor Markteinführung"
    fam_df.loc[fam_df['Verkehrsstatus\n'] == 5, 'Verkehrsstatus\n'] = "nicht verkehrsfähig"
    fam_df.loc[fam_df['Veterinaerpraeparat\n'] == 0, 'Veterinaerpraeparat\n'] = "Humanpräparat"
    fam_df.loc[fam_df['Veterinaerpraeparat\n'] == 1, 'Veterinaerpraeparat\n'] = "Veterinärpräparat"
    fam_df.loc[fam_df['Zusaetz_Ueberwachung\n'] == 0, 'Zusaetz_Ueberwachung\n'] = "Arzneimittel unterliegt keiner zusätzlichen Überwachung"
    fam_df.loc[fam_df['Zusaetz_Ueberwachung\n'] == 1, 'Zusaetz_Ueberwachung\n'] = "Arzneimittel unterliegt einer zusätzlichen Überwachung"
    return fam_df

def editFAI(fai_df, sna_df):
    fai_df.drop(["Komponentennr\n", "Rang\n", "Einheit\n", "Entsprichtstoff\n", "Stofftyp\n", "Suffix\n", "Zahl\n", "Vergleich\n", "Verwendung_intern\n"], axis=1, inplace=True)
    fai_df = fai_df.merge(sna_df, left_on="Key_STO\n", right_on="Key_STO\n", how="left")
    fai_df.drop(["Zaehler\n", "Herkunft\n", "Sortierbegriff\n", "Suchbegriff\n", "Vorzugsbezeichnung\n", "Key_STO\n"], axis=1, inplace=True)
    # fai_df = fai_df.groupby("Key_FAM\n")["Name\n"].apply(lambda x: "%s" % ', '.join(x))
    fai_df = fai_df.groupby("Key_FAM\n", as_index=False)["Name\n"].agg({"Name\n":lambda x: "%s" % ', '.join(x)})
    return fai_df

def editFAK(fak_df):
    fak_df.drop(["Komponentennr\n", "Absolutbezug_Zahl\n", "Brennwert\n", "Broteinheiten\n", "Ethanolgehalt\n", "Galenische_Grundform\n",
                 "Komponentenname\n", "Relativbezug_Einheit\n", "Relativbezug_Zahl\n", "Status_Hilfsstoffe\n"], axis=1, inplace=True)
    fak_df.loc[fak_df['Abgabeform\n'] == 0, 'Abgabeform\n'] = "k.A."
    fak_df.loc[fak_df['Abgabeform\n'] == 1, 'Abgabeform\n'] = "fest"
    fak_df.loc[fak_df['Abgabeform\n'] == 2, 'Abgabeform\n'] = "flüssig"
    fak_df.loc[fak_df['Abgabeform\n'] == 3, 'Abgabeform\n'] = "gasförmig"
    fak_df.loc[fak_df['Abgabeform\n'] == 4, 'Abgabeform\n'] = "halbfest"
    fak_df.loc[fak_df['Freisetzung\n'] == 0, 'Freisetzung\n'] = "k.A."
    fak_df.loc[fak_df['Freisetzung\n'] == 1, 'Freisetzung\n'] = "schnell"
    fak_df.loc[fak_df['Freisetzung\n'] == 2, 'Freisetzung\n'] = "normal"
    fak_df.loc[fak_df['Freisetzung\n'] == 3, 'Freisetzung\n'] = "pH-abhängig"
    fak_df.loc[fak_df['Freisetzung\n'] == 4, 'Freisetzung\n'] = "verzögert"
    fak_df.loc[fak_df['Freisetzung\n'] == 5, 'Freisetzung\n'] = "differenziert"
    fak_df.loc[fak_df['Freisetzung\n'] == 6, 'Freisetzung\n'] = "konstant"
    fak_df.loc[fak_df['Freisetzung\n'] == 7, 'Freisetzung\n'] = "ohne"

    # fak_df = fak_df.groupby("Key_FAM\n")["Name\n"].apply(lambda x: "%s" % ', '.join(x)).reset_index()
    fak_df = fak_df.groupby("Key_FAM\n", as_index=False).agg({"Abgabeform\n":lambda x: "%s" % ', '.join(x),
                                             "Absolutbezug_Einheit\n":lambda x: "%s" % ', '.join(x),
                                             "Relativbezug_Form\n":lambda x: "%s" % ', '.join(x)
                                              })
    return fak_df

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

# Merge all dataframes
df_merge = pd.DataFrame()

#TODO Column "Key_FAT" funktioniert nicht
df_FAM = editFAM(df_FAM)
df_merge = df_FAM.merge(df_DAR, left_on="Key_DAR\n", right_on="Key_DAR\n", how="left")

df_FAI =editFAI(df_FAI, df_SNA)
df_merge = df_merge.merge(df_FAI, left_on="Key_FAM\n", right_on="Key_FAM\n", how="left")
df_merge.drop(["0_x", "0_y"], axis=1, inplace=True)

df_FAK = editFAK(df_FAK)
df_merge = df_merge.merge(df_FAK, left_on="Key_FAM\n", right_on="Key_FAM\n", how="left")

df_merge = df_merge.merge(df_FAT, left_on="Key_FAT\n", right_on="Key_FAT\n", how="left")

writer = pd.ExcelWriter("Data/Datenbank/Excel/Merged_DB.xlsx")
df_merge.to_excel(writer, 'Sheet1')
writer.save()