FROM mcr.microsoft.com/dotnet/sdk:7.0
LABEL name="ashutoshh"
LABEL email="ashutoshh@linux.com"
RUN dotnet --version 
WORKDIR /app
COPY loginPage /app/
RUN dotnet restore && \ 
    dotnet build --configuration Release --output ./output 
ENTRYPOINT ["dotnet", "/app/output/loginPage.dll" ,"--urls", "http://0.0.0.0:5001"]




