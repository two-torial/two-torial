# Modding Unity-based games

!!! danger "Before proceeding"
    This guide applies to games made in the Unity engine, such as maimai DX, O.N.G.E.K.I. and Card Maker.

	**It is highly recommended to use an unpatched Assembly DLL as your base!**

---

!!! info "Patches have historically been hardcoded into the unprotected `Assembly-CSharp.dll`"
    The modern approach is to use BepInEx to load custom patches without tampering with Assembly-CSharp.<br>BepInEx can be used to load all mods, including those made for MelonLoader and MonoMod

### Installing BepInEx
!!! tip ""
    - Download the [BepInEx 5 stable release](https://github.com/BepInEx/BepInEx/releases/latest) (`BepInEx_win_x64_5.x.y.z.zip`).
    !!! warning "Some maimai DX mods are only compatible with BepInEx 5.4.22"

    - Extract the `BepInEx` folder to the `App\package` folder (ignore other files such as `.doorstop_version`)

    - Modify `segatools.ini` with the following:

    ```ini
    [unity]
    enable=1
    targetAssembly=BepInEx\core\BepInEx.Preloader.dll
    ```
### Installing mods
!!! tip "BepInEx plugins"
    Place them in `BepInEx\plugins`.

!!! tip "Melonloader mods and plugins"
    - Download `MLLoader-UnityMono-BepInEx5` of the latest [BepInEx.MelonLoader.Loader](https://github.com/BepInEx/BepInEx.MelonLoader.Loader/releases/latest).
    - Extract it into `App\package`.
    - Place mods in `MLLoader\Mods`.

!!! tip "MonoMod patches"
    !!! info ""
        These patches always follow the naming pattern: `Assembly-CSharp.Name.mm.dll`.

    - Extract [BepInEx.MonoMod.Loader](https://github.com/BepInEx/BepInEx.MonoMod.Loader/releases/latest) into `App\package`.
    - Place patches in `BepInEx\monomod`.