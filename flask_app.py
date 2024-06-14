from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_babel import Babel, _
import json
import os

from src.life import main
app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'
# babel = Babel(app)

# setup language support
LANGUAGES = {
    'en': 'English',
    'zh': 'Chinese',
    'ja': 'Japanese'
}


def get_locale():
    #  try to guess the language from the user accept header the browser transmits.
    return request.accept_languages.best_match(LANGUAGES.keys())


babel = Babel(app, locale_selector=get_locale)


@app.context_processor
def inject_locale():
    return dict(get_locale=get_locale)


#   load config.json
def load_config():
    with open('src/config/config.json', 'r', encoding='utf-8') as file:
        config_data = json.load(file)
    return config_data


# save config.json
def save_config(config_data):
    with open('src/config/config.json', 'w', encoding='utf-8') as file:
        json.dump(config_data, file, indent=4, ensure_ascii=False)


# index
@app.route('/')
def index():
    config_data = load_config()
    return render_template('index.html', config=config_data)


# config edit
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        # get form data and save it to config.json
        config_data = request.form.to_dict(flat=False)
        print(config_data)
        nested_data = parse_nested_form(config_data)
        save_config(nested_data)
        return redirect(url_for('index'))
    else:
        config_data = load_config()
        return render_template('edit.html', config=config_data)


def unflatten_dict(d):
    result_dict = {}
    for k, v in d.items():
        keys = k.split('.')
        d = result_dict
        for key in keys[:-1]:
            d = d.setdefault(key, {})
        d[keys[-1]] = v[0]  # assume only one value per key
    return result_dict

def parse_nested_form(form):
    config = {}
    for key, value in form.items():
        parts = key.split('.')
        current = config
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        current[parts[-1]] = value[0]
    return config

# run life
@app.route('/run', methods=['GET','POST'])
def run_life():
    config_path = 'src/config/config.json'
    # script_dir = os.path.dirname(os.path.abspath(__file__))
    main(config_path)
    # output_path =  os.path.join(script_dir ,load_config()['output_file_path'])

    # output_path = 'results/output.txt'
    # result = subprocess.run(['python', 'life.py', config_path], capture_output=True, text=True)
    # print(result)
    # with open(output_path, 'w', encoding='utf-8') as file:
    #     file.write(result.stdout)
    return redirect(url_for('download_file'))

# download output file
@app.route('/download')
def download_file():
    # directory = 'results'
    filename = load_config()['output_file_path']
    directory = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(directory, filename)


if __name__ == '__main__':
    app.run(debug=True)
