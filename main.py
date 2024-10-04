#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import hashlib
import json
from datetime import datetime

def hash_dataframes(dfs):
    df_strings = []
    for df in dfs:
        df_json = df.to_json()
        df_strings.append(df_json)
    combined_string = "".join(df_strings)
    return hashlib.md5(combined_string.encode()).hexdigest()

def get_data(hostname):
    data = list()
    pageNumber = 1
    previous_hash = []
    
    while pageNumber < 100:
        url = hostname + f"/{pageNumber}/format/html?"
        dfs = pd.read_html(url)
        current_hash = hash_dataframes(dfs)
        
        if current_hash not in previous_hash:
            print(f"Neue Daten auf Seite {pageNumber} gefunden.")
            data.extend(dfs)
            previous_hash.append(current_hash)
        else:
            print(f"Keine neuen Daten auf Seite {pageNumber}.\n\n")
            break
        
        pageNumber += 1
        
    df = pd.DataFrame()
    for d in data:
        df = pd.concat([df,pd.DataFrame(d)], ignore_index=True)
        df.drop_duplicates(subset=['SIN'], inplace=True)
    
    return df

dzb = list()
types = {"Zertifikate in Zeichnung":    "https://www.dzbank-wertpapiere.de/product/list/index/inSubscription/1/rowsPerPage/100/page",
         "Zinsprodukte in Zeichnung":   "https://www.dzbank-wertpapiere.de/product/list/index/structure/InterestRateProducts/isBeforeSubscriptionEnd/1/rowsPerPage/100/page"}
for key, value in types.items():
    print("\n",key,"\n")
    
    df = get_data(value)
    anz = df.shape[0]
    
    for i in df.index:
        if key == "Zertifikate in Zeichnung":
            name = df["Produktname"][i]
        else:
            name = df["WKNRef.-Zins/Währung"][i]
        print(f"\t(({i+1:0{len(str(anz))}d}/{anz}):\tAbfrage von {name}")
        url = "https://www.dzbank-wertpapiere.de" + df["SIN"][i]
        data = pd.read_html(url.split(" ")[0])
        js = list()
        for d in data:
            if d.shape[1] == 2:
                js.append(dict(zip(d[d.columns[0]], d[d.columns[1]])))
            if d.shape[1] == 4:
                js.append({row[d.columns[0]]: [row[d.columns[1]], row[d.columns[2]], row[d.columns[3]]] for _, row in d.iterrows()})
        
        if key == "Zertifikate in Zeichnung":
            dzb.append({
                "Typ":                      key,
                "Allgemein":                json.loads(df[df.index == i].to_json(orient='records')),
                "URL":                      url.split(" ")[0],
                "Stammdaten":               dict(js[0], **js[1]),
                "Kennzahlen":               dict(js[2], **js[3]),
                "Basiswert":                dict(js[4], **js[5]),
                "Analyse":                  dict(js[6], **js[7]),
                "Abfragezeitpunkt":         datetime.now()
                })
        else:
            dzb.append({
                "Typ":                      key,
                "Allgemein":                json.loads(df[df.index == i].to_json(orient='records')),
                "URL":                      url.split(" ")[0],
                "Stammdaten":               dict(js[0], **js[1]),
                "Kennzahlen":               dict(js[2], **js[3]),
                "Abfragezeitpunkt":         datetime.now()
                })


#Datengrundlage in dzb geschaffen, individuelle Datenaufbereitung ab hier