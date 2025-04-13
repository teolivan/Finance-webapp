from fastapi import FastAPI, HTTPException
from keys import polygon_key
import httpx

app = FastAPI()

@app.get("/stock/{ticker}")
async def get_stock_info(ticker: str):
    url = f"https://api.polygon.io/v3/reference/tickers/{ticker}"
    params = {"apiKey": polygon_key}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Polygon API error")

        data = response.json()
        return data

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")