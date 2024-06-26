# dotnet core 

### Installing dotnet core SDK and runtime in ubuntu 20.04 

# Installing .NET SDK 8 and Runtime on Ubuntu 20.04

Follow these steps to install the .NET SDK 8 and runtime on Ubuntu 20.04.

## Step 1: Update the Package Index

```bash
sudo apt update
wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb

sudo apt update
sudo apt install dotnet-sdk-8.0

sudo apt update
sudo apt install dotnet-runtime-8.0

```

### step 2 checking dotnet core version 

```
 dotnet --version 
8.0.301

```

### Creating webapp 

```
 dotnet new webapp -n AshuwebApp
The template "ASP.NET Core Web App (Razor Pages)" was created successfully.
This template contains technologies from parties other than Microsoft, see https://aka.ms/aspnetcore/8.0-third-party-notices for details.

Processing post-creation actions...
Restoring /home/azureuser/AshuwebApp/AshuwebApp.csproj:
  Determining projects to restore...
  Restored /home/azureuser/AshuwebApp/AshuwebApp.csproj (in 63 ms).
Restore succeeded.


azureuser@sre-vm:~$ ls
AshuwebApp  a.txt  hello
azureuser@sre-vm:~$ cd AshuwebApp/
azureuser@sre-vm:~/AshuwebApp$ ls
AshuwebApp.csproj  Pages  Program.cs  Properties  appsettings.Development.json  appsettings.json  obj  wwwroot
azureuser@sre-vm:~/AshuwebApp$ 

```

## Explanation of Directory strucutre 

# Project Structure

## Summary

- **Pages**: Holds Razor Pages and their code-behind files.
- **Properties**: Contains `launchSettings.json` for launch configuration.
- **bin**: Contains compiled binaries after building the application.
- **obj**: Holds intermediate build files and artifacts.
- **wwwroot**: Root directory for static files like CSS, JavaScript, and images.
- **Program.cs**: Entry point of the application, setting up the web host.
- **ashuwebApp.csproj**: Project file with metadata and dependencies.
- **appsettings.json**: General configuration settings.
- **appsettings.Development.json**: Environment-specific settings for development.



### Running dotnet webapp

```
azureuser@sre-vm:~/AshuwebApp$ ls
AshuwebApp.csproj  Pages  Program.cs  Properties  appsettings.Development.json  appsettings.json  obj  wwwroot


azureuser@sre-vm:~/AshuwebApp$ dotnet run
Building...
warn: Microsoft.AspNetCore.DataProtection.KeyManagement.XmlKeyManager[35]
      No XML encryptor configured. Key {916c66eb-1a6f-49e2-bf5a-01d8f97c60d9} may be persisted to storage in unencrypted form.
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: http://localhost:5184
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]

```

