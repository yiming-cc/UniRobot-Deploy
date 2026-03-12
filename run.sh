#!/bin/bash
conda activate unirobot

# # bimanual ur starVLA client
# python inference.py \
#   --client=bimanual_ur_starvla \
#   --host="https://ai-notebook-inspire.sii.edu.cn/ws-9dcc0e1f-80a4-4af2-bc2f-0e352e7b17e6/project-97ab58cb-3162-4d0e-9137-1299d6cdea25/user-6d664c70-4a65-47de-8033-c7f0bd1610c6/vscode/8ba7e934-e894-4b31-ad5b-d00e4b4854ae/428e3bed-9e03-4144-b209-3bf6195b5401/proxy/10093/" \
#   --task="Put all the items on the table into the drawer." \
#   --action_type=joint \
#   --fps=30 \
#   --execution_steps=16 \
#   --prefix_steps=8 \
#   --rtc \
#   --verbose


# bimanual ur dreamzero client
python inference.py \
  --client=bimanual_ur_dreamzero \
  --host="https://ai-notebook-inspire.sii.edu.cn/ws-9dcc0e1f-80a4-4af2-bc2f-0e352e7b17e6/project-97ab58cb-3162-4d0e-9137-1299d6cdea25/user-6d664c70-4a65-47de-8033-c7f0bd1610c6/vscode/8ba7e934-e894-4b31-ad5b-d00e4b4854ae/428e3bed-9e03-4144-b209-3bf6195b5401/proxy/10093/" \
  --task="Put all the items on the table into the drawer." \
  --action_type=joint \
  --fps=30 \
  --verbose