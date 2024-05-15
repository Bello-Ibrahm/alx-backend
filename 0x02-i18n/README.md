# 0x02. i18n 

# Tasks
## 0. Basic Flask app 
First you will setup a basic Flask app in `0-app.py`. Create a single `/` route and an `index.html` template that simply outputs “Welcome to Holberton” as page title (`<title>`) and “Hello world” as header (`<h1>`).



Initialize (babel.cfg) the translations with:
```
pybabel extract -F babel.cfg -o messages.pot .
```
Result in `AttributeError: module 'jinja2.ext' has no attribute 'autoescape'`

To fix this modify the babel.cfg to below - [Resource](https://stackoverflow.com/questions/72651555/attributeerror-module-jinja2-ext-has-no-attribute-autoescape-while-trying-t):
```
[python: **.py]
[jinja2: **/templates/**.html]
;extensions=jinja2.ext.autoescape,jinja2.ext.with_
```
and your two dictionaries with
```
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
```
