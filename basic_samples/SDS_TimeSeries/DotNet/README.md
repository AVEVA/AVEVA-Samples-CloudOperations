# Building a DotNet client to make REST API calls to the SDS Service

**Version:** 1.1.8

[![Build Status](https://dev.azure.com/osieng/engineering/_apis/build/status/product-readiness/OCS/SDS_TS_DotNet?branchName=master)](https://dev.azure.com/osieng/engineering/_build/latest?definitionId=926&branchName=master)

The sample code in this topic demonstrates how to invoke the OCS client library. By examining the code, you will see how to create an SdsType and SdsStream, and how to create, read, update, and delete values in SDS. You will also see the summaries value call, and how to do bulk streams calls.

When working in .NET, it is recommended that you use the OCS Client Libraries metapackage, OSIsoft.OCSClients. The metapackage is a NuGet package available from [https://api.nuget.org/v3/index.json](https://api.nuget.org/v3/index.json). The libraries offer a framework of classes that make client development easier.

[SDS documentation](https://ocs-docs.osisoft.com/Content_Portal/Documentation/SequentialDataStore/Data_Store_and_SDS.html)

Developed against DotNet 2.2.300.

## Getting Started

In this example we assume that you have the dotnet core CLI.

To run this example from the commandline run

```shell
cd SDS_TS_DotNet
dotnet restore
dotnet run
```

to test this program change directories to the test and run

```shell
cd SDS_TS_DotNetTests
dotnet restore
dotnet test
```

## Configure constants for connecting and authentication

The sample is configured using the file [appsettings.placeholder.json](SdsTsDotNet/appsettings.placeholder.json). Before editing, rename this file to `appsettings.json`. This repository's `.gitignore` rules should prevent the file from ever being checked in to any fork or branch, to ensure credentials are not compromised.

The SDS Service is secured by obtaining tokens from Azure Active Directory. Such clients provide a client application identifier and an associated secret (or key) that are authenticated against the directory. You must replace the placeholders in the `appsettings.json` file with the authentication-related values you received from OSIsoft.

```json
{
  "NamespaceId": "REPLACE_WITH_NAMESPACE_ID",
  "TenantId": "REPLACE_WITH_TENANT_ID",
  "Resource": "https://dat-b.osisoft.com",
  "ClientId": "REPLACE_WITH_APPLICATION_IDENTIFIER",
  "ClientKey": "REPLACE_WITH_APPLICATION_SECRET"
}
```

## Try .NET

This sample is also provided in Try .NET. Currently using this in Try .NET is available only by self-hosting it.

To get to the try .MD file that walk over the sample click here:

- [Sample](Sample.md)

To learn more about try .NET and to learn how to install and use it please see [try .NET](https://github.com/dotnet/try). Included below are the abbreviated steps to do this.

1. from anywhere `dotnet tool install --global dotnet-try --version 1.0.19264.11`
2. from this directory run `dotnet try`

Note: you do not have to use this sample in try .NET. It will work like any other dotnet application.

---

For the general steps or switch languages see the Task [ReadMe](../../../)  
For the main OCS page [ReadMe](https://github.com/osisoft/OSI-Samples-OCS)  
For the main samples page on master [ReadMe](https://github.com/osisoft/OSI-Samples)
