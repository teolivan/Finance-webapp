'use client'
import { useState } from "react"
import axios from 'axios'; //axios parses JSON automatically, makes code cleaner

export default function Home() {
  const [ticker, setTicker] = useState("");
  const [result, setResult] = useState<StockResult | null>(null);

  type StockResult = {
    results: {
      ticker: string;
      name: string;
      market: string;
      price: string;
    };
  };

  const stockSearch = async () => {
    try {
        const response = await axios.get<StockResult>(`http://localhost:8000/stock/${ticker}`);
        setResult(response.data);

    } catch (error) {
      console.error("API error: ", error);
    }
  }

  return (

    <div className="flex flex-col justify-center items-center h-screen bg-gray-900">

      <img src="logo.svg" alt="" className="h-[200px] mb-8"/>

      <div className="flex items-center gap-x-4">


        <input
          type="text"
          value={ticker}
          onChange={(e) => setTicker(e.target.value.toUpperCase())}
          className="w-[200px] h-[50px] bg-white text-gray-700 px-4 rounded focus:outline-none"
          placeholder="Enter ticker here..."
        />
        <button onClick={stockSearch} className="bg-white hover:bg-gray-100 text-gray-700 h-[50px] font-semibold py-2 px-4 border border-gray-400 rounded shadow">
          Search
        </button>
      </div>

      {result && (
            <div>
              <h2>Ticker: {result.ticker}</h2> //need to fix this
              <p>Price: {result.price}</p>
            </div>

        )}
    </div>
  );
}
