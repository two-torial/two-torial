# Contributing to two-torial

## Git

1. Fork the Project ([guide](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository))
2. Clone your own project (`git clone https://github.com/yourname/two-torial.git`)
3. Create your Feature Branch (`git checkout -b branchname`)
4. Commit your Changes (`git add .` & `git commit -m "Added X and Y"`)
5. Push to the Branch (`git push origin branchname`)
6. Open a Pull Request ([guide](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project#making-a-pull-request))

## Local iteration

For quick local iteration, you can setup your own [mkdocs](https://www.mkdocs.org/user-guide/installation/) environment:

1. Install the latest [Python](https://www.python.org/) and [pip](https://pip.readthedocs.io/en/stable/installing/)
2. Make sure pip is up-to-date by running `pip install --upgrade pip`
3. Change directory to the root of your forked project and run `python -m pip install -r requirements.txt`
4. From the same root directory run `python -m mkdocs serve`

You can now access your live preview at `http://127.0.0.1:8000/`  
The live preview will update in real time as changes are found in your files.

## Adding new games

To add new games, the file structure should be as follows:

- For documentation: `docs/games/[Publisher]/[Game Name]/[Game Version]` then at least `setup.md`, and occasionally `controllers.md` and `troubleshooting.md`.
- For images: `docs/img/[Publisher]/[Game Name]/[Game Version]` with `logo.png` and any image needed for your guide.

### Embedded files

If you would like to cover multiple guides that have the same exact setup process, you use **embeddable files**. The [CHUNITHM guides](https://github.com/two-torial/two-torial/tree/master/docs/games/sega/chunithm) are a good example of this.

In short, each game version only include the game's title and logo, followed by a line of code that inserts the guide from the `common` folder.
Refer to existing guides for examples.

### mkdocs.yml

This file defines what should be on the website's left-side navigation bar. 
It mainly follows the file structure of the documentation.

There should be a "Game Setup" section, as well as occasional "Controllers" and "Troubleshooting" sections.
Refer to existing games for examples.

If you used [Embedded files](#embedded-files), make sure to include the `common` folder in `not_in_nav`.