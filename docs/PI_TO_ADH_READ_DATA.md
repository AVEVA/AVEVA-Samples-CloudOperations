# PI to ADH Read Data Samples

The sample code in the folders below demonstrate how to invoke SDS REST APIs via the sample client libraries to read data from PI to ADH streams ingressed to Data Hub.
The steps performed in the samples are similar and follow the general flow as shown on [Read Data Docs](https://docs.osisoft.com/bundle/data-hub/page/api-reference/sequential-data-store/sds-read-data-api.html):

1. Authenticate against ADH
1. Retrieve stream
1. Retrieve Window events
1. Retrieve Window events in table form
1. Retrieve Window events using paging
1. Retrieve Range events
1. Retrieve Interpolated events
1. Retrieve Filtered events

| Languages | Test Status |
| --- | --- | 
[Python](https://github.com/osisoft/sample-pi-to-adh-read-only-data-python) | [![Build Status](https://dev.azure.com/osieng/engineering/_apis/build/status/product-readiness/ADH/aveva.sample-pi-to-adh-read-only-data-python?branchName=main)](https://dev.azure.com/osieng/engineering/_build/latest?definitionId=4498&branchName=main) |
| [.NET](https://github.com/osisoft/sample-pi-to-adh-read-only-data-dotnet)   | [![Build Status](https://dev.azure.com/osieng/engineering/_apis/build/status/product-readiness/ADH/aveva.sample-pi-to-adh-read-only-data-dotnet?branchName=main)](https://dev.azure.com/osieng/engineering/_build/latest?definitionId=4507&branchName=main)                                             |

For the main ADH page [ReadMe](https://github.com/osisoft/OSI-Samples-OCS)  
For the main samples page [ReadMe](https://github.com/osisoft/OSI-Samples)