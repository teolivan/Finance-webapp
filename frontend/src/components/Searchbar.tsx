

const Searchbar = () => {
    return ( 
        <div>
            <div className="flex items-center">
          <input type="text" placeholder="Enter ticker..." className="mr-4"/>
          <button>Search</button>
          </div>
        </div>
    );
};

export default Searchbar;