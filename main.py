import boto3

def list_s3_buckets():
    # Create a Boto3 client for S3
    s3_client = boto3.client('s3')
    
    try:
        # List all S3 buckets
        response = s3_client.list_buckets()
        
        # Extract bucket names from the response
        bucket_names = [bucket['Name'] for bucket in response['Buckets']]
        
        return bucket_names
    
    except Exception as e:
        print("An error occurred:", e)
        return []

if __name__ == "__main__":
    # Call the function to list S3 buckets
    buckets = list_s3_buckets()
    
    if buckets:
        print("S3 Buckets:")
        for bucket in buckets:
            print(bucket)
    else:
        print("No S3 buckets found.")
