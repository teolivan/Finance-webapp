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
    
    # Retrieve aggregated historical OHLC (Open, High, Low, Close) and volume data for a specified stock ticker over a custom date range and time interval in Eastern Time (ET)
    # e.g. of request url http://localhost:8000/stock/OHLC/AAPL/1/day/2024-03-01/2024-03-10
@app.get("/stock/OHLC/{ticker}/{multiplier}/{timespan}/{timefrom}/{timeto}") 
async def get_OHLC_info(ticker: str, multiplier: str, timespan: str, timefrom: str, timeto: str):
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{timefrom}/{timeto}?adjusted=true&sort=asc&limit=120"
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
    

