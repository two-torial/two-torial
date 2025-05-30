    ??? info "Relative Paths"

        Relative paths make your configuration portable and easier to maintain.
        
        Say your game folder structure looks like this:

        ```
        📂Game Folder
        ┣━📂App
        ┃ ┗━📝segatools.ini
        ┗━📂Option
        ```

        If `segatools.ini` needs to access the `Option` folder, you can use `../../Option/`:
        
        - `../` moves up from `bin` to `App`
        - `../` moves up again from `App` to the root `Game Folder`
        - Then it can access the `Option` folder