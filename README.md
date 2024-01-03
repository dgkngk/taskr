# taskr

## To setup backend

Create a python virtual environment
```sh
python -m venv venv
```
Activate and Setup Environment
```sh
. venv/bin/activate
cd ./backend/taskr-be/ 
pip install -r requirements.txt
```
Export PYTHONPATH variable
```sh
env PYTHONPATH=$cwd
```
Run Flask server
```sh
flask run
```

## To setup frontend
### Install npm
https://www.npmjs.com/package/npm

### Install packages
```sh
cd ./frontend/taskr-fe/
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```
