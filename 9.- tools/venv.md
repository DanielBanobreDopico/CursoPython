# venv

## Creación de venv
```bash
mkdir proyecto
cd proyecto
python3 -m venv venv
git init
echo 'venv' > .gitignore
source venv/bin/activate
pip install django
pip freeze > requirements.txt
pip list
deactivate # salimos del entorno
pip list # y vemos que los paquetes se instalaron sólo en el venv
```

## Reconstrucción de venv
```bash
cd proyecto
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip list
deactivate # salimos del entorno
pip list # y vemos que los paquetes se instalaron sólo en el venv
```