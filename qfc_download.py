#!/usr/bin/env python

import os
from qfieldcloud_sdk import sdk
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("QFIELDCLOUD_TOKEN", None)

client = sdk.Client(
    url="https://app.qfield.cloud/api/v1/",
    token=token
)

try:
    client.download_project(
        project_id=os.environ.get("QFIELDCLOUD_PROJECT_ID"),
        local_dir=os.environ.get("QFIELDCLOUD_LOCAL_DIR"),
        filter_glob=os.environ.get("QFIELDCLOUD_FILTER_GLOB"),
        show_progress=True,
    )
except Exception as e:
    print(e)
