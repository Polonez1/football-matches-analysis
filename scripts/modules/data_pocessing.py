import json
import pandas as pd
import sys

import open_load_save as ols


def create_main_table(json_object: json) -> pd.DataFrame:
    json_headers = ols.open_json(relative_path="\\json", file_name="table_headers.json")
    columns = json_headers["tables"]["general_table"]["columns"]

    df = pd.DataFrame(json_object["data"])
    return df
