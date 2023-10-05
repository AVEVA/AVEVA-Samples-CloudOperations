# AVEVA ADH Samples

AVEVA Data Hub ([ADH](https://www.aveva.com/en/products/aveva-data-hub/)) is a highly flexible cloud-based platform that provides a scalable, elastic,
centralized environment to aggregate data for reporting, advanced analytics, and third-party applications. ADH is powered by AVEVA's Sequential Data Store (SDS). In this GitHub repo, we provide samples which will help you get started with the [ADH API](https://ocs-docs.aveva.com/) against your [ADH instance](https://cloud.aveva.com/welcome).

If you are interested in other AVEVA samples please see [AVEVA Samples](https://github.com/aveva/OSI-Samples).

If you are new to our APIs and are looking to get going quickly, the  [Types, Streams, and Retrieving Data](https://github.com/aveva/OSI-Samples-OCS/blob/main/docs/COMMON_ACTIONS.md) samples are good starting points.

The official ADH samples are divided in multiple categories depending on the scenario and problem/task, accessible through the following table. 

Click here for general  <a href="https://github.com/aveva/OSI-Samples-OCS/blob/main/docs/AUTHENTICATION.md"><b>Authentication</b></a> information.

<details><summary><a href="https://www.aveva.com/en/products/aveva-data-hub/"><b> AVEVA Data Hub</b></a><img width="48" height="48"
                src="https://github.com/AVEVA/AVEVA-Samples/blob/main/miscellaneous/images/application-aveva-connect.png"></summary> 
<table align="middle" width="100%">
  <tr>
    <td align="left" valign="top">
  <a href="https://github.com/aveva/OSI-Samples-OCS/blob/main/docs/AUTHENTICATION.md"><b>Authentication</b></a>
        <details open><summary><a href="https://github.com/aveva/sample-adh-authentication_client_credentials-dotnet"><b>Client Credentials</b></a></summary>
                <a href="https://github.com/aveva/sample-adh-authentication_client_credentials-dotnet">.NET Libraries</a> <br />
                <a href="https://github.com/aveva/sample-adh-authentication_client_credentials_simple-dotnet">.NET REST API</a>    <br />
                <a href="https://github.com/aveva/sample-adh-authentication_client_credentials_simple-java">Java</a>    <br />
                <a href="https://github.com/aveva/sample-adh-authentication_client_credentials_simple-nodejs">NodeJS</a>    <br />
                <a href="https://github.com/aveva/sample-adh-authentication_client_credentials_simple-postman">Postman</a>    <br />
                <a href="https://github.com/aveva/sample-adh-authentication_client_credentials_simple-powershell">Powershell</a>    <br />
                <a href="https://github.com/aveva/sample-adh-authentication_client_credentials_simple-python">Python</a>    <br />
                <a href="https://github.com/aveva/sample-adh-authentication_client_credentials_simple-rust">Rust</a>    
        </details>
        <details open><summary><a href="https://github.com/aveva/sample-adh-authentication_client_credentials-dotnet"><b>Authorization Code + PKCE</b></a></summary>
                    <a href="https://github.com/aveva/sample-adh-authentication_authorization-dotnet">.NET</a>    <br />
                    <a href="https://github.com/aveva/sample-adh-authentication_authorization-nodejs">NodeJS</a>    <br />
                    <a href="https://github.com/aveva/sample-adh-authentication_authorization-python">Python</a>
        </details>
    </td>
    <td align="left" valign="top">
    <a href="https://github.com/aveva/OSI-Samples-OCS/blob/main/docs/COMMON_ACTIONS.md"><b>Types, Streams,
        Events, and Retrieving Data</b></a>
<details open><summary><a href="docs/SDS_TIME_SERIES.md"><b>Create, Read & Write Time-Series Data</b></a></summary>
            <a href="https://github.com/aveva/sample-adh-time_series-python">Python </a>    <br />
            <a href="https://github.com/aveva/sample-adh-time_series-dotnet">.NET</a>    <br />
</details>

<details open><summary><a href="docs/SDS_WAVEFORM.md"><b>Read & Write Data with a Sequential Index</b></a></summary>
                        <a href="https://github.com/aveva/sample-adh-waveform_libraries-dotnet">.NET Libraries</a>    <br />
                         <a href="https://github.com/aveva/sample-adh-waveform-python">Python</a>    <br />
</details>

<details open><summary><a href="docs/PI_TO_ADH_READ_DATA.md"><b> PI to ADH Read Only Streams </b></a></summary>
            <a href="https://github.com/aveva/sample-pi-to-adh-read-only-data-dotnet">.NET</a>
</details>

<details open><summary><a href="https://github.com/aveva/sample-adh-streaming-updates_rest_api-dotnet"><b>  Streaming Updates </b></a></summary>
            <a href="https://github.com/aveva/sample-adh-streaming-updates_rest_api-dotnet">.NET</a>
</details>

<details open><summary><a href="https://github.com/aveva/sample-adh-event_store-python"><b>   Event Data </b></a></summary>
              <a href="https://github.com/aveva/sample-adh-event_store-python">Python</a>
</details>

<details open><summary><a href="https://github.com/aveva/OSI-Samples-OCS/blob/main/docs/DATA_INGRESS.md"><b>   Data Ingress </b></a></summary>
        <a href="https://github.com/aveva/sample-adh-omf_ingress-dotnet">OMF Ingress</a>
</details>

<details open><summary><a href="https://github.com/aveva/sample-adh-csv_to_adh-dotnet"><b>   CSV to ADH </b></a></summary>
            <a href="https://github.com/aveva/sample-adh-csv_to_adh-dotnet">.NET</a>
</details>
    </td>
    <td align="left" valign="top">
<a href="https://github.com/aveva/OSI-Samples-OCS/blob/main/docs/VISUALIZATION.md"><b>Visualization</b></a>
<details open><summary><a href="https://github.com/aveva/sample-adh-grafana_backend_plugin-datasource"><b>   Grafana </b></a></summary>
            <a href="https://github.com/aveva/sample-adh-grafana_backend_plugin-datasource">NodeJS</a>
</details>

<details open><summary><a href="https://github.com/aveva/sample-sds-visualization-angular"><b>   SDS Visualization </b></a></summary>
            <a href="https://github.com/aveva/sample-sds-visualization-angular">Angular</a>
</details>

<details open><summary><a href="docs/ASSETS.md"><b>   Assets </b></a></summary>
            <a href="https://github.com/aveva/sample-adh-assets_rest_api-dotnet">.NET</a>    <br />
            <a href="https://github.com/aveva/sample-adh-assets-python">Python</a>
</details>
    
<details open><summary><a href="https://github.com/aveva/sample-ocs-data_retrieval-power_query_m"><b>   Power Query M </b></a></summary>
            <a href="https://github.com/aveva/sample-ocs-data_retrieval-power_query_m">Power Query M</a>
</details>
    </td>    
    <td align="left" valign="top">
    <a href="https://github.com/aveva/OSI-Samples-OCS/blob/main/docs/ANALYTICS.md"><b>Analytics</b></a>
<details open><summary><a href="docs/DATA_VIEWS.md"><b>   Data Views</b></a></summary>
            <a href="https://github.com/aveva/sample-adh-data_views-python">
              Python
            </a>    <br />
            <a href="https://github.com/aveva/sample-adh-data_views-dotnet">
              .NET
            </a>
</details>

<details open><summary><a href="https://github.com/aveva/sample-adh-data_views_jupyter-python"><b>   Data Views Jupyter</b></a></summary>
            <a href="https://github.com/aveva/sample-adh-data_views_jupyter-python">Jupyter Notebook</a>
</details>

<details open><summary><a href="https://github.com/aveva/sample-adh-data_views_r-r"><b>   Data Views R</b></a></summary>
            <a href="https://github.com/aveva/sample-adh-data_views_r-r">R</a>
</details>
    </td>
    <td align="left" valign="top">
    <a href="https://github.com/aveva/OSI-Samples-OCS/blob/main/docs/OTHER.md"><b>Functionality & Utilities</b></a>
<details open><summary><a href="https://github.com/aveva/sample-adh-uom-dotnet"><b>   UOM</b></a></summary>
            <a href="https://github.com/aveva/sample-adh-uom-dotnet">
              .NET
            </a>
</details>

<details open><summary><a href="https://github.com/aveva/sample-adh-data_views_jupyter-python"><b>   Data Views Jupyter</b></a></summary>
            <a href="https://github.com/aveva/sample-adh-data_views_jupyter-python">Jupyter Notebook</a>
</details>

<details open><summary><a href="https://github.com/aveva/sample-adh-namespace_data_copy-python"><b>   Namespace Data Copy</b></a></summary>
            <a href="https://github.com/aveva/sample-adh-namespace_data_copy-python">Python</a>
</details>

<details open><summary><a href="docs/SAMPLE_LIBRARIES.md"><b>   Sample Libraries </b></a></summary>
            <a href="https://github.com/aveva/sample-adh-sample_libraries-python">
              Python
            </a>
</details>

<details open><summary><a href="https://github.com/aveva/sample-ocs-security_management-python"><b>  Security Management</b></a></summary>
            <a href=https://github.com/aveva/sample-ocs-security_management-python">
              Python
            </a>

<details open><summary><a href="https://github.com/aveva/sample-ocs-stream_type_change-python"><b>  Stream Type Change</b></a></summary>
            <a href="https://github.com/aveva/sample-ocs-stream_type_change-python">
              Python
            </a>
</details>

<details open><summary><a href="https://github.com/aveva/sample-adh-pi_to_adh_transfer_verification-powershell"><b> PI to AVEVA Data Hub Transfer Verification Sample</b></a></summary>
            <a href="https://github.com/aveva/sample-adh-pi_to_adh_transfer_verification-powershell">
              Powershell
            </a>
</details>

<details open><summary><a href="https://github.com/aveva/sample-adh-data_hub_to_pi-python"><b>  Data Hub to PI</b></a></summary>
            <a href="https://github.com/aveva/sample-adh-data_hub_to_pi-python">
              Python
            </a>
</details>
    </td>

  </tr>
</table>
</details>

<details><summary><a href="https://www.aveva.com/en/products/aveva-data-hub/"><b> AVEVA PI System</b></a><img width="48" height="48"
                src="https://github.com/AVEVA/AVEVA-Samples/blob/main/miscellaneous/images/configuration--operations-management.png"></summary> 
<table align="middle" width="100%">
  <tr>
   <td align="left" valign="top">
    <a href="https://github.com/aveva/OSI-Samples-OCS/blob/main/docs/OTHER.md"><b>Functionality & Utilities</b></a>
<details open><summary><a href="https://github.com/aveva/sample-adh-uom-dotnet"><b>   UOM</b></a></summary>
            <a href="https://github.com/aveva/sample-adh-uom-dotnet">
              .NET
            </a>
</details>

<details open><summary><a href="https://github.com/aveva/sample-adh-data_views_jupyter-python"><b>   Data Views Jupyter</b></a></summary>
            <a href="https://github.com/aveva/sample-adh-data_views_jupyter-python">Jupyter Notebook</a>
</details>

<details open><summary><a href="https://github.com/aveva/sample-adh-namespace_data_copy-python"><b>   Namespace Data Copy</b></a></summary>
            <a href="https://github.com/aveva/sample-adh-namespace_data_copy-python">Python</a>
</details>

<details open><summary><a href="docs/SAMPLE_LIBRARIES.md"><b>   Sample Libraries </b></a></summary>
            <a href="https://github.com/aveva/sample-adh-sample_libraries-python">
              Python
            </a>
</details>

<details open><summary><a href="https://github.com/aveva/sample-ocs-security_management-python"><b>  Security Management</b></a></summary>
            <a href=https://github.com/aveva/sample-ocs-security_management-python">
              Python
            </a>

<details open><summary><a href="https://github.com/aveva/sample-ocs-stream_type_change-python"><b>  Stream Type Change</b></a></summary>
            <a href="https://github.com/aveva/sample-ocs-stream_type_change-python">
              Python
            </a>
</details>

<details open><summary><a href="https://github.com/aveva/sample-adh-pi_to_adh_transfer_verification-powershell"><b> PI to AVEVA Data Hub Transfer Verification Sample</b></a></summary>
            <a href="https://github.com/aveva/sample-adh-pi_to_adh_transfer_verification-powershell">
              Powershell
            </a>
</details>

<details open><summary><a href="https://github.com/aveva/sample-adh-data_hub_to_pi-python"><b>  Data Hub to PI</b></a></summary>
            <a href="https://github.com/aveva/sample-adh-data_hub_to_pi-python">
              Python
            </a>
</details>
    </td>
  </tr>
</table>
</details>


**Note**: Tests with automated UI browser components (such as Hybrid Authentication, Authorization Code Flow and Angular samples) fail intermittently due to automation issues.

For OMF to ADH samples please see the OMF repository: [OSI-Samples-OMF](https://github.com/aveva/OSI-Samples-OMF)

## Credentials

A credential file is used in the samples unless otherwise noted in the sample. The name and location of the credential file should be noted in the sample's ReadMe.  
**Note**: This is not a secure way to store credentials. This is to be used at your own risk.  
You will need to modify these files locally when you run the samples.

## About this repo

The [style guide](https://github.com/aveva/.github/blob/main/STYLE_GUIDE.md) describes the organization of the repo and the code samples provided. The [test guide](https://github.com/aveva/.github/blob/main/TEST_GUIDE.md) goes into detail about the included automated tests. The [on prem testing](https://github.com/aveva/.github/blob/main/ON_PREM_TESTING.md) document describes the software installed on our internal AVEVA build agent.

## Feedback

To request a new sample, if there is a feature or capability you would like demonstrated, or if there is an existing sample you would like in your favorite language, please give us feedback at [https://feedback.aveva.com](https://feedback.aveva.com) under the Developer Samples category. [Feedback](https://datahub.feedback.aveva.com/ideas/search?category=7135134109509567625&query=sample).

## Support

If your support question or issue is related to something with an AVEVA product (an error message, a problem with product configuration, etc...), please open a case with AVEVA Tech Support through myAVEVA Customer Portal ([https://my.aveva.com](https://my.aveva.com)).

If your support question or issue is related to a non-modified sample (or test) or documentation for the sample; please email Samples@aveva.com.

## Contributions

If you wish to contribute please take a look at the [contribution guide](https://github.com/aveva/.github/blob/main/CONTRIBUTING.md).

## License

[OSI Samples](https://github.com/aveva/OSI-Samples) are licensed under the [Apache 2 license](LICENSE).
