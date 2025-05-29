    ??? info "Relative Directories"

        The `../` in the above example represents the parent directory in a relative path. It is used to navigate up one level in the directory hierarchy.

        For example, your segatools.ini is located at `/App/bin/segatools.ini` and your Option folder is located next to the App folder.

        Since segatools.ini is in the `/bin/` folder, typing `../` would move you up to the App folder. Since the Option folder is next to the App folder, the second `../` takes you to `App`'s parent folder, which is the folder containing `App`, `Option`, etc.

        The benefits of using this method include:

        - Avoiding issues that arise when folders have spaces in their names.

        - Being able to move your game folder without redefining the locations of your VFS folders.

        - A cleaner and easier to read segatools.ini, making spotting issues simpler.