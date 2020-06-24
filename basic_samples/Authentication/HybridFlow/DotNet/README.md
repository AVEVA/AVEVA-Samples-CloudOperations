# Hybrid Flow Sample and Test

**Version:** 1.1.1

[![Build Status](https://dev.azure.com/osieng/engineering/_apis/build/status/product-readiness/OCS/Auth_Hybrid_DotNet?branchName=master)](https://dev.azure.com/osieng/engineering/_build?definitionId=847&branchName=master)

This client uses the OIDC Hybrid Flow to obtain an access token. See the root folder [README](../../../README.md) for more information about this flow.

## Requirements

- .NET Core 3.1 or later
- Web Browser with Javascript enabled
  - You will need Google Chrome if you want to run the automated test

1. Replace the placeholders in the [appsettings](appsettings.json) file with your Tenant Id, Client Id and Client Secret
2. Ensure that this client was created to allow Refresh Tokens
   - If this client does not allow refresh tokens, no refresh token will be issued upon authentication
3. Ensure that the client contains \$"{RedirectHost}:{RedirectPort}/{RedirectPath}" in the list of RedirectUris
   - Default value from config is: `https://127.0.0.1:54567/signin-oidc`
   - You can change the values to match your preferences

## Running the sample

### Prerequisites

- Register a Hybrid client in OCS and ensure that the registered client in OCS contains `https://127.0.0.1:54567/signin-oidc` in the list of RedirectUris.
- Replace the placeholders in the [appsettings](appsettings.json) file with your Tenant Id, Client Id, and Client Secret obtained from registration.

### Using Visual Studio

1. Load the .csproj in this directory
2. Rebuild project
3. Run it
   - If you want to see the token and other outputs from the program, put a breakpoint at the end of the main method and run in debug mode
4. Follow the prompts in the web browser to log in
   - Keep in mind that if you are already logged in with the same Account in the browser, you will not have to log in again
5. Return to the application after having been authenticated in the browser

### Using Command Line

- Make sure you have the install location of dotnet added to your path
- Run the following command from the location of this project:

```shell
dotnet run
```

- Follow the prompts in the web browser to log in
- Return to the application after having been authenticated in the browser

## Running the automated test

### Test Prerequisites

- Make sure Google Chrome is the default browser on your test system.
- Download the ChromeDriver version from `http://chromedriver.storage.googleapis.com/index.html` corresponding to the version of Google Chrome that is installed. Set the environmental variable ChromeWebDriver to the directory containing the Chrome Driver executable.
- Update the [appsettings.json](../HybridFlowTest/appsettings.json) with the username and password for the Microsoft account that will be used to log in. The test is only written to work with a personal Microsoft account and must only prompt for only username followed by password (no Two-Factor authentication or other consent or informational prompts). Also if the location of the sample application has been modified then change the RedirectHost and/or RedirectPort.

### Test Using Visual Studio

- Load the .csproj from the HybridFlowTest directory above this in Visual Studio
- Rebuild project
- Open Test Explorer and make sure there is one test called Test1 showing
- Run the test

### Test Using Command Line

- Make sure you have the install location of dotnet added to your path
- Run the following command from the location of the HybridFlowTest project (you may need to run as Administrator for the test to use the Chrome Driver):

```shell
dotnet test
```

---

Tested against DotNet 3.1.

For the general steps or switch languages see the Task [ReadMe](../../)  
For the main OCS page [ReadMe](https://github.com/osisoft/OSI-Samples-OCS)  
For the main samples page on master [ReadMe](https://github.com/osisoft/OSI-Samples)
