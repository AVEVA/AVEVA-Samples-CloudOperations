# Intro

This document is a guide on how to connect to CONNECT data services (Cds) using a client of your choice. We will first cover the difference between authorization (AuthZ) and authentication (AuthN) and how they relate to you as a developer of ADH. Then we will introduce some possible scenarios using some GitHub examples.

## Authentication

In the realm of web security, authentication is about proving to a second party that you are who you say you are. For example, I, as a user (_resource owner_), use a website (_client_) to authenticate against a backend service (_authorization server_) so that I can access resources from that same or another backend service (_resource server_). In other words, before I can check my mail using a web browser I need to authenticate using my username and password. After this step is concluded the browser receives a token, which it then uses on any subsequent request to the backend email server to fetch my emails. This token will in most cases have an expiration, after which it either needs to be renewed, using a refresh token or going through the process again, or it is no longer valid.

## Authorization

Authorization is related to, but not the same as authentication. Authorization is about proving to a second party that you are allowed to access some resources on it. This means that you have already proven you are who you say you are, and have been provided with some sort of token to prove your identity.

If you are taking a flight, at the gate you show your ticket to prove that you are authorized to access the flight. You also show a form of identification to show that you are the person whose name is listed on that ticket; in other words, you authenticate yourself.

## ADH Authentication and Authorization

ADH uses implementations of [OpenID Connect](https://openid.net/connect/) connect and [OAuth 2.0](https://oauth.net/2/) to handle authentication and authorization. Our implementation of these protocols relies on third party _Identity Providers_ (e.g., Microsoft Accounts, Azure Active Directory, etc.), and does not allow user accounts to be created or stored in ADH.

## All the Parties involved

For the rest of this document we will use the following language to refer to the parties involved during authentication and authorization,

- Resource Owner - This is a typically a user who owns some sort of resource in a server. For example, a company employee who has been registered as part of a tenant.
- Client - Any software that the _resource owner_ uses to access resources. For example, a console app used to access data, a web browser, or a native application.
- Resource Server - The server that holds some resources, owned by users, which they try to access. For example, the Cds Service that hold data for a tenant.
- Authorization Server - The server that generates an Access Token for a client once it has been authenticated and given the right permissions by the resource owner. In our case this would be the Cds Identity Service.
- IdentityProvider - a third party that creates, maintains, and manages identity information for principals while providing authentication services. For example, Microsoft Account and Azure Active Directory.

## Other terms

These are some of the terms that you will encounter in this document and other related OAuth 2.0 and OpenID Connect literature.

- [JSON Web Token (JWT)](https://jwt.io/introduction/) - A three part, period delimited, base 64 encoded string, that contains header, claims, and signature. The signature is a cryptographically encrypted version of the body, which when possesing the right cryptographic keys, is used to verify the authenticity and integrity of the header and claims components. These tokens have an expiration time.
- Claims - A list of key value pairs that provide some information about the Resource Owner, client, and audience. These claims are base 64 encoded, and are used in the backend and frontend to determine the user and the tenant it belongs to among other things.
- Access Token - The JWT that results from a successful authentication process, and contains some predefined fields. This is sent as part of the Authorization header with all the following requests in the session.
- Refresh Token - A token used to get a new Access Token after the current one expires, without having to go through the authentication process again. Usually has a long expiration date.

## Cds Supported Authenticated Flows

Currently Cds supports a number of authentication flows. Based on your requirements choose the one that best fits your needs. The following subsections are more technical and implementation oriented than the first part of the document.

### Authorization Code Flow with PKCE

If you are developing any Javascript/Browser (SPA) based applications or native mobile applications, with the user (resource owner) trying to access resources, use this flow. This flow adds an extra layer of security on top of the OIDC implicit flow by:

1. Requiring a client-verified code exchange for access token
2. By not returning the access token in a redirect URI.

In this OIDC flow, no refresh token is provided.

Authorization Code Flow supports silent refresh, which makes it possible to receive a new access token while the user is both using the application and logged in with the Identity Provider in the same browser session. This is done behind the scenes without interrupting the user experience.

The sample for this authentication flow can be found [here for DotNet](https://github.com/osisoft/sample-adh-authentication_authorization-dotnet), [here for NodeJS](https://github.com/osisoft/sample-adh-authentication_authorization-nodejs), and [here for Python](https://github.com/osisoft/sample-adh-authentication_authorization-python).

### Client Credential Flow

If you are writing software (client) to communicate with Cds without the presence of a user, then this is authentication flow you should follow. This flow was created for machine to machine communication.

A client is any software that a resource owner uses to access his resources on a remote server. In this case the client itself is the resource owner, and there is no actual user to perform the authentication process. The client uses his Client Id and Client Secret to authenticate against Cds and is awarded an Access Token. It is assumed that the client stores the Client Secret in a safe location, and uses cryptographically secure channels -read https- to communicate with Cds. Cds only supports communication over https. No Refresh Token is awarded.

The overall steps for this process are as follows:
1. Obtain the needed configuration information, including Tenant ID, Client ID, and Client Secret
1. Check the token (authentication) endpoint from the ADH discovery URL
1. POST the Client ID and Secret to the token endpoint in order to get an access (bearer) token 
1. Pass it back to ADH in the Authorization header in subsequent calls (the base tenant endpoint is used in these samples)

The samples for this authentication flow are found in the `Client Credential Flow` section of the table below.

### Hybrid Flow

If you are developing a traditional thick applications, with the user trying to access resources this should be your authentication method of choice. This flow provides a more secure means of authenticating, but also has the most constraining requirements. In this case the user will authenticate against the identity provider using any type of browser, even an unsafe one. Once this is completed the server-side client will authenticate against the authorization server and be awarded an Access Token and a Refresh Token, which should never be displayed to the user or the browser.

The sample for this authentication flow can be found [here](https://github.com/osisoft/sample-adh-authentication_hybrid-dotnet).

| Tasks  | Languages  | 
| ---- | --- |
| **Authorization Code Flow** | [.NET](https://github.com/osisoft/sample-adh-authentication_authorization-dotnet) </br> [NodeJS](https://github.com/osisoft/sample-adh-authentication_authorization-nodejs) </br> [Python](https://github.com/osisoft/sample-adh-authentication_authorization-python) | 
| **Client Credential Flow**  | [.NET Libraries](https://github.com/osisoft/sample-adh-authentication_client_credentials-dotnet) </br> [.NET REST API](https://github.com/osisoft/sample-adh-authentication_client_credentials_simple-dotnet) </br> [Java](https://github.com/osisoft/sample-adh-authentication_client_credentials_simple-java) </br> [NodeJS](https://github.com/osisoft/sample-adh-authentication_client_credentials_simple-nodejs) </br> [Postman](https://github.com/osisoft/sample-adh-authentication_client_credentials_simple-postman)</br> [Powershell](https://github.com/osisoft/sample-adh-authentication_client_credentials_simple-powershell) </br> [Python](https://github.com/osisoft/sample-adh-authentication_client_credentials_simple-python) </br> [Rust](https://github.com/osisoft/sample-adh-authentication_client_credentials_simple-rust) |
| **Hybrid Flow**             | [.NET](https://github.com/osisoft/sample-adh-authentication_hybrid-dotnet)  |

For the main ADH page [ReadMe](https://github.com/osisoft/OSI-Samples-adh)  
For the main samples page [ReadMe](https://github.com/osisoft/OSI-Samples)
