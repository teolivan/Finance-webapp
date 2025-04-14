'use client'
import { useState } from "react"

export default function Home() {
  const [ticker, setTicker] = useState("");

  return (

    <div className="flex flex-col justify-center items-center h-screen bg-gray-900">

      <img src="logo.svg" alt="" className="h-[200px] mb-8"/>

      <div className="flex items-center gap-x-4">


        <input
          type="text"
          value={ticker}
          onInput={(e) => setTicker(e.currentTarget.value.toUpperCase())}
          className="w-[200px] h-[50px] bg-white text-gray-700 px-4 rounded focus:outline-none"
          placeholder="Enter ticker here..."
        />
        <button className="bg-white hover:bg-gray-100 text-gray-700 h-[50px] font-semibold py-2 px-4 border border-gray-400 rounded shadow">
          Search
        </button>
      </div>
    </div>
  );
}
