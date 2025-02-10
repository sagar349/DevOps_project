From golang:1.22-alpine AS builder

WORKDIR /app

Copy . .
# Copy all files from current directory to /app

RUN go mod download 
# IT Download dependencies

RUN go build -o prdocut-catalog ./
# Build binary

From alpine:latest AS release
# distroless image is a minimal image that contains only your application and its runtime dependencies
# scratch is an empty image
# second stage is executed as a container

WORKDIR /app

COPY ./prdocuts.json ./products.json
# Copy products.json file from current directory to /app
# Because products.json file is not included in the binary , it is a data file
# ADD is used to copy files from remote URL and extract tar files

COPY --from=builder /app/product-catalog ./product-catalog

ENV PRODUCT_CATALOG_PORT 8088

ENTRYPOINT ["./product-catalog"]


# Copy binary on to second stage in multi-stage build