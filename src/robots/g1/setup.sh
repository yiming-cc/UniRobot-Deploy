sudo apt install iproute2
pip install -r requirements_gui.txt

# install sdk from robot (run after connected to G1)
curl -sSL http://10.42.0.101:8849/install.sh | bash

# setup env
cd a2d_sdk/
source env.sh
