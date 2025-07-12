Snippets are like [embedded files](embedded_files.md) but for small parts instead of the whole guide.  
They're useful for information that spreads across multiple guides.

## File structures

Snippets can be found in the `snippets` directory, and follow the same structure as guides.

```
📂docs
    ┗━📂snippets
        ┣━📂common
        ┃   ┗━📄[File Name].md
        ┗━📂[Publisher]
            ┣━📂common
            ┃   ┗━📄[File Name].md
            ┗━📂[Game Name]
                ┗━📄[File Name].md
```

To use them, simply add this line to your guide, changing the values with the snippet's name you wish to use.

``` md
;--8<-- "docs/snippets/[Publisher]/[Game Name]/[File Name].md"
```

For example, with our data warning snippet, here's how it will look.

``` md
;--8<-- "docs/snippets/common/data_warning.md"
```

--8<-- "docs/snippets/common/data_warning.md"

## When to use

Only use snippets when necessary and if they are shared between multiple games.  
We already have many snippets available and ready to use. Refer to the existing guides for examples.