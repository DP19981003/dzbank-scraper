
# Automatisierte Datenerfassung für DZ-Bank-Zertifikate und -Zinsprodukte

## Überblick

Dieses Repository enthält ein Python-Skript zur automatisierten Erfassung und Speicherung von Daten zu Zertifikaten und Zinsprodukten in der Zeichnungsphase. Es wurde speziell für Kreditinstitute entwickelt, um einen regelmäßigen, vollautomatischen Import dieser Wertpapierinformationen in ihr Datawarehouse zu ermöglichen.

## Funktionalität

- **Umfassende Datenabfrage**: Erfasst alle relevanten Zertifikate und Zinsprodukte in Zeichnung.
- **Strukturierte Datenspeicherung**: Jedes Wertpapier wird als eigenständiges Dictionary mit detaillierten Informationen gespeichert.
- **Zentrale Datensammlung**: Alle Wertpapier-Dictionaries werden in der Liste `dzb` (Datenbank Zeichnungsprodukte) zusammengeführt.

## Technische Details

### Verwendete Python-Pakete

- pandas
- json
- datetime
- hashlib

## Anwendungsbereiche

- Automatisierte Datenerfassung im Finanzsektor
- Regelmäßige Aktualisierung von Wertpapierinformationen
- Integration von Zeichnungsprodukten in Datawarehouse-Systeme

## Vorteile

- **Effizienz**: Schnelle und zuverlässige Erfassung großer Datenmengen
- **Aktualität**: Gewährleistung stets aktueller Marktinformationen
- **Flexibilität**: Einfache Anpassung an spezifische Anforderungen
- **Datenintegrität**: Sicherstellung durch Hash-Funktionen