from huggingface_hub import snapshot_download

# Downloads only the 10 archive files, skipping Git files and metadata
snapshot_download(
    repo_id="BodyMaps/PanTSMini",
    repo_type="dataset",
    allow_patterns="*.tar.gz",
    local_dir="./pants_mini_data",
    max_workers=1 # Set to 1 to download one large file at a time and avoid network crashes
)
