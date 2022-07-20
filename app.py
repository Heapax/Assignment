#!/usr/bin/env python3
### Read the S3 bucket
### Download the required files, and display an according status message
# Import libraries
import boto3
from flask import Flask

# Connect to S3 bucket
s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-1',
    aws_access_key_id='[Access_Key]',
    aws_secret_access_key='[Secret_Access_Key]'
)

dog = s3.Bucket('[bucketName]').Object('dog.jpg').get()
goat = s3.Bucket('[bucketName]').Object('goat.jpg').get()

try:
    cat = s3.Bucket('[bucketName]').Object('cat.jpg').get()

except:
    cat = "Error"
    print("no luck finding cat.jpg")

print(dog)
print(type(goat))

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')