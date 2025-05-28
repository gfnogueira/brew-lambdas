# AWS Lambda USD to BRL Quote Fetcher (Terraform)

This module creates a Lambda function in Python that fetches the current USD to BRL exchange rate from AwesomeAPI and logs it to CloudWatch.

## 🔧 Setup

1. Run `terraform init`
2. Run `terraform apply`

## 📦 Includes

- IAM Role and Permissions
- Python Lambda Function (`lambda/dolar.py`)
- CloudWatch Log Group
- Archive of the function using `archive_file`

## 🔁 Sample Output

The Lambda prints the current USD value:
```
Current dollar rate: R$5.32
```

## 📂 Structure

```
lambda_dolar/
├── main.tf
├── variables.tf
├── outputs.tf
├── lambda/
│   └── dolar.py
```
