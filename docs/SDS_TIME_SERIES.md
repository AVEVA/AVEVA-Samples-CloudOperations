# Welcome

The SDS Client time series samples are introductory, language-specific samples of programming against the SDS Service. They are intended as instructional samples only.

There are some differences between these samples and the Waveform samples. The differences include the Type being used, compression settings, and many of the steps. Please check out the Sample Pattern and code of both samples to determine which sample is most appropriate for you. The ReadMe of each sample will also discuss its compression strategy.

## Sample Pattern

All SDS Time Series samples are console applications that follow the same sequence of events, allowing you to select the langauge with which you are most comfortable without missing any instructional features. The pattern followed is:

1. Instantiate an SDS client and obtain an authentication token
1. Create an SdsType to represent a time value pair
1. Create SdsStreams to store event data in
1. Insert data of Simple Type
1. Create an SdsType to represent a complex type that has 2 values and a timestamp
1. Create SdsStream to store event data in
1. Insert data of Complex Type
1. View window data
1. View window data after turning on AcceptVerbosity
1. View summary data
1. Do bulk call on stream retrieval
1. Delete objects

These steps illustrate the fundamental programming steps of SDS. Feel free to modify the samples and/or propose changes.

Step numbers are searchable in the code. For example to find the relevant part of the code for accepting verbosity, search: `step 9`

| Languages  | 
| --- |
| [Python](https://github.com/osisoft/sample-adh-time_series-python) |
| [DotNet](https://github.com/osisoft/sample-adh-time_series-dotnet) | 

---

For the main ADH page [ReadMe](../../)  
For the main samples page [ReadMe](https://github.com/osisoft/OSI-Samples)
