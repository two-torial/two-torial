!!! tip ""

    - Extract the update to your game directory, ensure directories align and overwrite files when prompted
    - Open `prop\ea3-config.xml` and find the `<ext>` line:
    ```xml
    <ext __type="str">NewDateCode</ext>
    ```
    - Update the datecode to match your new game version and save
    - If `prop\bootstrap.xml` exists, also update its `<release_code>` line:
    ```xml
    <release_code>NewDateCode</release_code>
    ```