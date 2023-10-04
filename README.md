# AVEVA ADH Samples

AVEVA Data Hub ([ADH](https://www.osisoft.com/Solutions/OSIsoft-Cloud-Services/)) is a highly flexible cloud-based platform that provides a scalable, elastic,
centralized environment to aggregate data for reporting, advanced analytics, and third-party applications. ADH is powered by AVEVA's Sequential Data Store (SDS). In this GitHub repo, we provide samples which will help you get started with the [ADH API](https://ocs-docs.osisoft.com/) against your [ADH instance](https://cloud.osisoft.com/welcome).

If you are interested in other AVEVA samples please see [AVEVA Samples](https://github.com/osisoft/OSI-Samples).

If you are new to our APIs and are looking to get going quickly, the  [Types, Streams, and Retrieving Data](https://github.com/osisoft/OSI-Samples-OCS/blob/main/docs/COMMON_ACTIONS.md) samples are good starting points.

The official ADH samples are divided in multiple categories depending on the scenario and problem/task, accessible through the following table. 

Click here for general  <a href="https://github.com/osisoft/OSI-Samples-OCS/blob/main/docs/AUTHENTICATION.md"><b>Authentication</b></a> information.

<details open><summary><a href="https://github.com/osisoft/sample-adh-authentication_client_credentials-dotnet"><b>Client Credentials</b></a></summary>
          <a href="https://github.com/osisoft/sample-adh-authentication_client_credentials-dotnet">.NET Libraries</a> <br />
          <a href="https://github.com/osisoft/sample-adh-authentication_client_credentials_simple-dotnet">.NET REST API</a>    <br />
          <a href="https://github.com/osisoft/sample-adh-authentication_client_credentials_simple-java">Java</a>    <br />
          <a href="https://github.com/osisoft/sample-adh-authentication_client_credentials_simple-nodejs">NodeJS</a>    <br />
          <a href="https://github.com/osisoft/sample-adh-authentication_client_credentials_simple-postman">Postman</a>    <br />
          <a href="https://github.com/osisoft/sample-adh-authentication_client_credentials_simple-powershell">Powershell</a>    <br />
          <a href="https://github.com/osisoft/sample-adh-authentication_client_credentials_simple-python">Python</a>    <br />
          <a href="https://github.com/osisoft/sample-adh-authentication_client_credentials_simple-rust">Rust</a>    
</details>

<details open><summary><a href="https://github.com/osisoft/sample-adh-authentication_client_credentials-dotnet"><b>Authorization Code + PKCE</b></a></summary>
            <a href="https://github.com/osisoft/sample-adh-authentication_authorization-dotnet">.NET</a>    <br />
            <a href="https://github.com/osisoft/sample-adh-authentication_authorization-nodejs">NodeJS</a>    <br />
            <a href="https://github.com/osisoft/sample-adh-authentication_authorization-python">Python</a>
</details>

<details open><summary><a href="docs/SDS_TIME_SERIES.md"><b>Create, Read & Write Time-Series Data</b></a></summary>
            <a href="https://github.com/osisoft/sample-adh-time_series-python">Python </a>    <br />
            <a href="https://github.com/osisoft/sample-adh-time_series-dotnet">.NET</a>    <br />
</details>

<details open><summary><a href="docs/SDS_WAVEFORM.md"><b>Read & Write Data with a Sequential Index</b></a></summary>
                        <a href="https://github.com/osisoft/sample-adh-waveform_libraries-dotnet">.NET Libraries</a>    <br />
                         <a href="https://github.com/osisoft/sample-adh-waveform-python">Python</a>    <br />
</details>


**Note**: Tests with automated UI browser components (such as Hybrid Authentication, Authorization Code Flow and Angular samples) fail intermittently due to automation issues.

For OMF to ADH samples please see the OMF repository: [OSI-Samples-OMF](https://github.com/osisoft/OSI-Samples-OMF)

## Credentials

A credential file is used in the samples unless otherwise noted in the sample. The name and location of the credential file should be noted in the sample's ReadMe.  
**Note**: This is not a secure way to store credentials. This is to be used at your own risk.  
You will need to modify these files locally when you run the samples.

## About this repo

The [style guide](https://github.com/osisoft/.github/blob/main/STYLE_GUIDE.md) describes the organization of the repo and the code samples provided. The [test guide](https://github.com/osisoft/.github/blob/main/TEST_GUIDE.md) goes into detail about the included automated tests. The [on prem testing](https://github.com/osisoft/.github/blob/main/ON_PREM_TESTING.md) document describes the software installed on our internal AVEVA build agent.

## Feedback

To request a new sample, if there is a feature or capability you would like demonstrated, or if there is an existing sample you would like in your favorite language, please give us feedback at [https://feedback.aveva.com](https://feedback.aveva.com) under the Developer Samples category. [Feedback](https://datahub.feedback.aveva.com/ideas/search?category=7135134109509567625&query=sample).

## Support

If your support question or issue is related to something with an AVEVA product (an error message, a problem with product configuration, etc...), please open a case with AVEVA Tech Support through myAVEVA Customer Portal ([https://my.osisoft.com](https://my.osisoft.com)).

If your support question or issue is related to a non-modified sample (or test) or documentation for the sample; please email Samples@osisoft.com.

## Contributions

If you wish to contribute please take a look at the [contribution guide](https://github.com/osisoft/.github/blob/main/CONTRIBUTING.md).

## License

[OSI Samples](https://github.com/osisoft/OSI-Samples) are licensed under the [Apache 2 license](LICENSE).
