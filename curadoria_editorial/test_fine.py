import sys
from pathlib import Path
BASE_DIR = Path("Ferramentas_Traducao")
sys.path.insert(0, str(BASE_DIR))
from artonelico_tool.project import encoded_size

print("--- 32633 (CAP 80B) ---")
for s in [
    "Tripolar?!CRLyner, por que fez isso?!",
    "Tripolar?! Por que fez isso?!",
    "Tripolar?! Lyner, por queCRfez isso?!",
    "Tripolar?! Por que foiCRfazer isso?!"
]:
    print(s, encoded_size(s))

print("--- 32664 (CAP 96B) ---")
for s in [
    "Céus... Você anda estranhoCRultimamente, Lyner...",
    "Céus... Você anda bem estranhoCRultimamente...",
    "Puxa... Você anda tão estranhoCRultimamente, Lyner...",
    "Nossa... Você anda tão estranhoCRultimamente...",
    "Céus... Você anda meio estranhoCRultimamente..."
]:
    print(s, encoded_size(s))

print("--- 32666 (CAP 88B) ---")
for s in [
    "Por que criou partesCRdo meu próprio corpo?",
    "Por que fez partesCRdo meu próprio corpo?",
    "Por que refez partesCRdo meu próprio corpo?",
    "Por que criou partesCRdo meu corpo?"
]:
    print(s, encoded_size(s))

print("--- 32706 (CAP 104B) ---")
for s in [
    'Pensando bem, "Mini-Inferior"CRsoa mais fofo...',
    'Pensando bem, "Inferiorzinho"CRsoa mais bonitinho...',
    'Pensando bem, "Inferiorzinho"CRsoa bem mais fofo...',
    '"Grathnode Petit"CRsoa bem mais bonitinho...'
]:
    print(s, encoded_size(s))
