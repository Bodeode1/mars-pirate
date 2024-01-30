// Function to handle GET requests for fetching books data (API endpoint)
const getBooks = function(){
    this.json({
        books : [
            {
                title : "Seasons of the Witches",
                id : 1 , 
                price : 300 , 
                readers : 20
            }
        ]
    })
}

// Function to handle GET requests for rendering a view (webpage)
const getBooksViewHandler = function(){
    // 'this' refers to the context of the request
    const self = this;

    // Set a property in the repository (not a common practice, might be a typo)
    self.repository.firstName = "Adeleke";

    // Render the 'book' view
    self.view("book");
}

// Exported function for installing routes
exports.install = function(){
    // Define a route for handling GET requests to '/books' and invoking the getBooksViewHandler function
    ROUTE("GET /books" , getBooksViewHandler);
}
