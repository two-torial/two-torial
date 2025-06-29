If you would like to cover multiple game versions that have the same exact setup process, you can use **embeddable files**. The [O.N.G.E.K.I. guides](https://github.com/two-torial/two-torial/tree/master/docs/games/sega/ongeki) are a good example of this.

In short, each game version only include the game's title and logo, followed by a line that inserts the guide from the `common` folder.

## File structure

Here's what the file structure should look like when using embedded files for a game.

```
📂docs
    ┣━📂games
    ┃   ┗━📂[Publisher]
    ┃       ┗━📂[Game Name]
    ┃           ┣━📂[Version 1]
    ┃           ┃   ┣━📄[File Name 1].md
    ┃           ┃   ┗━📄[File Name 2].md
    ┃           ┣━📂[Version 2]
    ┃           ┃   ┣━📄[File Name 1].md
    ┃           ┃   ┗━📄[File Name 2].md
    ┃           ┗━📂common
    ┃               ┣━📄[File Name 1].md
    ┃               ┗━📄[File Name 2].md
    ┗━📂img
       ┗━📂[Publisher]
            ┗━📂[Game Name]
                ┣━📂[Version 1]
                ┃   ┗━🖼️logo.webp
                ┣━📂[Version 2]
                ┃   ┗━🖼️logo.webp
                ┗━📂common
                    ┣━🖼️[Image Name 1].webp
                    ┗━🖼️[Image Name 2].webp
```

The actual guide should be in the `common` folder of the `docs` directory. The images used in the guide should be in the `common` folder in the `img` directory.

## Files content

In individual versions, there should be only two lines, one for the game logo and the other inserting the guide from the `common` folder.

Below is an example for `setup.md`, which is the main part of a game guide.

``` md title="/games/[Publisher]/[Game Name]/[Version 1]/setup.md"
<img class="header-logo" src="/img/[Publisher]/[Game Name]/[Version 1]/logo.webp">
;--8<-- "docs/games/[Publisher]/[Game Name]/common/setup.md"
```

As for the guide in the `common` folder, it should simply be the guide.

``` md title="/games/[Publisher]/[Game Name]/common/setup.md"
# Game Setup

Actual guide goes here.
```

Refer to existing guides for examples.