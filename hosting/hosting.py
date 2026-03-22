from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HUGGINGFACE_ACCESS_KEY"))
api.upload_folder(
    folder_path="deployment",     # the local folder containing your files
    repo_id="rkpworks/Bank-Customer-Churn",          # the target repo
    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)
