import os
import httpx
from dotenv import load_dotenv

load_dotenv()


class MondayClient:
    BASE_URL = "https://api.monday.com/v2"

    def __init__(self):
        self.api_token = os.getenv("MONDAY_API_TOKEN")

        if not self.api_token:
            raise ValueError("MONDAY_API_TOKEN not found.")

        self.headers = {
            "Authorization": self.api_token,
            "Content-Type": "application/json"
        }

    def get_board_items(self, board_id):
        query = """
        query ($board_id: ID!) {
          boards(ids: [$board_id]) {
            items_page(limit: 500) {
              items {
                id
                name
                column_values {
                  text
                  column {
                    title
                  }
                }
              }
            }
          }
        }
        """

        try:
            response = httpx.post(
                self.BASE_URL,
                headers=self.headers,
                json={
                    "query": query,
                    "variables": {
                        "board_id": str(board_id)
                    }
                },
                timeout=30
            )

            response.raise_for_status()

        except httpx.TimeoutException:
            raise Exception(
                "The request to Monday.com timed out. Please try again."
            )

        except httpx.RequestError:
            raise Exception(
                "Unable to connect to Monday.com. Please check your internet connection."
            )

        except httpx.HTTPStatusError as e:
            raise Exception(
                f"Monday.com API returned an error (Status Code: {e.response.status_code})."
            )

        data = response.json()

        if "errors" in data:
            error_message = data["errors"][0].get("message", "Unknown GraphQL error.")
            raise Exception(f"Monday.com Error: {error_message}")

        try:
            return data["data"]["boards"][0]["items_page"]["items"]
        except (KeyError, IndexError):
            raise Exception(
                "Unable to retrieve board data. Please verify that the board ID is correct."
            )