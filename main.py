from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils import PossibleDate


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:63342",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/{date_input}')
async def read_item(date_input: str):
    possible_date = PossibleDate(date_input)
    parsed_date = possible_date.parse_date()
    if not parsed_date:
        return {"Error": "Failed to parse date"}
    weeks = possible_date.count_weeks(parsed_date)
    if not weeks:
        return {"Error": "Date is behind counting start"}
    return {"weeks": weeks}
