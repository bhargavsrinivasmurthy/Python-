import os
import boto3
from moto import mock_s3, mock_sns

from Task1 import run_monitor, prefix_key, bytes_to_human


@mock_s3
@mock_sns
def test_scan_bucket_and_no_alert(monkeypatch):
    bucket = "infosys-client-datalake-prod"
    region = "us-east-1"
    sns_topic_arn = "arn:aws:sns:us-east-1:123456789012:dummy-topic"

    s3 = boto3.client("s3", region_name=region)
    s3.create_bucket(Bucket=bucket)
    s3.put_object(Bucket=bucket, Key="folder1/file1.txt", Body=b"a" * 1024 * 1024)
    s3.put_object(Bucket=bucket, Key="folder2/file2.txt", Body=b"a" * 2 * 1024 * 1024)

    sns = boto3.client("sns", region_name=region)
    sns.create_topic(Name="dummy-topic")

    monkeypatch.setenv("BUCKET_NAME", bucket)
    monkeypatch.setenv("THRESHOLD_GB", "5")
    monkeypatch.setenv("SNS_TOPIC_ARN", sns_topic_arn)
    monkeypatch.setenv("AWS_REGION", region)

    result = run_monitor()

    assert result == 0


@mock_s3
@mock_sns
def test_scan_bucket_alert(monkeypatch):
    bucket = "infosys-client-datalake-prod"
    region = "us-east-1"

    s3 = boto3.client("s3", region_name=region)
    s3.create_bucket(Bucket=bucket)

    # this is 15 MB not 60 GB due moto limit, but acts as breach with low threshold
    s3.put_object(Bucket=bucket, Key="a/bigfile.dat", Body=b"a" * 15 * 1024 * 1024)

    sns = boto3.client("sns", region_name=region)
    topic_arn = sns.create_topic(Name="dummy-topic")["TopicArn"]

    monkeypatch.setenv("BUCKET_NAME", bucket)
    monkeypatch.setenv("THRESHOLD_GB", "0.01")
    monkeypatch.setenv("SNS_TOPIC_ARN", topic_arn)
    monkeypatch.setenv("AWS_REGION", region)

    result = run_monitor()

    assert result == 0


def test_prefix_key():
    assert prefix_key("dir1/file.txt") == "dir1"
    assert prefix_key("singlefile") == "<root>"
    assert prefix_key("/startingslash/file") == ""


def test_bytes_to_human():
    assert bytes_to_human(1023).endswith("B")
    assert bytes_to_human(1024).endswith("KB")
    assert bytes_to_human(1024 * 1024).endswith("MB")
