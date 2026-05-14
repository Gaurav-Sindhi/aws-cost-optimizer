# Automated AWS Cost Optimizer

## 📌 Overview

This project automatically reduces AWS costs by stopping idle EC2 instances using AWS Lambda and CloudWatch.

## 🧰 Services Used

* AWS Lambda
* Amazon EC2
* Amazon CloudWatch

## ⚙️ How It Works

* CloudWatch triggers Lambda every hour
* Lambda checks EC2 instances
* Stops running instances to save cost

## 📊 Benefits

* Reduces unnecessary AWS billing
* Fully automated
* Serverless solution

## 🚀 Future Improvements

* Stop only idle instances (based on CPU)
* Send SNS alerts before stopping
* Add tagging-based filtering
