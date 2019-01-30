#! /bin/bash

##########################################################################
set -e          # Fail fast if an error is encountered
set -o pipefail # Look at all commands in a pipeline to detect failure, not just the last
set -o functrace # Allow tracing of function calls
set -E          # Allow ERR signal to always be fired
##########################################################################


####### Error Handling ################
failure() {
    local lineno=$1
    local msg=$2
    echo "Failed at $lineno: $msg"
}
trap 'failure ${LINENO} "$BASH_COMMAND"' ERR
##########################################################################


python3.6 --version
python3.6 -c "import locale; locale.setlocale(locale.LC_ALL, '')"
python3.6 -v -m venv venv
source venv/bin/activate

mkdir -p $HOME/.pip

# pip3.6 install -r requirements.txt
pip3.6 download -d vendor -r requirements.txt --no-binary :all:

mkdir -p config/dev
cat > config/dev/.env <<WHATEVS3
REACT_APP_ENV=dev
REACT_APP_AUTH_URL=https://dev-sbr-ui.apps.cf1.ons.statistics.gov.uk
REACT_APP_API_URL=https://dev-sbr-ui.apps.cf1.ons.statistics.gov.uk/api
WHATEVS3

cat > config/dev/manifest.yml <<WHATEVS2
---
applications:
- name: sbr-ui
  memory: 1024M
  env:
    NODE_ENV: production
    SERVE_HTML: true
    NODE_TLS_REJECT_UNAUTHORIZED: 0
    SERVER_AUTH_URL: https://apigw-in-d-01.ons.statistics.gov.uk:9443/sbr/auth
    SERVER_API_GW_URL: https://apigw-in-d-01.ons.statistics.gov.uk:9443
    NODE_MODULES_CACHE: false
WHATEVS2

zip -r sbr-ui-5.zip .
