!!! danger "Pick one or the other, not both!"

??? tip "Option 1: Remote (Online Network)"

    Remote networks typically require an invitation to join.  
    You'll need to connect with members of the community who can provide you with an invite.

    Your network should provide you with the necessary information to proceed:

    - Open `iidxhook-xx.conf` (xx being your game version) with a text editor

    - In the line `eamuse.server=localhost:80`, replace `localhost:80` with your provided network url

    - In the lines `eamuse.pcbid=XXXXXXXXXXXXXXXXXXXX` **and** `eamuse.eamid=XXXXXXXXXXXXXXXXXXXX`, replace the part after `=` with your provided PCBID
    
    - Example:
    ```
    # URL (e.g. http://my.eamuse.server:80/whatever) or IPV4 (e.g. 127.0.0.1:80) of the target eamuse server. The port is optional but defaults to 80.
    eamuse.server=http://be.ma.ni/

    # PCBID
    eamuse.pcbid=ABMYPRECIOUSPCBIDCDE

    # EAMID
    eamuse.eamid=ABMYPRECIOUSPCBIDCDE
    ```

??? tip "Option 2: Local e-amuse Emulator (Asphyxia)"

    For instructions on setting up Asphyxia, please refer to our [Asphyxia setup guide](/extras/asphyxia.md).

    After Asphyxia is setup with the proper plugin for your game:

    - Open `iidxhook-xx.conf` (xx being your game version) with a text editor

    - In the line `eamuse.server=localhost:80`, replace `localhost:80` to point to your asphyxia server, typically `localhost:8083`
    
    - Example:
    ```
    # URL (e.g. http://my.eamuse.server:80/whatever) or IPV4 (e.g. 127.0.0.1:80) of the target eamuse server. The port is optional but defaults to 80.
    eamuse.server=localhost:8083
    ```