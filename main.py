from fastapi import FastAPI
from utils import PossibleDate


app = FastAPI()


@app.get('/{date_input}')
async def read_item(date_input: str):
    possible_date = PossibleDate(date_input)
    parsed_date = possible_date.parse_date()
    if not parsed_date:
        return {"Error": "Failed to parse date"}
    weeks = possible_date.count_weeks(parsed_date)
    return {"weeks": weeks}
