from fastapi import FastAPI, HTTPException
from keys import polygon_key
import httpx
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    
# to retrieve the logo & icon of the company
@app.get("/branding-image")
async def get_stock_info(url: str):
    url = f"{url}"
    print('test')
    print(url)
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
    
    #Retrieve the Simple Moving Average (SMA) for a specified ticker over a defined time range. 
    # The SMA calculates the average price across a set number of periods, 
    # smoothing price fluctuations to reveal underlying trends and potential signals.
    # e.g. of request url http://localhost:8000/stock/SMA/AAPL

@app.get("/stock/SMA/{ticker}") 
async def get_OHLC_info(ticker: str):
    url = f"https://api.polygon.io/v1/indicators/sma/{ticker}?timespan=day&adjusted=true&window=50&series_type=close&order=desc"
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
    