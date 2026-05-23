# shell.nix
{ pkgs ? import <nixpkgs> { } }:
pkgs.mkShell {
  nativeBuildInputs = [
    # Chrome driver and google-chrome dependencies
    pkgs.python311Packages.selenium
    pkgs.python311Packages.questionary
    #pkgs.chromedriver 
    #pkgs.google-chrome { allowUnfree = true; }

    # For Clipboard Access:
    # pkgs.clipboard-jh

    # Create a script to run google-chrome-stable
    (pkgs.writeShellScriptBin "chrome" "exec -a $0 ${pkgs.google-chrome}/bin/google-chrome-stable $@")
  ];

  # shellHook = ''
  #  export CLIPBOARD_NOAUDIO=true
  #  export CLIPBOARD_NOGUI=true
  #  export CLIPBOARD_SILENT=true
  #  export CLIPBOARD_NOREMOTE=true
  # '';
}
