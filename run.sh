bash clean.sh

python lerobot_record.py \
    --robot.type G1 \
    --dataset.repo_id ymc/eval_g1 \
    --dataset.single_task "Retrieve the bottled ad calcium milk from the table with the right arm." \
    --dataset.push_to_hub False \
    --dataset.episode_time_s 10000000 \
    --policy.type xvla_client \
    --policy.url https://nat-notebook-inspire.sii.edu.cn/ws-6040202d-b785-4b37-98b0-c68d65dd52ce/project-5939d5ca-7339-4306-b57a-7696f8f7a4c1/user-5fd8c13a-1a2d-4ddb-8393-06cb7e005a55/vscode/2626e4db-71f2-4014-b5ad-d6b66775ce7b/dd6f0f46-83f6-40d4-abfa-f30e1381eb8f/proxy/8000/


# python lerobot_record.py \
#     --robot.type G1 \
#     --dataset.repo_id ymc/eval_g1 \
#     --dataset.single_task "Retrieve the bottled ad calcium milk from the table with the right arm." \
#     --dataset.push_to_hub False \
#     --dataset.episode_time_s 10000000 \
#     --policy.type go1_client \
#     --policy.url https://nat-notebook-inspire.sii.edu.cn/ws-6040202d-b785-4b37-98b0-c68d65dd52ce/project-5939d5ca-7339-4306-b57a-7696f8f7a4c1/user-5fd8c13a-1a2d-4ddb-8393-06cb7e005a55/vscode/2626e4db-71f2-4014-b5ad-d6b66775ce7b/dd6f0f46-83f6-40d4-abfa-f30e1381eb8f/proxy/8002/