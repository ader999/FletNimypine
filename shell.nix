{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    # Python environment
    python3
    python3Packages.pip
    python3Packages.virtualenv

    # Flutter SDK for building
    flutter

    # Libraries for graphics and sound
    mesa
    openal
    
    # For USB device access (Android deployment)
    android-tools
    
    # For patching binaries
    patchelf
  ];

  shellHook = ''
    export SSL_CERT_FILE=${pkgs.cacert}/etc/ssl/certs/ca-bundle.crt
    export FLET_BUILD=true
  '';
}