# Edward
Python REST API which demonstrates the time and space complexity of various algorithms.

## Setup

```
$ git clone https://github.com/lukebarker3/Edward.git
$ cd Edward
$ pipenv install
```

## Startup

```
$ python3 app.py
```

This will startup the server which, currently, only returns JSON data. I am planning on updating the API to provide more flexible functionality, when I get the time...

## Examples

It is recommended you use an API testing application, such as [Postman](https://www.getpostman.com/apps "Postman Download Page"), to send your own requests.

### GET

Returns algorithm metadata - including a description, average run times, and a list of steps to execute the algorithm by hand.

E.g.

A request to **/algorithms/insertion-sort** will return metadata for the classic Insertion Sort algorithm.

### POST

Executes a desired algorithm on a dataset.

#### Options

These options should be set in the body of your POST request:

##### action
Should either be **run** or **test** - **run** just executes the algorithm and returns the results, **test** executes the algorithm multiple times on different datasets, recording the average times for each dataset and returns these results.

##### makegraph
When set to true, the **test** action will create a visual graph of the results returned from Edward, the ID of the graph is returned to you and can be accessed via a GET request to **/algorithms/graphs/<graph_id>**

##### options
Allows you to precisely control how the algorithm is executed through the test action:

###### min_size
The smallest number of elements the test collection must have. Must be at least 5. Default is 5.

###### max_size
The largest number of elements the test collection must have. Must be at least 10. Default is 20.

###### jump
The size to skip between collections. For example, if you wanted to test collections of sizes 10 to 200, but wanted to test sizes 10, 20, 30, 40 etc. then set **jump** to 10. Default is 1.

###### repeats
How many times should the **test** be repeated? Default is 5 repeats.

##### collection
Allows you to provide your own dataset, rather than allow Edward to generate it's own via the **run** or **test** commands.
