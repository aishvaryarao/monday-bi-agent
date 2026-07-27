import pandas as pd


class DataCleaner:
    @staticmethod
    def board_to_dataframe(items):
        rows = []

        for item in items:
            row = {
                "Item Name": item.get("name", "")
            }

            for column in item.get("column_values", []):
                title = column.get("column", {}).get("title", "")
                value = column.get("text", "")

                row[title] = value

            rows.append(row)

        return pd.DataFrame(rows)

    @staticmethod
    def clean_dataframe(df):
        df = df.copy()

        df = df.fillna("")

        df.columns = (
            df.columns.str.strip()
            .str.replace(" ", "_")
            .str.lower()
        )

        return df