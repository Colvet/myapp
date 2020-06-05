import pandas as pd

class MakeSummary:

    def analy(df):
        info = []
        for d in df:
            col_info = {
                "colName": d,
                "summary": {
                    "dataType": "String",
                    "deIdentified": "masking",
                    "prove": "K"
                }
            }
            info.append(col_info)

        return info
