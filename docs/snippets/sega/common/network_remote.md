??? tip "Option 1: Remote (Online Network)"

    - Head to the `[dns]` section inside `segatools.ini`
    - Set `default` to the address provided by your network  
    **Do not add `http://` or `https://` to the address!**

    ```ini
    [dns]
    default=network.example
    ```

    - Then, head to the `[keychip]` section and add & set `id` to the keychip ID provided by your network  
    **Do not change the subnet from its default unless told to by your network!**

    ```ini
    [keychip]
    subnet=192.168.XXX.XXX
    id=A69E-XXXXXXXXXXX
    ```

    - Create a file named `aime.txt` inside `App\bin\DEVICE` and type in a 20-digit access code  
    If you don't already have one, simply make one up, just know **it must not start with the number 3!**

    ```
    📄aime.txt
        01234567890123456789
    ```