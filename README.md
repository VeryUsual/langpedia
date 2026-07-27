# Langpedia

An encyclopedia of programming languages, built using a custom static site generator with a custom XML dialect.

## Usage

Access the site [here](https://veryusual.github.io/langpedia/).

### Manual Build Instructions

```
git clone https://github.com/VeryUsual/langpedia
cd langpedia
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 ssg.py run
```

## License

The content on this site is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. The static site generator is licensed under the GNU General Public License Version 3.