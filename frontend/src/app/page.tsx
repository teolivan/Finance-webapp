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
      description: string;
      locale: string;
      logo_url: string;
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
            <div className="flex flex-col justify-center items-center h-250 bg-gray-900 w-300">
              <h1 className="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white">{result.results.name} ({result.results.ticker})</h1> 
              <p className="mb-6 text-lg font-normal text-gray-500 lg:text-xl sm:px-16 xl:px-48 dark:text-gray-400">Locale: {result.results.locale}</p>
              <p className="mb-6 text-lg font-normal text-gray-500 lg:text-xl sm:px-16 xl:px-48 dark:text-gray-400">Market: {result.results.market}</p>
              <p className="mb-6 text-lg font-normal text-gray-500 lg:text-xl sm:px-16 xl:px-48 dark:text-gray-400">{result.results.description}</p>
              <img src={result.results.logo_url} alt={result.results.name} />
            </div>

        )}
    </div>
  );
}
