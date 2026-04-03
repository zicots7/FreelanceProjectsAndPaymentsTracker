FROM maven:3-eclipse-temurin-25-alpine AS build

WORKDIR /home/app/freelanceTrackerPdf

COPY . .

RUN mvn clean package -DskipTests

FROM eclipse-temurin:25-jre-alpine AS deploy

WORKDIR /home/app/freelanceTrackerPdf/build

COPY --from=build /home/app/freelanceTrackerPdf/target/*.jar FreelanceTrackerPdf.jar


EXPOSE 8080


CMD ["java","-jar","FreelanceTrackerPdf.jar"]
