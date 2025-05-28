output "lambda_function_name" {
  value = aws_lambda_function.dolar_cotacao.function_name
}

output "lambda_log_group" {
  value = aws_cloudwatch_log_group.lambda_log_group.name
}
