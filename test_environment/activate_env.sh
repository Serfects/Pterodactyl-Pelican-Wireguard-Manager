#!/bin/bash
source /workspaces/Pterodactyl-Pelican-Wireguard-Manager/test_environment/venv/bin/activate
export FAKE_ROOT="/workspaces/Pterodactyl-Pelican-Wireguard-Manager/test_environment/fake_root"
export TESTING=true
export PYTHONPATH=$PYTHONPATH:/workspaces/Pterodactyl-Pelican-Wireguard-Manager/src/ppwm-dev:/workspaces/Pterodactyl-Pelican-Wireguard-Manager
