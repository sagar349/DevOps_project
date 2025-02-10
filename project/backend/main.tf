provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "example" {
    bucket = "sagar-terraform-bucket-1234"
    lifecycle {
        prevent_destroy = true # It will prevent the bucket from being deleted
    }

}

resource "aws_dynamodb_table" "dynamo-db-table" {
    name           = "sagar-terraform-dynamo-db-table-1234"
    lifecycle {
        prevent_destroy = true # It will prevent the table from being deleted
    }
    billing_mode   = "PAY_PER_REQUEST"
    hash_key       = "LockID"
    attribute {
        name = "LockID"
        type = "S"
    }
    tags = {
        Name = "sagar-terraform-dynamo-db-table"
    }
}

