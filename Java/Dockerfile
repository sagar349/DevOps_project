FROM eclipse-temurin:21-jdk AS build

WORKDIR /app

COPY gradlew* settings.gradle build.gradle ./
# it will download the gradle version specified in the gradle-wrapper.properties file
# and will use it to build the project
COPY ./gradle ./gradle
# it will download the dependencies specified in the build.gradle file

RUN chmod +x ./gradlew

RUN ./gradlew 

RUN ./gradlew downloadRepos
# till here we are downloading the dependencies
# and the gradle version specified in the gradle-wrapper.properties file

COPY . .

COPY ./pb ./proto

RUN chmod +x ./gradlew

RUN ./gradlew installDist -PprotoSrcDir=./proto

# Till here we are building the project

###################################

FROM eclipse-temurin:21-jre
# this image contain the jre only
WORKDIR /app

COPY --from=build /app ./app

ENV AD_PORT 9099

ENTRYPOINT ["./build/install/opentelemetry-demo-ad/bin/Ad"]

# Entrypoint is provided by developer to run the application