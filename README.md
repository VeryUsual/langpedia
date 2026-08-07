# Langpedia

An encyclopedia of programming languages, built using a custom static site generator with a custom XML dialect. It provides history and explanations on various programming languages, as other sites like Wikipedia display them in a confusing, complicated fashion. Langpedia, on the other hand, provides information on programming languages, and makes it very easy to go through and look at information of programming languages.

<p float="middle">
  <img width="400" alt="image" src="https://github.com/user-attachments/assets/e85cd4d9-b21b-4ac8-b37d-9bf0acbf2245" />
  <img width="400" alt="image" src="https://github.com/user-attachments/assets/2edf76b9-6ee0-4b04-8192-f6d95b47ff92" />
</p>

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

Then, visit [127.0.0.1:8000](http://127.0.0.1:8000) in your browser of choice.

## License

The content on this site is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. The static site generator is licensed under the GNU General Public License Version 3.
