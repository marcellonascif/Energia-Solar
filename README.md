# Energia-Solar

### Comando para gerar o requirements:
pipdeptree --freeze --warn silence | findstr /R "^[a-zA-Z0-9]" | findstr /V "pipdeptree" > requirements.txt
