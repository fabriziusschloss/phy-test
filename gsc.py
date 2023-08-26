
import os
from dotenv import load_dotenv

# Laden Sie die Werte aus der .env-Datei
load_dotenv()

# Verwenden Sie den Wert aus der .env-Datei
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")

# ... Rest des Skripts bleibt unverändert ...


# Importieren Sie die erforderlichen Bibliotheken
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import httplib2

# Ersetzen Sie den Pfad zur JSON-Schlüsseldatei Ihres Servicekontos
#SERVICE_ACCOUNT_FILE = "C:\\Users\\fabian\\git-hub\\gaapireport-691250c1e39f.json"


# Definieren Sie den OAuth 2.0-Bereich (Scope) für die Google Search Console API
OAUTH_SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"

# Erstellen Sie die Anmeldeinformationen für das Servicekonto
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    SERVICE_ACCOUNT_FILE, scopes=[OAUTH_SCOPE])

# Erstellen Sie ein autorisiertes HTTP-Objekt
http_auth = credentials.authorize(httplib2.Http())

# Erstellen Sie das Search Console Service-Objekt
search_console = build("searchconsole", "v1", http=http_auth)

# Rufen Sie die Liste der verifizierten Websites des Benutzers ab
sites = search_console.sites().list().execute()

# Rufen Sie die Liste der verifizierten Websites des Benutzers ab
sites = search_console.sites().list().execute()

# Drucken Sie die Liste der verifizierten Websites
print("Verifizierte Websites:")

if "siteEntry" in sites:
    for site in sites["siteEntry"]:
        print(f"  - {site['siteUrl']}")
else:
    print("Es wurden keine verifizierten Websites gefunden.")

