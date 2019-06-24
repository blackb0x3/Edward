# Edward
Python x React application which demonstrates the time and space complexity of various algorithms.

## Setup

### Install dependencies

[Install pipenv](https://docs.pipenv.org/en/latest "pipenv info page")

```
$ python3 -m pip install --user pipenv
```

[Install node & npm (LTS version)](https://nodejs.org/en/download "NodeJS download page")

```
$ sudo apt-get update
$ sudo apt-get install nodejs
```

[Install yarn through npm](https://www.npmjs.com/package/yarn "yarn info page")

```
$ npm install -g yarn
```

## Startup

### Clone the repository

```
$ git clone https://github.com/lukebarker3/Edward.git
```

### Activate the pipenv shell environment

```
$ cd Edward
$ pipenv install
$ pipenv shell
```

### Build the React app

```
$ cd static
$ yarn install
$ yarn build
```

### Start the application

```
$ python3 app.py
```

This will startup the server and hosts both the React app and the Python REST API. Navigate to [localhost:5000](http://localhost:5000 "Edward's React app!") to access the React app once it has been built.

## The React App

Currently, the React app for this project is in the beta phase. Feel free to test it out and break it as much as you can, you could even make a new branch and submit your own pull request for the project!

## The REST API

It is recommended you use an API testing application, such as [Postman](https://www.getpostman.com/apps "Postman Download Page") or[Request Bin](https://requestbin.com "Request Bin Homepage"), to test and debug your own requests.

All API endpoints must be accessed via ```/api/path/to/endpoint```, as ```/``` will return the home page of the React app.

### Headers
| Content-Type
--- | ---
| application/json

### Endpoints

#### ```/api/algorithms``` (GET)

Returns a list of available algorithms which can be tested against the API (but not necessarily through the React appication!)

#### Example Response

```
{
    "available_algorithms": [
        "insertion-sort",
        "selection-sort",
        "traditional-bubble-sort",
        "optimised-bubble-sort",
        "recursive-quick-sort",
        "iterative-quick-sort",
        "counting-sort",
        "linear-search",
        "binary-search"
    ]
}
```

#### ```/api/algorithms/<algorithm_key>``` (GET)

Returns metadata for an algorithm specified by a given algorithm key (which can be fetched via ```/api/algorithms```)

#### Example Response

```
{
    "name": "Insertion Sort",
    "description": "An in-place, comparison-based sorting algorithm. It sorts array by shifting elements one by one and inserting the right element at the right position.",
    "steps": [
        "First Step",
        "Second Step",
        "Finally...",
        "Done"
    ],
    "best_case": "O(n) comparisons, O(1) swaps",
    "average_case": "O(n<sup>2</sup>) comparisons, O(n<sup>2</sup>) swaps",
    "worst_case": "O(n<sup>2</sup>) comparisons, O(n<sup>2</sup>) swaps"
}
```

Note the ```<sup>``` HTML tags used in the React app!

#### ```/api/algorithms/<algorithm_key>``` (POST)

Runs the algorithm and returns the execution statistics. These statistics vary based on the data provided in the POST request.

#### POST Options

key | action | collection | options | verbose
--- | --- | --- | --- |--- |--- |--- |--- |--- |--- |--- |---
description | run,test,compare | a data structure for the algorithm to execute | parameters used for test and compare actions to generate a data structure for your algorithm ([see below]()) | set to ```true``` to return data at each stage when performing a ```test``` or ```compare``` action
type | string | list,json | json | boolean

#### ```run``` and ```test``` options

option | min_size | max_size | jump | repeats
--- | --- | --- | --- |--- |--- |--- |--- |--- |--- |--- |---
description | minimum number of elements in the data structure | minimum number of elements in the data structure | element sizes to skip | number of times to repeat the experiment
type | int | int | int | int
default | 5 | 20 | 1 | 5

#### Example Response - RUN

```
{
    "successful_execution": true,
    "input": [
        2,
        5,
        4,
        3,
        8
    ],
    "output": [
        2,
        3,
        4,
        5,
        8
    ],
    "execution_start": "2019-06-24 01:13:57",
    "execution_end": "2019-06-24 01:13:57",
    "execution_time": "0:00:00.000012"
}
```

#### Example Response - TEST

```
{
    "sizes": [
        10,
        15,
        20,
        25,
        30
    ],
    "times": [
        0.0000194,
        0.00002,
        0.000029199999999999998,
        0.000042199999999999996,
        0.000053200000000000006
    ]
}
```

#### Example Response - TEST (verbose)

```
{
    "10": [
        {
            "successful_execution": true,
            "input": [
                883,
                852,
                5,
                906,
                648,
                883,
                778,
                896,
                188,
                936
            ],
            "output": [
                5,
                188,
                648,
                778,
                852,
                883,
                883,
                896,
                906,
                936
            ],
            "execution_start": "2019-06-24 01:17:19",
            "execution_end": "2019-06-24 01:17:19",
            "execution_time": "0:00:00.000015"
        },
        ...
        ...
        {
            "successful_execution": true,
            "input": [
                444,
                90,
                438,
                687,
                701,
                53,
                389,
                968,
                535,
                835
            ],
            "output": [
                53,
                90,
                389,
                438,
                444,
                535,
                687,
                701,
                835,
                968
            ],
            "execution_start": "2019-06-24 01:17:19",
            "execution_end": "2019-06-24 01:17:19",
            "execution_time": "0:00:00.000010"
        }
    ]
    ...
    ...
    "30": [
        {
            "successful_execution": true,
            "input": [
                737,
                551,
                286,
                231,
                38,
                204,
                503,
                332,
                457,
                817,
                877,
                1000,
                354,
                385,
                180,
                423,
                263,
                388,
                702,
                41,
                901,
                216,
                667,
                906,
                626,
                178,
                205,
                972,
                236,
                835
            ],
            "output": [
                38,
                41,
                178,
                180,
                204,
                205,
                216,
                231,
                236,
                263,
                286,
                332,
                354,
                385,
                388,
                423,
                457,
                503,
                551,
                626,
                667,
                702,
                737,
                817,
                835,
                877,
                901,
                906,
                972,
                1000
            ],
            "execution_start": "2019-06-24 01:17:19",
            "execution_end": "2019-06-24 01:17:19",
            "execution_time": "0:00:00.000048"
        },
        ...
    ]
}
```

#### ```/api/algorithmType/<algorithm_type>``` (GET)

Returns a list of available algorithms filtered to solve a particular computational problem (e.g. ```sorting```, ```searching```, ```knapsack``` etc.)

#### Example Response

```
{
    "insertion-sort": "INSERTION SORT",
    "selection-sort": "Selection Sort",
    "traditional-bubble-sort": "Traditional Bubble Sort",
    "optimised-bubble-sort": "Optimised Bubble Sort",
    "recursive-quick-sort": "Quick Sort - Recursive Version",
    "iterative-quick-sort": "Quick Sort - Iterative Version",
    "top-down-merge-sort": "Merge Sort - Top Down Approach",
    "bottom-up-merge-sort": "Merge Sort - Bottom Up Appproach",
    "heap-sort": "Heap Sort",
    "shell-sort": "Shell Sort",
    "counting-sort": "Counting Sort",
    "bucket-sort": "Bucket Sort"
}
```

## Pull Requests
Feel free to clone the repo, make a branch, and submit your own algorithms as pull requests. I've started working on different algorithms but not implemented all of them!
