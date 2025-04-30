??? tip "Option 1: Remote (Online Network)"

    Head to the `[dns]` section inside `segatools.ini`. Set `default` to the address
    provided by your network. **Do not add `http://` or `https://` to the address!**

    ```ini
    [dns]
    default=network.example
    ```

    Then, head to the `[keychip]` section and add & set `id` to the keychip ID provided by your network:

    ```ini
    [keychip]
    subnet=192.168.139.0
    id=A69E-XXXXXXXXXXX
    ```

    Finally, you need a card number. Create a file named `aime.txt` inside `App\bin\DEVICE` and type in
    your 20-digit access code if you already have one, or make one up if you don't. If you're making one
    up, the access code **MUST NOT** start with a 3.

    ```
    📄aime.txt
        01234567890123456789
    ```